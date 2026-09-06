#!/usr/bin/env bash
# Read events from the signed-in user's primary calendar via /me/calendarView.
set -Eeuo pipefail
IFS=$' \t\n'

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
# shellcheck source=./_lib.sh
. "$SCRIPT_DIR/_lib.sh"

usage() {
    cat >&2 <<'USAGE'
Usage: calendar-read.sh <range> [options]

Range:
  today                Today events.
  tomorrow             Tomorrow events.
  week                 Calendar week (Mon-Sun) containing --from/default today.
  next-days N          Next N days starting at --from/default today (N in 1..90).

Options:
  --from YYYY-MM-DD    Start date (default: today in --tz).
  --tz IANA_TZ         Timezone (default: Asia/Shanghai).
  --top N              Page size / max events per page (default 100; 1..1000).
  --format FMT         json (default) | summary | ids | raw
  --query Q            Graph search query against subject.
  --max-pages P        Max pages to follow (default 5).
  -h, --help           Show this help.
USAGE
}

RANGE=""
TOP=100
MAX_PAGES=5
FORMAT="json"
FROM=""
TZ_NAME="Asia/Shanghai"
QUERY=""
N_DAYS=1

while (( $# > 0 )); do
    case "$1" in
        today) RANGE="today"; shift ;;
        tomorrow) RANGE="tomorrow"; shift ;;
        week) RANGE="week"; shift ;;
        next-days)
            RANGE="next-days"
            ND="${2:-}"
            [[ -n "$ND" ]] || die "next-days requires a number"
            [[ "$ND" =~ ^[0-9]+$ ]] || die "next-days must be an integer 1..90"
            (( ND >= 1 && ND <= 90 )) || die "next-days must be 1..90 (got: $ND)"
            N_DAYS="$ND"
            shift 2
            ;;
        --from) FROM="${2:-}"; shift 2 ;;
        --tz) TZ_NAME="${2:-}"; shift 2 ;;
        --top) TOP="${2:-}"; shift 2 ;;
        --format) FORMAT="${2:-}"; shift 2 ;;
        --query) QUERY="${2:-}"; shift 2 ;;
        --max-pages) MAX_PAGES="${2:-}"; shift 2 ;;
        -h|--help) usage; exit 0 ;;
        *) die "unknown argument: $1 (try --help)" ;;
    esac
done

[[ -n "$RANGE" ]] || { usage; die "range required: today | week | next-days N"; }
case "$FORMAT" in json|summary|ids|raw) : ;; *) die "invalid --format: $FORMAT" ;; esac
[[ "$TOP" =~ ^[0-9]+$ ]] || die "--top must be numeric"
(( TOP >= 1 && TOP <= 1000 )) || die "--top must be 1..1000"
[[ "$MAX_PAGES" =~ ^[0-9]+$ ]] || die "--max-pages must be numeric"
(( MAX_PAGES >= 1 && MAX_PAGES <= 100 )) || die "--max-pages must be 1..100"

command -v python3 >/dev/null 2>&1 || die "python3 is required for timezone-aware date math"
PY_OUT=$(FROM="$FROM" TZ_NAME="$TZ_NAME" RANGE="$RANGE" N_DAYS="$N_DAYS" python3 - <<'PY'
import os, sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

tz_name = os.environ["TZ_NAME"]
try:
    tz = ZoneInfo(tz_name)
except Exception as exc:
    sys.exit(f"invalid --tz: {tz_name}: {exc}")

from_str = os.environ.get("FROM", "").strip()
if from_str:
    try:
        base = datetime.fromisoformat(from_str).replace(tzinfo=tz)
    except ValueError as exc:
        sys.exit(f"invalid --from: {from_str}: {exc}")
else:
    base = datetime.now(tz).replace(hour=0, minute=0, second=0, microsecond=0)

rng = os.environ["RANGE"]
if rng == "today":
    start = base
    end = start + timedelta(days=1) - timedelta(seconds=1)
elif rng == "tomorrow":
    start = base + timedelta(days=1)
    end = start + timedelta(days=1) - timedelta(seconds=1)
elif rng == "week":
    start = base - timedelta(days=base.weekday())
    end = start + timedelta(days=7) - timedelta(seconds=1)
elif rng == "next-days":
    n = int(os.environ["N_DAYS"])
    start = base
    end = start + timedelta(days=n) - timedelta(seconds=1)
else:
    sys.exit(f"unknown range: {rng}")

print(start.isoformat(timespec="seconds"))
print(end.isoformat(timespec="seconds"))
PY
) || die "date computation failed: $PY_OUT"

START_AT=$(printf '%s\n' "$PY_OUT" | sed -n '1p')
END_AT=$(printf '%s\n' "$PY_OUT" | sed -n '2p')
log_info "range=$RANGE tz=$TZ_NAME start=$START_AT end=$END_AT"

load_config || die "config missing; run scripts/setup-device-code.sh first"
ensure_fresh_token

URL=$(jq -rn \
    --arg base "${OUTLOOK_CAL_GRAPH_BASE%/}" \
    --arg start "$START_AT" \
    --arg end "$END_AT" \
    --argjson top "$TOP" \
    --arg query "$QUERY" \
    'def qstr(v): v | @uri;
     ($base + "/me/calendarView?startDateTime=" + qstr($start)
            + "&endDateTime=" + qstr($end)
            + "&$top=" + ($top|tostring)
            + "&$orderby=start/dateTime"
            + "&$select=id,subject,start,end,location,organizer,attendees,isAllDay,showAs,bodyPreview,webLink,responseStatus") as $url
     | if $query != "" then $url + "&$search=" + qstr("subject:\"" + $query + "\"") else $url end')

ALL_EVENTS="[]"
PAGE=0
NEXT_URL="$URL"
while :; do
    PAGE=$((PAGE + 1))
    if (( PAGE > MAX_PAGES )); then
        log_warn "reached --max-pages $MAX_PAGES; some events may be truncated"
        break
    fi
    log_info "fetching page $PAGE..."
    RESP=$(graph_request GET "$NEXT_URL" "" "Prefer: outlook.timezone=\"$TZ_NAME\"")
    VALUES=$(printf '%s' "$RESP" | jq -c '.value // []')
    ALL_EVENTS=$(jq -n -c --argjson a "$ALL_EVENTS" --argjson b "$VALUES" '$a + $b')
    NEXT_LINK=$(printf '%s' "$RESP" | jq -r '."@odata.nextLink" // empty')
    [[ -n "$NEXT_LINK" ]] || break
    NEXT_URL="$NEXT_LINK"
done

COUNT=$(printf '%s' "$ALL_EVENTS" | jq 'length')
log_info "got $COUNT event(s)"

case "$FORMAT" in
    json)
        printf '%s\n' "$ALL_EVENTS" | jq .
        ;;
    ids)
        printf '%s\n' "$ALL_EVENTS" | jq -r '.[]?.id // empty'
        ;;
    summary)
        if [[ "$COUNT" == "0" ]]; then
            echo "No events in range."
        else
            printf '%-36s  %-19s  %-19s  %-20s  %s\n' "ID" "START" "END" "LOCATION" "SUBJECT"
            printf '%-36s  %-19s  %-19s  %-20s  %s\n' "------------------------------------" "-------------------" "-------------------" "--------------------" "-------"
            printf '%s\n' "$ALL_EVENTS" | jq -r '
              .[] | [
                (.id // "-"),
                ((.start.dateTime // "-") | sub("T"; " ") | sub("\\.[0-9]+"; "") | sub("[+-][0-9]{2}:[0-9]{2}$"; "")),
                ((.end.dateTime // "-") | sub("T"; " ") | sub("\\.[0-9]+"; "") | sub("[+-][0-9]{2}:[0-9]{2}$"; "")),
                (.location.displayName // "-"),
                (.subject // "-")
              ] | @tsv
            ' | awk -F'\t' '{ printf "%-36s  %-19s  %-19s  %-20s  %s\n", $1, $2, $3, $4, $5 }'
        fi
        ;;
    raw)
        printf '%s\n' "$ALL_EVENTS"
        ;;
esac
