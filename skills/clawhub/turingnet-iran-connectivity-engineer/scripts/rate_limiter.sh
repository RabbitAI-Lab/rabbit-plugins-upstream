#!/usr/bin/env bash
# rate_limiter.sh — official public status-page budget: max 3 GET/HEAD per 10 min.
# 'check' makes NO network call. 'get URL' performs ONE bounded request
# (HEAD preferred, fallback GET, 10s timeout, no redirect following across hosts).
# State: ${TURINGNET_STATE:-$HOME/.cache/turingnet}/rate.json (append-safe).
set -u
STATE_DIR="${TURINGNET_STATE:-$HOME/.cache/turingnet}"
STATE="$STATE_DIR/rate.json"
MAX=3
WINDOW=600  # seconds

mkdir -p "$STATE_DIR" 2>/dev/null || true

now() { date +%s; }
ts_list() {  # print valid timestamps from state
  python3 - "$STATE" <<'PY' 2>/dev/null
import json, sys, time
try:
    d = json.load(open(sys.argv[1]))
except Exception:
    d = []
cut = time.time() - 600
print("\n".join(str(int(t)) for t in d if t >= cut))
PY
}

write_ts() {  # write_ts <epoch>
  python3 - "$STATE" "$1" <<'PY' 2>/dev/null
import json, os, sys, tempfile
path, now = sys.argv[1], int(sys.argv[2])
try:
    d = json.load(open(path))
except Exception:
    d = []
d = [t for t in d if t >= now - 600] + [now]
fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path) or ".")
with os.fdopen(fd, "w") as f:
    json.dump(sorted(d), f)
os.replace(tmp, path)
PY
}

case "${1:-}" in
  check)
    USED=$(ts_list | grep -c . || true)
    echo "status-page budget: $((MAX - USED))/$MAX remaining in this 10-minute window"
    [ "$((MAX - USED))" -gt 0 ] && exit 0 || exit 1
    ;;
  allow)
    HOST="${2:-}"
    case "$HOST" in
      *.example|*.local|localhost) echo "refusing placeholder/internal host" >&2; exit 2 ;;
    esac
    [ -n "$HOST" ] || { echo "usage: rate_limiter.sh allow <status.host>" >&2; exit 2; }
    mkdir -p "$STATE_DIR"
    echo "$HOST" >> "$STATE_DIR/allowed_hosts.txt"
    sort -u "$STATE_DIR/allowed_hosts.txt" -o "$STATE_DIR/allowed_hosts.txt"
    echo "allowlisted status host: $HOST"
    exit 0
    ;;
  get)
    URL="${2:-}"
    USED=$(ts_list | grep -c . || true)
    if [ "$USED" -ge "$MAX" ]; then
      echo "refusing: status-page budget exhausted ($MAX per 10 min)" >&2
      exit 1
    fi
    case "$URL" in
      https://*) : ;;
      *) echo "refusing: only https:// URLs" >&2; exit 2 ;;
    esac
    HOST=$(printf '%s' "$URL" | sed -E 's#^https://([^/:]+).*#\1#')
    ALLOW="$STATE_DIR/allowed_hosts.txt"
    if [ ! -f "$ALLOW" ] || ! grep -qxF "$HOST" "$ALLOW"; then
      echo "refusing: host '$HOST' not allowlisted — run: rate_limiter.sh allow $HOST" >&2
      exit 2
    fi
    # one bounded attempt: HEAD first (cheapest), fallback to GET, 10s cap
    if curl -sS -I --max-time 10 "$URL" -o /dev/null 2>/dev/null; then
      write_ts "$(now)"; echo "HEAD $URL ok (budget now $((MAX - USED - 1))/$MAX)"
    elif curl -sS --max-time 10 "$URL" -o /dev/null 2>/dev/null; then
      write_ts "$(now)"; echo "GET $URL ok (budget now $((MAX - USED - 1))/$MAX)"
    else
      write_ts "$(now)"; echo "unreachable in 10s (attempt still counted)" >&2
      exit 3
    fi
    ;;
  *)
    echo "usage: rate_limiter.sh check | allow <host> | get <https://host/path>" >&2
    exit 2
    ;;
esac
