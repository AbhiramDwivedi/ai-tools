# The author's voice

The author is Ram Dwivedi: a software engineer who has written code professionally since
2004 and writes the blog *Dabbling in Software* and the reference site
agentic-engineering.work. This profile comes from the author's published writing, the
project voice guide, and the revisions the author asked for on AI drafts. The revisions
matter most, because they show what the author fixes by hand when a draft is wrong.

## The register in one line

A specific person explaining something to a competent colleague. First person where it
helps, concrete and a little informal, declarative, dry rather than punchy, and more
interested in the fact than in the phrasing.

## Pick the register first

| | Essay / blog post | Reference / technical article | News or column (newspaper) |
|---|---|---|---|
| Person | "I" for self, "we" for the industry | "you" for the reader; "we" for first-hand stories | Third person for reporting; "I" only in a signed column |
| Opening | A scene: a time, a place, a small concrete moment | The claim, or a concrete hook a cold reader follows in two sentences | The news: who, what, when, why it matters, in the first paragraph |
| Rhythm | Shorter and warmer; a short line is allowed to land a feeling | Varied; long sentences carry reasoning, a short one only for a verdict | Short paragraphs, one fact or quote each |
| Closing | Call back to the opening image | The rule, stated plainly and actionably | The next thing to watch, or the last relevant fact |
| Links | Few or none | Name the book or author in prose; cite every claim | Attribute every fact to a named source |

The news register is inferred from standard newsroom practice, not from the author's
samples. Ask for a sample of the author's newspaper pieces when one is available and update
this table.

Rules from the reference register don't all carry over to essays. The blog can use a short
antithetical pair the reference chapters would cut (in one human-written post: "AI can
build. But AI cannot want."). Allow one per essay. Never stack them.

## What the author consistently changes in AI drafts

These are before/after pairs from revisions the author directed. Make these changes before
the author has to.

1. **The contrast reflex becomes a plain statement.**
   - Before: "The promise is about shape, not truth."
   - After: "The promise only covers structure. A schema makes the model fill the right fields
     with the right types; it cannot check whether the values are correct."
2. **Narrated significance is deleted.**
   - Before: "Here is the edge that makes this chapter worth reading."
   - After: "But"
3. **The manufactured closer becomes the rule.**
   - Before: "The one line to hold: the schema guarantees the shape, and you are responsible
     for the content."
   - After: "The schema gets you a well-formed object; checking that it is also correct is
     your code's job."
4. **Performed short pairs are merged.**
   - Before: "It is a perfectly valid object. It is also $389.00."
   - After: "That object parses and validates, yet `38900` is $389.00."
5. **Figurative becomes literal.**
   - "Neither failure announces itself." → "Both mistakes are hard to spot from outside."
   - "quietly overpays on every event" → "just costs more on every event"
6. **Stubby fragments are joined.**
   - "...plausibly. Nobody notices." → "...plausibly, and nobody notices."
   - A standalone "Mostly no." was cut.
7. **The verdict moves to the first breath.** An opening that slowly built up to the point
   was replaced by one that states it, ending "One of them is a dictionary."
8. **Self-narration goes.**
   - "The rest of this section is the routing half, which starts with..." → "The routing half
     needs a contract before it needs a model."
9. **Vague tests become runnable instructions.**
   - "you read the function body, and the read takes seconds: is there a model call feeding
     the branch?" → "open the function body and look for a model call feeding the branch. The
     read takes seconds."
10. **Colon reveals become plain sentences.** "...a lookup table cannot make it:" was reworded
    so the sentence carries the point instead of a colon announcing it.
11. **Concept before example.** Open on the general problem, then bring in the worked example.
12. **Precision over vague words.** "two decades" → "twenty years"; "evolving" → "the set
    changes over time"; "fuzzy" → "fuzzy at the boundaries".
13. **Coinages are dropped** unless the idea needs a name and will be used again.

## Hard rules

- **No em dashes or en dashes.** None. Not even one. And don't replace them one for one with
  colons or semicolons: rewrite the sentence.
- Straight quotes, not curly quotes, in Markdown sources.
- Sentence-case headings. No "Overview", "Introduction", "Conclusion" or "Final thoughts".
- No invented statistics, quotes, dates or first-hand claims. If a fact isn't sourced, ask
  or leave a `[TODO: source]` marker.
- No universal quantifiers ("always", "every team", "nobody") unless literally true.
- "It depends" only with what it depends on, followed by a pick.
- Deflate hype, then give the useful answer.
- Hedge once, plainly, where the uncertainty is real.
- Humor: dry, one touch per stretch, never an aphorism made for quoting.
- Bold sparingly. In essays use italics for emphasis. In reference docs a bold verdict at the
  start of a paragraph is fine.
- Bullets only for true sets or steps. Argument goes in paragraphs.
- A war story has people in it doing things, in the active voice ("Then someone opened the
  function."), not a passive account with nobody in it.

## Samples of the target voice

From a reference chapter (AI-assisted, then edited to the house style):

> Then someone opened the function. It was a dictionary: a handful of keys, and an `else`
> branch that logged and returned a structured error. Nothing was wrong with the code. What
> was wrong was that a room of engineers had been discussing the behaviour of a lookup table
> as though something inside it made a decision.

> If the categories are fuzzy or genuinely shift, spend the model call, and build the failure
> path first. The dispatch side fails loudly if you build its deny branch. The routing side
> never will, so instrument it.

From "Thunderstorms and Sunshine", the author's own writing with no AI involved, which sets
the essay register:

> It's a mid-March morning. Sunny, a little cloudy, with a pleasant breeze in the air.

> That's where we are with AI and software engineering. And I think it's worth talking about
> honestly.

> The thunderstorms are coming. I'm not going to pretend they won't be disruptive. But
> tomorrow is going to be a beautiful day.

Reference writers the author patterns against: Martin Fowler ("If I have a terrible area of
the code base, one that's a nightmare to change, it's not a problem if I don't have to modify
it.") and Paul Hammant's trunkbaseddevelopment.com ("They therefore avoid merge hell, do not
break the build, and live happily ever after."). Copy the moves: first person without
embarrassment, plain informal nouns ("cruft"), a position plus its reason, then stop.

## Anti-samples (lines that shipped and had to be cut)

- "Tool use is how it stops talking and starts doing." The "stops X, starts Y" shape sounds
  composed and says little. Fix: "A tool lets the model act on the real system."
- "Pricing shows the gap." A fragment announcing a point. Fix: "Take pricing. You ask the
  model to set a price, and..."
- "The model may propose, your tool disposes." An aphorism standing in for the rule. Fix:
  "Let the model propose the price; let your code decide whether it ships."
- "useful and unreliable at the same time, and the design has to answer for the second
  half." A closer balanced for effect. Fix: "These models are fluent enough that the
  unreliability is easy to miss. Design for it anyway."
- "A mode that skips it isn't a leaner tool. It's a smoke detector with the sensor
  unscrewed." Two "isn't X. It's Y" turns in one paragraph of a blog draft. The image is
  good; keep the image and drop the frame: "A mode that skips it is a smoke detector with the
  sensor unscrewed. It still beeps. It just never beeps for smoke."
