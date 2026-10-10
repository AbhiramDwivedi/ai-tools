# ai-tools

Skills and small tools I use with AI coding agents. Each skill is a folder with a `SKILL.md`,
which both Claude Code and Codex read, so one copy serves both.

## Skills

### technical-writer

Drafts, revises and reviews technical prose (blog posts, reference docs, newspaper pieces,
READMEs) so it reads like a sharp engineer wrote it and not a model.

I used to ask for three things on every piece: the humanizer skill, Google's developer
documentation style, and Zinsser's principles. The output still needed hand edits. This skill
puts those sources together with two others that matter more:

- **Recent research on how AI prose differs from human prose.** The most useful finding:
  people who use chatbots a lot spot machine text almost perfectly, and they judge the whole
  piece (no point of view, nothing specific, uniform smoothness) rather than single words.
  So the skill fixes the thinking first and the wording second. Sources are in
  [`references/ai-tells.md`](skills/technical-writer/references/ai-tells.md). It also covers
  the phrases current models overuse, from Graphite's October 2026 study: "this matters",
  "why X matters" and "looking ahead". Em dashes are no longer the main sign.
- **My own voice and the edits I keep making by hand,** taken from revisions I asked for on
  AI drafts. See [`references/voice.md`](skills/technical-writer/references/voice.md). Where
  my samples don't cover a kind of piece, such as news reports, READMEs and release notes,
  the skill follows writers who do it well. They are listed in
  [`references/craft.md`](skills/technical-writer/references/craft.md).

I disclose AI involvement on everything I publish, so the skill isn't trying to fool anyone.
It adds a one-line disclosure and still holds the prose to a human standard.

It also ships a linter for the mechanical tells (contrast framing, narrated significance,
trailing "-ing" clauses, em dashes, AI vocabulary, uniform sentence length and more). It needs
only the Python standard library:

```sh
python skills/technical-writer/scripts/tells.py draft.md
cat draft.md | python skills/technical-writer/scripts/tells.py -
python skills/technical-writer/scripts/tells.py --json draft.md
```

A clean run is necessary, not sufficient. The tells that matter most are invisible to a regex.

## Install

macOS / Linux:

```sh
git clone https://github.com/AbhiramDwivedi/ai-tools.git
cd ai-tools && ./install.sh          # symlinks; add --copy to copy instead
```

Windows (PowerShell):

```powershell
git clone https://github.com/AbhiramDwivedi/ai-tools.git
cd ai-tools; .\install.ps1           # directory junctions; add -Copy to copy instead
```

Both scripts install into `~/.claude/skills/` and `~/.codex/skills/` (or `$CODEX_HOME/skills`).
With links, a `git pull` updates the installed skill.

## Use

- Claude Code: `/technical-writer`, or ask it to write or edit a post; the skill loads by
  description.
- Codex: `$technical-writer` or mention the skill by name, or let it trigger by description.
- Any other agent: point it at `skills/technical-writer/SKILL.md` and tell it to follow it.

The voice profile is mine. To use the skill for your own writing, replace
`references/voice.md` with your own: your registers, a few samples, and the edits you keep
making to AI drafts. The rest of the skill is general.

## License

MIT for the code and the skill text. The short quotations in `references/voice.md` belong to
their authors and are quoted for illustration.

*This repository was drafted with AI assistance and reviewed by its author.*
