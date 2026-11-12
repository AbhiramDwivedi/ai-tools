# ai-tools

Skills and small tools I use with AI coding agents. Each skill is a folder with a `SKILL.md`,
which both Claude Code and Codex read, so one copy serves both.

## Skills

### technical-writer

Drafts, revises and reviews technical prose (blog posts, reference docs, newspaper pieces,
READMEs) so it reads like a sharp engineer wrote it.

I used to ask for three things on every piece: the humanizer skill, Google's developer
documentation style, and Zinsser's principles. The output still needed hand edits, so this
skill adds two sources to those three: research on how AI prose differs from human prose, and
a voice built from the edits AI drafts keep needing.

The most useful research finding is that people who use chatbots a lot spot machine text
almost perfectly, and they judge the whole piece (no point of view, nothing specific, uniform
smoothness) rather than single words. So the skill fixes the thinking first and the wording
second. The sources are in
[`references/ai-tells.md`](skills/technical-writer/references/ai-tells.md), along with the
phrases current models overuse from Graphite's October 2026 study, such as "this matters",
"why X matters" and "looking ahead". Those phrases have replaced the em dash as the commonest
sign of a model.

The default voice is in [`references/voice.md`](skills/technical-writer/references/voice.md),
with before/after edits taken from revisions of real AI drafts. You can give the skill your
own voice instead (see below). For kinds of piece the voice doesn't cover, such as news
reports, READMEs and release notes, the skill copies writers who do them well. They are listed
in [`references/craft.md`](skills/technical-writer/references/craft.md).

The skill isn't meant to fool anyone. It adds a one-line AI disclosure when your voice
profile, you or the publication ask for one, and offers one otherwise. Either way, the prose
has to pass the same checks.

It also ships a linter for the mechanical tells (contrast framing, narrated significance,
trailing "-ing" clauses, em dashes, AI vocabulary, uniform sentence length and more). It needs
only the Python standard library:

```sh
python skills/technical-writer/scripts/tells.py draft.md
cat draft.md | python skills/technical-writer/scripts/tells.py -
python skills/technical-writer/scripts/tells.py --json draft.md
```

A clean run doesn't make a draft good, because the linter can't see a missing point of view,
structural sameness or invented facts. The skill's revision passes cover those.

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

### Make it sound like you

The skill works out of the box with its default voice. To make it write like you, put a
personal profile at `~/.config/technical-writer/voice.md` (on Windows,
`%USERPROFILE%\.config\technical-writer\voice.md`). Start from the outline in
[`references/voice-template.md`](skills/technical-writer/references/voice-template.md): your
registers, a few samples, the edits you keep making to AI drafts, and whether you disclose
AI help. The profile lives outside the repo, so `git pull` and reinstalling never touch it.
Where it says nothing, the default voice applies.

## License

MIT for the code and the skill text. The short quotations in `references/voice.md` belong to
their authors and are quoted for illustration.

*This repository was drafted with AI assistance and reviewed by its author.*
