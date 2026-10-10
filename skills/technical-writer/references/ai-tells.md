# How machine prose gives itself away

Read this when revising a draft, or when a reader says something "sounds AI". Each tell has
a tag: **[Q]** means a quantitative study backs it, **[E]** means editors and heavy users
report it but nobody has measured it. Sources are at the end.

The point of this file is not to dodge detectors. It is to get rid of the habits that make
prose worse, and those habits happen to be what readers notice.

## The finding that matters most

Readers who use chatbots a lot are very good at spotting machine text. In one study a vote
of five such readers misjudged 1 article out of 300. That beat most commercial detectors,
including on paraphrased and "humanized" text. They did not judge by single words. They
judged by formality, originality and clarity (Russell et al. 2025) [Q].

So swapping words does not work. Text with no "delve" in it still reads as machine-written
when it has no opinion, no specifics and the same rhythm all the way through. Fix the
thinking first and the sentences second.

## Deep tells (fix these first)

| Tell | What it looks like | Why it happens |
|---|---|---|
| No position | Every claim is balanced, hedged or "it depends". The piece ends neutral. | Preference tuning rewards safe answers. Heavy LLM use is linked to more essays that take no side (Abdulhai et al. 2026, unverified) [Q-ish] |
| Generic over particular | "many teams", "various tools", "significant improvements" where a person would name the team, the tool and the number. | The model averages over many possible texts; particulars are rare in the average. [E] |
| Sameness | Different prompts produce the same structure, the same moves and the same closing line. The skeleton gives it away even when every sentence is clean: claim, example, list of three, caveats, closing rule. | Instruction tuning, not base models, makes co-written essays converge (Padmakumar & He 2024) [Q] |
| Uniform smoothness | Every sentence is grammatical, mid-length and the same register. There are no rough edges, asides or changes of pace. | Lower variation in sentence length and structure than human text (2023 study; weaker evidence) [Q, weak] |
| Low density | Three sentences say what one would. The paragraph restates the heading, makes the point, then restates the point. | [E] |
| Templates | The same part-of-speech skeletons recur ("X is not just Y; it is Z that W"). 76% of templates in model output also appear in pretraining data, vs 35% for human text, and RLHF does not remove them (Shaib et al. 2024). | [Q] |

## Sentence and syntax tells

- **Trailing participle that pretends to analyse.** "The cache was rebuilt, highlighting the
  importance of observability." Instruction-tuned models use present participial clauses at
  2 to 5 times the human rate (Reinhart et al. 2025) [Q]. Fix: delete it, or make it a real sentence
  with a subject that did something.
- **Nominalization.** "The implementation of the optimization of the query" instead of "we
  made the query faster". About 1.5 to 2 times the human rate, higher in tuned models (Reinhart) [Q].
  Fix: find the verb hiding in the noun and give it a subject.
- **Negative parallelism.** "It's not a bug, it's a feature." "This isn't about speed. It's
  about trust." "Not just X, but Y." Reported at about 3x human frequency and the hardest tic
  to shake across ChatGPT, Claude and Gemini (Pangram via The Atlantic, 2026) [E, vendor
  figure]. Fix: state the positive claim. If the contrast is real and the reader actually
  believes X, keep one, once per piece, and earn it.
- **Rule of three.** Lists of three adjectives or three clauses because three sounds finished
  [E]. Fix: count the real items. Two is fine. Four is fine.
- **Copula avoidance.** "serves as", "stands as", "boasts", "functions as" for "is" and "has"
  [E]. Fix: use "is" and "has".
- **Fake suspense.** "The result? A 40% drop." "The catch? It doesn't scale." [E] Fix: say it.
- **Vague "This".** "This highlights...", "This means..." with no noun after "This" [E]. Fix:
  name the thing: "This retry loop means...".
- **Hedge stacks.** "may potentially", "could arguably", "to some extent" [E]. Fix: hedge once,
  where the uncertainty is real, and say what it depends on.

## Word tells

Excess vocabulary since 2023, mostly verbs and adjectives (Kobak et al. 2025; Juzek & Ward
2025) [Q]: delve, underscore, showcase, pivotal, intricate, tapestry, testament, realm,
landscape, crucial, robust, seamless, leverage, foster, harness, elevate, multifaceted,
nuanced, comprehensive, meticulous, vibrant, notably, moreover, furthermore, additionally.

Juzek & Ward's evidence points to preference tuning (RLHF) as the cause, not training data.
In practice the list moves. When one word gets noticed and suppressed, another takes its
place. Treat the list as a symptom check, not as the cure.

Intensifiers belong here too: truly, incredibly, deeply, genuinely, fundamentally,
remarkably. And the promotional register: "game-changing", "cutting-edge", "unlock",
"empower", "elevate your workflow".

## Structure and formatting tells

- Bullets where an argument should be. Bullets with a bold lead ("**Speed:** ...") stacked in
  parallel and all about the same length [E].
- Title Case Headings in a doc that otherwise uses sentence case [E].
- A summary at the end of every section, and a "Conclusion" that repeats the introduction [E].
- Signposting: "Let's dive in", "Here's the thing", "In this post we'll explore" [E].
- A tidy, quotable closing line that sounds profound and says nothing ("In the end, the best
  code is the code that serves people.") [E].
- Emoji bullets, needless tables, bold scattered through paragraphs [E].
- Chat residue: "I hope this helps", "Great question", "Let me know if you'd like..." [E].

## Stance and content tells

- Inflated significance: "a pivotal moment", "reshaping the landscape", "a testament to" [E].
- Vague attribution: "experts say", "studies show", "it is widely believed" with no source [E].
- Invented specifics. A confident number, quote or citation that doesn't exist is worse than
  being generic, because it is false. Never invent a particular to look human.

## Fixes that backfire

The evidence here is thin. Treat the first two items as established and the rest as
judgement.

1. **Detector-chasing.** Detectors are unreliable and humanizer tools evade them (Pangram
   2025, vendor preprint). The target is a good reader, not a classifier.
2. **Killing one glyph or word.** Newer models suppress em dashes, but the other tells barely
   moved. "Delve" faded and "it's not X, it's Y" stayed. Fixing tokens leaves the habit.
3. **Swapping em dashes one for one** for colons, semicolons or parentheses. The rhythm and the
   structure stay the same, so the text still reads as generated. Rewrite the sentence instead.
4. **Fake roughness.** Planted typos, slang, "lol", or forced casualness. It reads as a costume.
   Human prose has specific opinions, not spelling mistakes.
5. **Overcorrecting into choppiness.** Ten short punchy sentences in a row is its own template.
   Vary the length because the content varies.
6. **Over-hedging after a fix.** Removing confident claims to avoid sounding promotional leaves
   prose that commits to nothing.
7. **Mechanical checks as proof.** A clean linter run is necessary, not sufficient. Wikipedia's
   own guide says its signs describe; they don't prove.

## Sources

- Reinhart et al. "Do LLMs write like humans?
  Variation in grammatical and rhetorical styles." PNAS 2025. doi:10.1073/pnas.2422455122
- Kobak, González-Márquez, Horvát, Lause. "Delving into LLM-assisted writing in biomedical
  publications through excess vocabulary." Science Advances 11(27), 2025.
  doi:10.1126/sciadv.adt3813
- Juzek & Ward. "Why Does ChatGPT 'Delve' So Much? Exploring the Sources of Lexical
  Overrepresentation in Large Language Models." COLING 2025. arXiv:2412.11385
- Shaib et al. "Detection and Measurement of Syntactic Templates in Generated Text."
  EMNLP 2024. arXiv:2407.00211
- Russell, Karpinska, Iyyer. "People who frequently use ChatGPT for writing tasks are accurate
  and robust detectors of AI-generated text." ACL 2025. arXiv:2501.15654
- Padmakumar & He. "Does Writing with Language Models Reduce Content Diversity?" ICLR 2024.
- Abdulhai et al. 2026, arXiv:2603.18161 (search-summary only; not verified at source).
- Wikipedia: "Signs of AI writing" (WikiProject AI Cleanup), read 2026-10.
- The Atlantic, July 2026, on the "it's not X, it's Y" tic, via aiweekly.co (secondary).
- Pangram Labs. "DAMAGE: Detecting Adversarially Modified AI Generated Text." arXiv:2501.03437
