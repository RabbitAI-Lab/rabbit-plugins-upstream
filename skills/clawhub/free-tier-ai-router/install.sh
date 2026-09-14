#!/bin/bash
# install.sh — one-command setup for free-tier-ai-router.
#
#   bash install.sh              # install + wire up
#   bash install.sh <API_KEY>    # ...and register a key in the same step
#
# Works even when the ClawHub registry serves an outdated package: the
# authoritative router is carried in router_fixed.json next to this script,
# and integrate.sh restores it after a checksum check.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
KEY="${1:-}"

echo "🎛️  free-tier-ai-router installer"

if [ ! -f "$HERE/integrate.sh" ]; then
  echo "  ❌ run this from inside the skill directory"; exit 1
fi

bash "$HERE/integrate.sh" || exit $?

if [ -n "$KEY" ]; then
  echo
  python3 "$HERE/router.py" --setup "$KEY" || exit $?
  echo
  echo "  smoke test:"
  python3 "$HERE/router.py" --no-cache "Reply with exactly: OK" | sed 's/^/    /'
fi
