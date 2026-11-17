#!/bin/bash
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/hkw-terminal-tx-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT
export HKW_TRANSACTION_ROOT="$TMP/store"

mkdir -p "$TMP/home/dir"
printf 'before\n' > "$TMP/home/file"
printf 'nested-before\n' > "$TMP/home/dir/nested"
printf '%s\n' "$TMP/home/file" "$TMP/home/dir" "$TMP/home/new" > "$TMP/paths"

TX="$(python3 "$ROOT/lib/transaction.py" snapshot --label test --paths "$TMP/paths")"
printf 'after\n' > "$TMP/home/file"
printf 'nested-after\n' > "$TMP/home/dir/nested"
printf 'created\n' > "$TMP/home/new"
python3 "$ROOT/lib/transaction.py" rollback "$TX" >/dev/null

[ "$(cat "$TMP/home/file")" = "before" ]
[ "$(cat "$TMP/home/dir/nested")" = "nested-before" ]
[ ! -e "$TMP/home/new" ]

# Discrimination check: corrupting the restored file must make the assertion fail.
printf 'wrong\n' > "$TMP/home/file"
if [ "$(cat "$TMP/home/file")" = "before" ]; then
  echo "transaction test cannot distinguish before from wrong" >&2
  exit 1
fi
printf 'transaction: ok\n'
