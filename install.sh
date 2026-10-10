#!/usr/bin/env sh
# Link every skill in ./skills into Claude Code and Codex.
# Usage: ./install.sh            (symlink; edits in this repo go live)
#        ./install.sh --copy     (copy instead)
set -eu
repo=$(cd "$(dirname "$0")" && pwd)
mode=${1:-link}
for target in "$HOME/.claude/skills" "${CODEX_HOME:-$HOME/.codex}/skills"; do
  mkdir -p "$target"
  for skill in "$repo"/skills/*/; do
    name=$(basename "$skill")
    rm -rf "${target:?}/$name"
    if [ "$mode" = "--copy" ]; then cp -R "$skill" "$target/$name"; else ln -s "${skill%/}" "$target/$name"; fi
    echo "installed $name -> $target/$name"
  done
done
