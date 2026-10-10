#!/usr/bin/env python3
"""Flag mechanical signs of machine-written prose in a Markdown or text file.

Usage:
    python tells.py FILE [FILE ...]        # human-readable report
    python tells.py --json FILE            # machine-readable
    cat draft.md | python tells.py -       # read stdin

Standard library only. Code blocks, inline code, front matter and URLs are
skipped. The script finds candidates; it does not judge them. A hit is a
prompt to reread the sentence, not an order to delete it. Zero hits does not
mean the prose is good: the tells that matter most (no point of view, no
specifics, padding) are invisible to a regex.
"""
import json
import re
import statistics
import sys

# Words whose frequency rose sharply in text after 2023 (Kobak et al. 2025,
# Juzek & Ward 2025, Wikipedia "Signs of AI writing"), plus marketing filler.
WORDS = """
delve delves delving tapestry testament pivotal crucial crucially intricate
intricacies multifaceted seamless seamlessly robust leverage leveraging
elevate elevates foster fosters fostering harness harnessing unlock unlocks
unleash empower empowers empowering vibrant nuanced meticulous meticulously
notably moreover furthermore additionally paramount holistic synergy
streamline streamlines cutting-edge ever-evolving game-changer game-changing
embark realm landscape underscore underscores underscoring showcase
showcases showcasing boasts commendable invaluable enhance enhances
enduring profound transformative groundbreaking interplay navigate
navigating bustling nestled garner garnered align aligns resonate
resonates intrinsic noteworthy comprehensive utilize utilizes
dependable thoughtful meaningful
""".split()

# (label, regex). Case-insensitive. Keep these specific; vague patterns
# produce noise and train the writer to ignore the report.
INTENSIFIER = ("intensifier", r"\b(?:very|really|truly|incredibly|remarkably|deeply|profoundly|undeniably|"
     r"genuine|genuinely|fundamentally|simply|clearly|obviously|vastly)\b")

PATTERNS = [
    ("em/en dash", r"[—–]| -- "),
    ("narrated significance",
     r"\b(?:the one (?:line|thing|rule|takeaway) to (?:hold|keep|remember)|"
     r"here is (?:the|an?) [\w-]+ that (?:makes|matters|counts)|"
     r"what makes (?:this|it) [\w ]{0,24}worth (?:reading|your time)|"
     r"the (?:real|whole) (?:point|lesson|takeaway) (?:is|here)|the key (?:thing|point) (?:is|here)|"
     r"exactly what separates|importantly)\b"),
    ("manufactured antithesis (stops X, starts Y)", r"\bstops? \w+ing\b[^.?!]{0,40}\bstarts? \w+ing\b"),
    ("colon-zinger", r"(?<=\w): (?:a|an|the) \w+(?: \w+){0,5}\.(?:\s|$)"),
    ("negative parallelism (not X, but Y)",
     r"\bnot (?:just|only|merely|simply)\b[^.?!]{1,80}\bbut(?: also)?\b"),
    ("negative parallelism (it's not X, it's Y)",
     r"\b(?:it|this|that)(?:'s| is)(?: not|n't)\b[^.?!]{1,60}[.;,—–-]\s*(?:it|this|that)(?:'s| is)\b"),
    ("negative parallelism (X isn't Y. It's Z)",
     r"\b(?:is|are|was|were)n't (?:just |about |only |merely )?[^.?!]{1,60}[.;]\s+"
     r"(?:it|they|this|that)(?:'s|'re| is| are| was| were)\b"),
    ("contrast fragment (Not the X. The Y.)",
     r"(?:^|[.!?]\s+)Not (?:the|a|an) [^.?!]{1,40}\.\s+(?:The|A|An|It)\b"),
    ("contrast pair (One is X. The other is Y.)", r"\bOne is\b[^.?!]{1,60}\.\s+The other is\b"),
    ("fake suspense (The X? Y.)",
     r"(?:^|[.!]\s+)(?:The|And the|So the) \w+(?: \w+)?\?\s+[A-Z]"),
    ("signposting", r"\b(?:here's (?:the thing|why|how|what|the (?:part|bit|kicker|catch|twist))|let's (?:dive|break|unpack|explore|take a look)|"
     r"buckle up|without further ado|in this (?:post|article|guide),? (?:we|I)(?:'ll| will))\b"),
    ("summary closer", r"\b(?:in conclusion|in summary|to sum up|the bottom line|at the end of the day|"
     r"ultimately(?=,)|all in all)\b"),
    ("filler", r"\b(?:in order to|due to the fact|at this point in time|in the event that|"
     r"that said|the ability to)\b"),
    ("throat-clearing", r"\b(?:it(?:'s| is) (?:worth noting|important to note|important to remember|"
     r"crucial to)|it should be noted|needless to say|when it comes to|at its core|"
     r"in today's (?:\w+ )?(?:world|landscape|age|era))\b"),
    ("copula avoidance (serves as / stands as)", r"\b(?:serves|stands|acts|functions) as (?:a|an|the)\b"),
    ("inflated role", r"\bplays? an? (?:crucial|pivotal|key|vital|significant|important|central) role\b|"
     r"\b(?:fundamental|paradigm|seismic) shift\b|\bsets the stage\b|\breaps? (?:the )?(?:rewards|benefits)\b|\breshap(?:es|ing) the\b"),
    ("testament / legacy talk", r"\b(?:a testament to|stands as a|leaves? a lasting|rich (?:history|tapestry))\b"),
    ("trailing -ing analysis", r",\s(?:highlighting|underscoring|emphasizing|reflecting|showcasing|"
     r"demonstrating|illustrating|signaling|ensuring|cementing|solidifying|paving|"
     r"contributing|fostering|making it)\b"),
    ("vague 'This verb'", r"(?:^|[.!?]\s+)This (?:highlights|underscores|shows|demonstrates|ensures|"
     r"means|allows|enables|reflects|illustrates)\b"),
    ("whether-you're opener", r"\bwhether you(?:'re| are) an? \w+"),
    ("false range (from X to Y)", r"\bfrom \w+(?: \w+)? to \w+(?: \w+)?,? (?:and everything|to)\b"),
    ("hedge stack", r"\b(?:may|might|could) (?:potentially|possibly|perhaps)\b|\barguably\b|"
     r"\bit could be argued\b|\bto some extent\b"),
    ("chat residue", r"\b(?:I hope this helps|great question|certainly!|absolutely!|as an AI|"
     r"I'd be happy to|feel free to|let me know if)\b"),
    ("engagement-bait closer", r"\b(?:I'd love to hear|what do you think\?|let me know in the comments|"
     r"share your (?:thoughts|experience)|drop a comment)"),
    # Opus 5.5-era tells (Graphite, Oct 2026).
    ("'matters' frame", r"\b(?:this|that|it) matters\b|\bwhy (?:\w+ ){1,3}matters?\b|"
     r"\bmatters (?:most|enormously|more than)\b|\bwhat matters (?:is|here|most)\b"),
    ("forecast/next-step frame", r"\blooking ahead\b|\bwhat comes next\b|\badds? another layer\b|"
     r"\bjust as important\b|\brather than simply\b|\b(?:is|are) more than (?:a|an|just)\b"),
    ("helpfulness pitch", r"\b(?:can help you|helps you (?:avoid|stay|get|make|keep)|makes it easier|"
     r"is especially (?:helpful|useful))\b"),
    ("superlative", r"\b(?:one of the (?:best|most)|perhaps the most|the most (?:powerful|popular|important|"
     r"effective|significant))\b"),
    ("everyday/key/real-world filler", r"\b(?:key (?:takeaways?|insights?|considerations?)|"
     r"real-world (?:applications?|scenarios?|examples?)|best practices)\b"),
]

PATTERNS.append(INTENSIFIER)

TRIAD = re.compile(r"\b\w+(?: \w+)?, \w+(?: \w+)?,? and \w+(?: \w+)?\b")
BOLD_BULLET = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+\*\*[^*]+\*\*")
BULLET = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")
HEADING = re.compile(r"^#{1,6}\s+(.*)$")
SMALL = {"a", "an", "the", "and", "or", "but", "for", "nor", "of", "on", "in",
         "to", "at", "by", "with", "vs", "via", "as", "is"}


def strip_noise(text):
    """Blank out front matter, fenced code, inline code and URLs, keeping line numbers."""
    lines = text.splitlines()
    out, in_fence, in_front = [], False, bool(lines) and lines[0].strip() == "---"
    for i, line in enumerate(lines):
        s = line.strip()
        if in_front:
            out.append("")
            if i > 0 and s == "---":
                in_front = False
            continue
        if s.startswith("```") or s.startswith("~~~"):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence or line.startswith("    ") or s.startswith("<"):
            out.append("")
            continue
        if re.fullmatch(r"\*[^*]*\bAI\b[^*]*\*", s):
            out.append("")  # the disclosure line is required wording, not prose
            continue
        line = re.sub(r"`[^`]*`", "CODE", line)
        # A short quoted phrase is a mention of a tell, not a use of it.
        line = re.sub(r'"[^"\n]{1,60}"|\u201c[^\u201d\n]{1,60}\u201d', '"Q"', line)
        line = re.sub(r"\]\([^)]*\)", "]", line)
        line = re.sub(r"https?://\S+", "URL", line)
        out.append(line)
    return out


def sentences(lines):
    """Split prose into sentences. Paragraphs and list items are separate blocks, so a list
    never merges into one long 'sentence'. Headings, tables and TODO markers are skipped."""
    blocks, cur = [], []
    for l in lines:
        s = l.strip()
        if not s or HEADING.match(l) or s.startswith("|") or s.startswith("[TODO"):
            blocks.append(" ".join(cur)); cur = []
        elif BULLET.match(l):
            blocks.append(" ".join(cur)); cur = [BULLET.sub("", l)]
        else:
            cur.append(s)
    blocks.append(" ".join(cur))
    out = []
    for b in blocks:
        out += re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(])", b)
    return [p for p in out if len(p.split()) >= 3]


def stubs(lines):
    """Verbless 1-3 word sentences right after a long one: the performed fragment."""
    found = []
    for n, line in enumerate(lines, 1):
        if HEADING.match(line) or BULLET.match(line) or line.lstrip().startswith("|"):
            continue
        parts = re.split(r"(?<=[.!?])\s+", line.strip())
        for prev, cur in zip(parts, parts[1:]):
            words = cur.rstrip(".!?").split()
            if 1 <= len(words) <= 3 and len(prev.split()) >= 12 and cur.endswith(".") \
                    and not re.search(r"\b(?:is|are|was|were|do|does|did|has|had|can|will|\w+n\'t|"
                                      r"\w+ed|\w+s)\b", cur.lower()):
                found.append({"line": n, "kind": "stubby fragment after a long sentence",
                              "text": cur[:90]})
    return found


def is_title_case(h):
    words = [w for w in re.findall(r"[A-Za-z][\w'-]*", h)]
    if len(words) < 3:
        return False
    tail = [w for w in words[1:] if w.lower() not in SMALL]
    return len(tail) >= 2 and all(w[0].isupper() for w in tail)


def analyse(text):
    lines = strip_noise(text)
    body = "\n".join(l for l in lines if not HEADING.match(l))
    nwords = max(1, len(re.findall(r"\b\w+\b", body)))
    per_k = lambda n: round(n * 1000 / nwords, 1)
    hits = []

    word_re = re.compile(r"\b(" + "|".join(map(re.escape, WORDS)) + r")\b", re.I)
    compiled = [(label, re.compile(rx, re.I)) for label, rx in PATTERNS]
    for n, line in enumerate(lines, 1):
        if not line.strip():
            continue
        for m in word_re.finditer(line):
            hits.append({"line": n, "kind": "AI-favoured word", "text": m.group(0)})
        seen = []
        for label, rx in compiled:
            for m in rx.finditer(line):
                if label != "em/en dash":
                    if any(a < m.end() and m.start() < b for a, b in seen):
                        continue  # one finding per span, even if two patterns match it
                    seen.append(m.span())
                hits.append({"line": n, "kind": label, "text": m.group(0).strip()[:90]})
        h = HEADING.match(line)
        if h and not line.startswith("# ") and is_title_case(h.group(1)):
            hits.append({"line": n, "kind": "Title Case heading", "text": h.group(1)[:90]})
        elif h and re.search(r"(?<![.!?:]) (?:Of|The|And|To|In|For|A|An|On|With) ", h.group(1)):
            hits.append({"line": n, "kind": "capitalized small word in title", "text": h.group(1)[:90]})

    hits += stubs(lines)
    sents = sentences(lines)
    lens = [len(s.split()) for s in sents]
    stats = {"words": nwords, "sentences": len(lens)}
    if len(lens) >= 5:
        mean = statistics.mean(lens)
        sd = statistics.pstdev(lens)
        stats.update(mean_sentence=round(mean, 1), sd_sentence=round(sd, 1),
                     variation=round(sd / mean, 2),
                     short_sentences_pct=round(100 * sum(l <= 8 for l in lens) / len(lens)),
                     long_sentences_pct=round(100 * sum(l >= 30 for l in lens) / len(lens)))

    bullets = sum(1 for l in lines if BULLET.match(l))
    bold_bullets = sum(1 for l in lines if BOLD_BULLET.match(l))
    stats.update(
        em_dashes_per_1k=per_k(len(re.findall(r"[—–]|\s--\s", body))),
        semicolons_per_1k=per_k(body.count(";")),
        colons_in_prose_per_1k=per_k(len(re.findall(r"[a-z]: [a-z]", body))),
        triads_per_1k=per_k(len(TRIAD.findall(body))),
        bullet_lines=bullets, bold_lead_bullets=bold_bullets,
    )

    warnings = []
    if stats.get("variation", 1) < 0.4:
        warnings.append("Sentence lengths are uniform (variation < 0.40). Human prose mixes "
                        "short and long sentences; vary the rhythm where the content allows.")
    if stats["em_dashes_per_1k"] > 0:
        warnings.append("Em dashes present. The house style uses none: rewrite each sentence. "
                        "Don't swap them for semicolons or colons; that keeps the same rhythm.")
    semis, colons = body.count(";"), len(re.findall(r"[a-z]: [a-z]", body))
    if (semis >= 3 and stats["semicolons_per_1k"] > 4) or (colons >= 3 and stats["colons_in_prose_per_1k"] > 6):
        warnings.append("Heavy semicolon/colon use, often a sign of em dashes swapped one for one.")
    if len(TRIAD.findall(body)) >= 2 and stats["triads_per_1k"] > 4:
        warnings.append("Many 'X, Y, and Z' lists. Check whether each list really has three items.")
    if bullets and bold_bullets / bullets > 0.5 and bold_bullets >= 3:
        warnings.append("Most bullets open with a bold label. Consider prose, or plain bullets.")
    if bullets > 0.4 * max(1, stats["sentences"]) and bullets >= 8:
        warnings.append("Bullet-heavy. Argument and explanation belong in paragraphs.")
    return {"stats": stats, "warnings": warnings, "hits": hits}


def report(name, r):
    s = r["stats"]
    print(f"== {name}")
    print(f"   {s['words']} words, {s['sentences']} sentences", end="")
    if "mean_sentence" in s:
        print(f"; sentence length mean {s['mean_sentence']}, sd {s['sd_sentence']}, "
              f"variation {s['variation']} ({s['short_sentences_pct']}% <=8 words, "
              f"{s['long_sentences_pct']}% >=30)")
    else:
        print()
    print(f"   per 1k words: em dash {s['em_dashes_per_1k']}, semicolon {s['semicolons_per_1k']}, "
          f"colon {s['colons_in_prose_per_1k']}, triads {s['triads_per_1k']}; "
          f"bullets {s['bullet_lines']} ({s['bold_lead_bullets']} bold-led)")
    for w in r["warnings"]:
        print(f"   ! {w}")
    by_kind = {}
    for h in r["hits"]:
        by_kind.setdefault(h["kind"], []).append(h)
    for kind, hs in sorted(by_kind.items(), key=lambda kv: -len(kv[1])):
        print(f"   [{len(hs)}] {kind}")
        for h in hs[:12]:
            print(f"       L{h['line']}: {h['text']}")
        if len(hs) > 12:
            print(f"       ... {len(hs) - 12} more")
    if not r["hits"] and not r["warnings"]:
        print("   no mechanical tells found (that is necessary, not sufficient)")


def main(argv):
    as_json = "--json" in argv
    files = [a for a in argv if a != "--json"] or ["-"]
    results = {}
    for f in files:
        text = sys.stdin.read() if f == "-" else open(f, encoding="utf-8").read()
        results[f] = analyse(text)
    if as_json:
        json.dump(results, sys.stdout, indent=2)
    else:
        for f, r in results.items():
            report(f, r)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")
    main(sys.argv[1:])
