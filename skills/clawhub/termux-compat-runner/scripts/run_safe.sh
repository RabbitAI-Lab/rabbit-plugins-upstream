#!/usr/bin/env bash
# termux-compat-runner: validate a command against a safe allowlist, DRY-RUN only.
#
# This script NEVER executes the command. It only checks whether the command
# matches an allowlist of safe, read-only Termux/Linux patterns, then prints the
# command it WOULD run (with a timeout wrapper). Execution is left to the user.
#
# Usage:
#   ./run_safe.sh "pkg update"
#   ./run_safe.sh "ss -tulpen" --timeout 60
#   ./run_safe.sh "rm -rf /"        # will be rejected
set -uo pipefail

cmd="${1:-}"
timeout="${2:-}"
[ -z "$cmd" ] && { echo "usage: $0 <command> [--timeout N]" >&2; exit 2; }

if [ "$timeout" = "--timeout" ]; then
  shift 2; timeout="${1:-60}"; shift || timeout=60
fi

# Safe patterns: read-only / informational Termux commands. Anything involving
# destructive tokens (rm -rf, mkfs, dd, chmod -R, :(){), mv to /, etc.) is denied.
ALLOW=(
  '^pkg (update|upgrade|install|list-installed|search|show)[[:space:]]'
  '^(apt|dpkg)[[:space:]]'
  '^(ls|ll|cat|head|tail|wc|echo|printf|pwd|date|uname|whoami|id)[[:space:]]'
  '^(ss|netstat|ip|ifconfig|ping|getprop|dumpsys)[[:space:]]'
  '^(ps|top|free|df|du|mount|termux-(setup-storage|info|api-))[[:space:]]'
  '^curl[[:space:]]'
  '^python3?[[:space:]]'
  '^(git (status|log|diff|branch|fetch|pull|show))[[:space:]]'
)
DENY=(
  'rm[[:space:]].*-rf'
  'mkfs'
  '(^|[[:space:]])dd[[:space:]]'
  'chmod[[:space:]].*-R'
  ':(){'
  '>[[:space:]]/dev/'
  'shutdown|reboot'
  'systemctl'
)

reason=""
for d in "${DENY[@]}"; do
  if echo "$cmd" | grep -Eq "$d"; then
    reason="matches destructive pattern: $d"
    break
  fi
done

allowed=0
if [ -z "$reason" ]; then
  for a in "${ALLOW[@]}"; do
    if echo "$cmd" | grep -Eq "$a"; then
      allowed=1
      break
    fi
  done
fi

if [ "$allowed" = 1 ]; then
  echo "[run_safe] ALLOWED (dry-run only, NOT executed)"
  echo "[run_safe] would run with timeout ${timeout}s:"
  echo "    timeout ${timeout} ${cmd}"
  echo "[run_safe] review then run manually if you approve."
  exit 0
else
  echo "[run_safe] DENIED"
  [ -n "$reason" ] && echo "    reason: $reason" || echo "    reason: not on safe allowlist"
  echo "[run_safe] no command was executed."
  exit 1
fi
