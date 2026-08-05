#!/bin/bash
# test_07 — missing --spec is a usage error.
# --spec is a required argument; omitting it must make argparse exit 2 before
# any git work happens.
source "$(dirname "$0")/test_helpers.sh"

# No --spec at all: argparse bails with exit 2 before any workdir is touched.
# (No temp dir needed, nothing is created.)
"$PY" "$LOOP" >/tmp/acl_t07.log 2>&1
code=$?
[ "$code" -eq 2 ] || die "expected exit 2 (usage error), got $code (see /tmp/acl_t07.log)"

note "missing --spec rejected with usage error (exit 2)"
exit 0
