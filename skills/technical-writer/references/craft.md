# Craft: the rules worth keeping, and the writers worth copying

This file condenses three sources into rules you can apply while drafting, then describes the
moves of writers whose technical prose reads as human and smart. Use it when drafting from
scratch or when a revision needs more than deleting tells.

## Zinsser (On Writing Well), applied to technical writing

- **Clarity.** Know what you think before you write. If you can't say the point in two
  sentences, you're not ready to draft. Ask "what am I trying to say?" and then "have I said it?"
- **Simplicity.** Use the short word over the long one, the verb over the noun, the active
  voice over the passive.
- **Brevity.** Clutter is the disease. Cut every word that does no work: "currently", "in
  order to", "basically", "actually", "very", "a number of", "it is important to note that".
  Most first drafts can lose a third without losing a fact.
- **Humanity.** Write as a person to a person. Use "I" when you mean yourself. Your opinions
  and doubts are the part only you can supply.
- **Unity.** Pick one tense, one person, one register and one reader, and keep them.
- **The lead and the ending.** The first sentence has to pull the reader into the second. Stop
  when you've made the point. Don't summarize what the reader just read.

## Google developer documentation style, the parts that carry over to essays

- Second person ("you") for instructions. Present tense. Active voice.
- Sentence case for headings. Headings say what the section is about, not a teaser.
- Put the condition before the instruction: "To rebuild the index, run...", not "Run... to
  rebuild the index."
- Lists for steps and for parallel items that really are parallel. Prose for reasoning.
- Define a term the first time you use it. Spell out an acronym on first use.
- Code, commands, file names and values in code font. Show real, runnable examples.
- Global readers: no idioms that don't translate, no culture-bound jokes in instructions,
  short sentences where precision matters.
- No "simply", "just", "easy", "obviously". What's easy for you is the reader's blocker.
- Use numerals for numbers and include units. "3 retries", "200 ms".

When Google style and the author's voice conflict in an essay, voice wins. In reference docs
and how-to steps, Google style wins.

## Writers to learn from (copy the moves, not the sentences)

- **Martin Fowler.** Starts from a concrete situation seen on real projects. Names the idea,
  defines it in one plain paragraph, then shows where it breaks. Uses "I" freely and admits
  uncertainty plainly ("I don't have a strong opinion here"). Credits colleagues by name.
  Short bliki entries: one idea, said once, then stop.
- **Julia Evans.** Curiosity shows on the page. "I didn't understand X, so I tried Y, and here's
  what happened." Real commands, real output, small surprising details. Never pretends to
  know more than the post shows.
- **Dan Luu.** Blunt claims backed by data and links. Comfortable saying a common belief is
  wrong. Little ornament.
- **Paul Graham.** Plain words, short sentences, one argument pursued to its end.
- **Simon Willison.** Writes up what was actually done, links everything, and says plainly when
  an LLM helped and how. The disclosures are matter-of-fact, never apologetic.
- **Joel Spolsky / Charity Majors.** Opinionated, funny where it fits, stories from the job,
  named villains (practices, not people).

The common thread: a specific person who did a specific thing and has a view about it. That
is the part a model can't fake and the part a reader is looking for.

## When the author's own samples run out

`voice.md` comes from a few essays and one reference site. When a task needs something it
doesn't cover, such as a news story, a README, a talk abstract or a register it doesn't
describe, copy the writers below for that kind of piece. The author's hard rules still apply
(no dashes, no invented facts, sentence-case headings). This list fills gaps in `voice.md`;
it doesn't override it.

| Kind of piece | Writers to copy | The moves |
|---|---|---|
| News report | Reuters and AP wire style. For technical news analysis, Jonathan Corbet at LWN.net | The news goes in the first sentence. Every fact has a named source: "said" for people, "found" or "reported" for a study or document. No adjectives that judge. Short paragraphs. Only quote what someone said better than you could paraphrase it. Headlines are sentence case, a full sentence with a verb, and true without the story. For a study, say who made it, who paid for it, how big it was and what it can't show. With no one to quote, attribute to the document and don't invent a reaction. Numbers follow the publication's style (AP: "Oct. 1", "percent"), which wins over the Google numeral rule. |
| Column or opinion | Paul Ford; Charity Majors; John Gruber at his best | One argument, said in the first few paragraphs. A personal stake, said once. Concrete evidence, then a clear verdict. Dry humor allowed. |
| Essay or blog post | Martin Fowler, Paul Graham, Julia Evans, Dan Luu | See above. Open on a situation, follow one idea to its end, stop. |
| Reference article or explainer | Fowler's long-form articles; Julia Evans; Stripe's API docs | Define the term once and plainly. One worked example, then the general rule. State limits and failure cases. |
| README, how-to, tutorial | Google developer style; Daniele Procida's Diátaxis | Say what kind of document it is: a tutorial, a how-to, reference or an explanation. Don't mix them. Numbered steps start with a verb. Show expected output. |
| Release notes, changelog | Simon Willison's release notes; the Keep a Changelog format | What changed, who it affects, what to do. Link the issue. No "exciting". |

If you're unsure how one of these writers would handle something, ask what a careful expert
on the subject would write for a reader who is short of time. That is usually the answer.

## Moves that make prose read as human and intelligent

1. **Lead with the claim, or with a scene.** Not with context-setting ("In today's
   fast-moving world of...").
2. **One concrete example beats three abstract ones.** Name the tool, the version, the
   number, the error message, the date.
3. **Commit.** Say what you'd do and why. When it really is "it depends", say what it depends
   on and which way you lean.
4. **Show the reasoning, including the wrong turn.** "I assumed the cache was stale. It
   wasn't." Readers trust a writer who shows where they were wrong.
5. **Earn every abstraction.** Introduce a principle after the example that made you believe
   it, not before.
6. **Vary the rhythm because the content varies.** Long sentences to carry a chain of
   reasoning. Short ones to land a point. Not alternating by rule.
7. **Leave out what the reader already knows.** Experts notice padding first.
8. **End on the last useful thing.** An open question, a next step, a sharp consequence. Not
   a moral.
9. **Allow asides and small jokes** where a person would make them. Keep them dry and brief.
10. **Coin a name only when you'll use it again,** and only if the idea doesn't already have one.
