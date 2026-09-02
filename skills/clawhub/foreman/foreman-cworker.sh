#!/bin/bash
# foreman caged worker: bash foreman-cworker.sh <absolute-worktree-path> <prompt-file> [model]
#
# Blast radius = the mounted worktree + the container filesystem. The host $HOME, your
# other repos, and your primary agent login are all invisible to it, which is what makes
# --dangerously-skip-permissions acceptable here and nowhere else.
#
# Credential boundary — what happens to DEEPSEEK_API_KEY:
#   * Read from your environment at call time. This script never writes it to disk,
#     never logs it, and never bakes it into an image.
#   * Handed to the container as that worker's own API credential, so it is exposed
#     only to the process running inside the cage. This script never copies it into
#     the mounted worktree, and it is gone when the container exits (--rm).
#   * It authenticates against exactly one endpoint — the ANTHROPIC_BASE_URL set below.
#     Change that line to point at a different backend.
#   * The key never travels back out. The only thing that leaves this container is
#     whatever the worker writes into the mounted worktree.
set -euo pipefail
WT="$1"; PROMPT_FILE="$2"; MODEL="${3:-deepseek-v4-flash}"
[ -d "$WT" ] || { echo "worktree does not exist: $WT" >&2; exit 1; }
[ -n "${DEEPSEEK_API_KEY:-}" ] || { echo "DEEPSEEK_API_KEY is not set" >&2; exit 1; }
exec docker run --rm \
  --memory 4g --cpus 2 --pids-limit 512 \
  -v "$WT":/work \
  -v "$PROMPT_FILE":/prompt.md:ro \
  -e ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic \
  -e ANTHROPIC_AUTH_TOKEN="$DEEPSEEK_API_KEY" \
  -e ANTHROPIC_MODEL="$MODEL" \
  foreman-worker:latest \
  -p "$(cat "$PROMPT_FILE")" --dangerously-skip-permissions --output-format text
