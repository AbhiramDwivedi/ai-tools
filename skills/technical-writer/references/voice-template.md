# Writing your own voice profile

The skill reads a personal profile from `~/.config/technical-writer/voice.md` (on Windows,
`%USERPROFILE%\.config\technical-writer\voice.md`). It lives outside the skill folder, so
updating or reinstalling the skill never overwrites it. When it exists, it wins over the
default `voice.md` in this folder wherever the two disagree. Anything your profile leaves
out falls back to the default.

Copy the outline below into that file and fill it in. Short and true beats long and
aspirational. The most useful section is the list of edits you keep making to AI drafts.

```markdown
# My voice

## Who I am
One or two lines: what you do, what you write (blog, docs, newsletter, papers), and for
whom.

## The register in one line
How you sound to a reader, in a sentence.

## Registers
The kinds of piece you write, and for each: person (I / you / we), how it opens, rhythm,
how it closes. Leave out any you don't write; the default covers them.

## Edits I keep making to AI drafts
Before/after pairs from your own revisions. Five real ones beat twenty invented ones. Add a
pair each time you fix the same thing twice.

## Hard rules
Things you never or always do: punctuation (em dashes allowed or not), spelling (US or UK),
heading case, words you won't use, how you cite.

## Disclosure
Whether to end a piece with a line saying AI helped, and the wording you want. If you
don't disclose, say "No disclosure" here so the skill stops offering one.

## Samples
Two to four short passages you wrote yourself, with no AI help, that sound like you at
your best. Say which register each one shows.

## Anti-samples
Lines from AI drafts you had to cut, with the fix. These teach more than the samples do.
```
