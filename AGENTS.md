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
- Keep the skill generic: nothing in `skills/` may name or assume a particular writer.
  Personal voice belongs in the user's `~/.config/technical-writer/voice.md`.
- Never put em dashes in this repo's prose. Never invent sources; mark unverified ones.
- When you change `scripts/tells.py`, re-run it on `skills/technical-writer/tests/sample-ai.md`
  and `tests/sample-human.md` and check the AI sample still lights up and the human one stays
  quiet.
- When testing the skill end to end, use a draft that `references/voice.md` doesn't quote;
  the anti-samples there come from real drafts and would leak the answer.
- Known gaps in `tells.py`: it can't see structural sameness, missing point of view, or
  invented specifics. Those are the skill's job, not the linter's.
  By design it also skips short double-quoted phrases (a mention of a tell, not a use) and
  the italic AI-disclosure line, so a tell inside quoted dialogue goes unflagged.
- Model-specific tells move with each model release. When adding a new list, cite the study
  and its caveats in `references/ai-tells.md`, as the Graphite section does.
