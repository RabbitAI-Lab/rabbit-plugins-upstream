#!/usr/bin/env bash
set -euo pipefail

# Lightweight post-write sanity check for signal-dreaming runs.
# Usage: references/dream-audit.sh <workspace-root> [touched-file ...]
# Prints filenames only for suspected secrets; never echoes matched values.
# This is NOT full DLP or exhaustive secret detection.
#
# Exit code is advisory-free: index size never fails. Only a missing
# MEMORY.md/dream-log.md or a suspected credential exits non-zero. Never gate a
# consolidation run on this script's exit code.
#
# The index budget is derived from OpenClaw's own caps, not hard-coded here:
#   headroom = min(bootstrapMaxChars, bootstrapTotalMaxChars - other boot files)
#   target   = headroom * SD_INDEX_TARGET_PCT / 100        (default 80)
# Override the caps with SD_BOOTSTRAP_MAX_CHARS / SD_BOOTSTRAP_TOTAL_MAX_CHARS
# when the workspace configures different values. The 20% default margin is
# growth slack between runs, not a stricter limit.

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <workspace-root> [touched-file ...]" >&2
  exit 2
fi

ROOT="$1"
shift || true

if [[ ! -d "$ROOT" ]]; then
  echo "ERROR: workspace root does not exist: $ROOT" >&2
  exit 2
fi

PER_CAP="${SD_BOOTSTRAP_MAX_CHARS:-20000}"
TOTAL_CAP="${SD_BOOTSTRAP_TOTAL_MAX_CHARS:-60000}"
TARGET_PCT="${SD_INDEX_TARGET_PCT:-80}"
MEMORY="$ROOT/MEMORY.md"
DREAM_LOG="$ROOT/memory/dream-log.md"
status=0

# Character count. Returns non-zero when no usable UTF-8 locale is available.
# A count equal to the byte count is only trustworthy for pure-ASCII files;
# otherwise it means the locale did not take effect and wc -m fell back to
# counting bytes, which is exactly the error this whole check exists to avoid.
count_chars() {
  local f="$1" b c nonascii
  b=$(wc -c < "$f" 2>/dev/null | tr -d ' ') || return 1
  nonascii=$(LC_ALL=C tr -d '\000-\177' < "$f" 2>/dev/null | wc -c | tr -d ' ')
  for loc in en_US.UTF-8 C.UTF-8 en_GB.UTF-8; do
    c=$(LC_ALL="$loc" wc -m < "$f" 2>/dev/null | tr -d ' ') || continue
    [[ -n "$c" ]] || continue
    [[ "$c" -lt "$b" ]] && { printf '%s' "$c"; return 0; }
    if [[ "$c" -eq "$b" && "$nonascii" -eq 0 ]]; then printf '%s' "$c"; return 0; fi
  done
  return 1
}

# Headroom: MEMORY.md shares the total cap with the other bootstrap files.
others=0
for f in AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md BOOTSTRAP.md; do
  [[ -f "$ROOT/$f" ]] || continue
  n=$(count_chars "$ROOT/$f") || n=$(wc -c < "$ROOT/$f" | tr -d ' ')
  others=$((others + n))
done
remaining=$((TOTAL_CAP - others))
HEADROOM=$PER_CAP
[[ "$remaining" -lt "$HEADROOM" ]] && HEADROOM=$remaining
[[ "$HEADROOM" -lt 0 ]] && HEADROOM=0
TARGET=$((HEADROOM * TARGET_PCT / 100))

if [[ ! -f "$MEMORY" ]]; then
  echo "ERROR: missing MEMORY.md" >&2
  status=1
else
  bytes=$(wc -c < "$MEMORY" | tr -d ' ')
  chars=$(count_chars "$MEMORY") || chars=""
  if [[ -n "$chars" ]]; then
    pct=0
    [[ "$HEADROOM" -gt 0 ]] && pct=$((chars * 100 / HEADROOM))
    echo "MEMORY.md chars=$chars bytes=$bytes headroom=$HEADROOM target=$TARGET (${TARGET_PCT}%) used=${pct}%"
    if [[ "$chars" -gt "$HEADROOM" ]]; then
      echo "NOTE: MEMORY.md is past the runtime headroom ($HEADROOM chars); the disk file is intact, only the injected copy is truncated" >&2
    elif [[ "$chars" -gt "$TARGET" ]]; then
      echo "NOTE: MEMORY.md is past the ${TARGET_PCT}% target ($TARGET chars); sink detail into L2 on the next run" >&2
    fi
  else
    echo "MEMORY.md bytes=$bytes (character count unavailable: no UTF-8 locale; do not compare bytes to a character target)"
  fi
fi

if [[ ! -f "$DREAM_LOG" ]]; then
  echo "ERROR: missing memory/dream-log.md" >&2
  status=1
else
  dream_count=$(grep -c '^## 🌙 Dream #' "$DREAM_LOG" || true)
  echo "dream_log_entries=$dream_count"
fi

files=()
if [[ $# -gt 0 ]]; then
  for f in "$@"; do
    if [[ "$f" = /* ]]; then
      files+=("$f")
    else
      files+=("$ROOT/$f")
    fi
  done
else
  files+=("$MEMORY" "$DREAM_LOG")
fi

secret_re='(github_pat_[A-Za-z0-9_]{20,}|ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|[0-9]{8,12}:AA[A-Za-z0-9_-]{30,}|mfa\.[A-Za-z0-9_-]{20,}|[A-Za-z0-9_-]{24}\.[A-Za-z0-9_-]{6}\.[A-Za-z0-9_-]{25,}|xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----|x-access-token:[A-Za-z0-9_-]{20,}@)'

suspects=()
for f in "${files[@]}"; do
  [[ -f "$f" ]] || continue
  if LC_ALL=C grep -Iq . "$f" && LC_ALL=C grep -qE "$secret_re" "$f"; then
    suspects+=("$f")
  fi
done

if [[ ${#suspects[@]} -gt 0 ]]; then
  echo "ERROR: suspected credential pattern in file(s):" >&2
  printf ' - %s\n' "${suspects[@]}" >&2
  status=1
else
  echo "secret_scan=ok"
fi

exit "$status"
