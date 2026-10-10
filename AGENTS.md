# AGENTS.md

Guidance for agents (Claude Code, Codex and others) working in this repo.

- Each skill lives in `skills/<name>/` with a `SKILL.md` (YAML frontmatter with `name` and
  `description` only, so both Claude Code and Codex accept it), plus optional `references/`
  and `scripts/`. Keep frontmatter to those two keys.
- `SKILL.md` is the product. Edit it like an instruction document. Keep it under ~250 lines
  and move detail into `references/`.
- Scripts use the Python standard library only and must run on Windows, macOS and Linux.
  Read and write files as UTF-8 explicitly.
- Prose in this repo follows the technical-writer skill. Run
  `python skills/technical-writer/scripts/tells.py <file>` on any Markdown you change.
- Never put em dashes in the author's prose. Never invent sources; mark unverified ones.
- When you change `scripts/tells.py`, re-run it on `skills/technical-writer/tests/sample-ai.md`
  and `tests/sample-human.md` and check the AI sample still lights up and the human one stays
  quiet.
