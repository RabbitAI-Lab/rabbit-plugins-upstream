#!/usr/bin/env bash
# sith-choir offline self-test — sandboxed: throwaway HOME, fixture creds,
# zero network, zero real user state (publishing-standard C4 rule).
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SBX=$(mktemp -d)
trap 'rm -rf "$SBX"' EXIT
mkdir -p "$SBX/home"
HOME="$SBX/home" python3 "$HERE/choir.py" --state "$SBX/home/.cache/sith-choir" selftest
echo "sith-choir selftest: OK (sandboxed, no network)"
