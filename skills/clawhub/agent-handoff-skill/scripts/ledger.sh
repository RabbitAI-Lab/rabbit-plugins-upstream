#!/bin/sh
# Print the relay ledger for one task, oldest hop first.
# The ledger is git history filtered by the Task-Id trailer; there is no
# separate ledger file.
# Usage: ledger.sh <task-id>
set -eu

TASK=${1:?usage: ledger.sh <task-id>}

OUT=$(git log --reverse --grep="Task-Id: $TASK" \
  --format='%ad  hop=%(trailers:key=Hop,valueonly,separator=)  agent=%(trailers:key=Agent,valueonly,separator=)  %s' \
  --date=short)

if [ -z "$OUT" ]; then
  printf 'no commits found for task: %s\n' "$TASK" >&2
  exit 1
fi

printf '%s\n' "$OUT"
