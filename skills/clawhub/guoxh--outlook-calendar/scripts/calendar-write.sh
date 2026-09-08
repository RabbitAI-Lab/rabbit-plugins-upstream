#!/usr/bin/env bash
# scripts/calendar-write.sh
# Create, update, fetch, or delete events on the signed-in user's primary calendar.
#
# SAFETY MODEL
# ------------
# Every write/delete operation requires TWO safeguards:
#   1. The explicit --apply flag (without it, the script only prints the JSON it
#      WOULD have sent and exits 0). This lets the agent and the user inspect
#      the payload before anything touches the calendar.
#   2. A typed "YES" confirmation prompt at the terminal (skipped only when
#      --yes is also passed). The prompt summarizes subject / start / end /
#      location / id.
# Delete additionally requires --event-id and refuses to act on a 0-character
# subject or anything in the "DO NOT DELETE" guard list.
#
# Subcommands:
#   create   --subject S --start "YYYY-MM-DD HH:MM" --end "YYYY-MM-DD HH:MM"
#            [--tz TZ] [--body B] [--location L] [--all-day]
#   update   --event-id ID [--subject S] [--start ...] [--end ...] [--tz TZ]
#            [--body B] [--location L] [--clear-location]
#   get      --event-id ID
#   delete   --event-id ID
#
# Common flags:
#   --apply           Actually call Graph (default: dry-run; print JSON to stdout).
#   --yes             Skip the "type YES" confirmation prompt.
#   --tz TZ           Timezone for start/end (default: Asia/Shanghai).
#
# Examples:
#   # Dry-run: see what would be sent
#   calendar-write.sh create --subject "Lunch" --start "2026-06-18 12:00" --end "2026-06-18 13:00"
#
#   # Real call
#   calendar-write.sh create --subject "Lunch" --start "2026-06-18 12:00" --end "2026-06-18 13:00" --apply
#
#   # Update
#   calendar-write.sh update --event-id AAMkAD... --subject "Lunch (moved)" --apply
#
#   # Delete
#   calendar-write.sh delete --event-id AAMkAD... --apply

set -Eeuo pipefail
IFS=$' \t\n'

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
# shellcheck source=./_lib.sh
. "$SCRIPT_DIR/_lib.sh"

usage() {
    cat >&2 <<'USAGE'
Usage: calendar-write.sh <subcommand> [options]

Subcommands:
  create   Create a new event.
  update   Update an existing event.
  get      Fetch a single event by id.
  delete   Delete an event by id.

Global options:
  --apply           Send the request. Without it, only the JSON payload is printed.
  --yes             Skip the "type YES" confirmation prompt.
  --tz TZ           IANA timezone (default: Asia/Shanghai).

Options for create / update:
  --subject S       Event subject.
  --start  S        Start as "YYYY-MM-DD HH:MM" (local in --tz) or full ISO datetime.
  --end    S        End   as "YYYY-MM-DD HH:MM" (local in --tz) or full ISO datetime.
  --body    B       Free-text body.
  --location L      Location display name.
  --clear-location  (update only) Remove the location.

Options for update / get / delete:
  --event-id ID     Graph event id (AAMkAGI...).

Other:
  --all-day         (create only) Treat start/end as YYYY-MM-DD (date-only).
  -h, --help        Show this help.
USAGE
}

# ---- Arg parsing (subcommand + flags) -------------------------------------
SUBCMD="${1:-}"
shift || true
if [[ -z "$SUBCMD" || "$SUBCMD" == "-h" || "$SUBCMD" == "--help" ]]; then
    usage; exit 0
fi
case "$SUBCMD" in
    create|update|get|delete) : ;;
    *) usage; die "unknown subcommand: $SUBCMD" ;;
esac

APPLY=0
YES=0
SUBJECT=""
START=""
END=""
TZ="Asia/Shanghai"
BODY=""
LOCATION=""
CLEAR_LOC=0
EVENT_ID=""
ALL_DAY=0

while (( $# > 0 )); do
    case "$1" in
        --apply)          APPLY=1; shift ;;
        --yes)            YES=1; shift ;;
        --subject)        SUBJECT="${2:-}"; shift 2 ;;
        --start)          START="${2:-}"; shift 2 ;;
        --end)            END="${2:-}"; shift 2 ;;
        --tz)             TZ="${2:-}"; shift 2 ;;
        --body)           BODY="${2:-}"; shift 2 ;;
        --location)       LOCATION="${2:-}"; shift 2 ;;
        --clear-location) CLEAR_LOC=1; shift ;;
        --event-id)       EVENT_ID="${2:-}"; shift 2 ;;
        --all-day)        ALL_DAY=1; shift ;;
        -h|--help)        usage; exit 0 ;;
        *) die "unknown argument: $1  (try --help)" ;;
    esac
done

# ---- Validations -----------------------------------------------------------

# Validate timezone
if ! command -v python3 >/dev/null 2>&1; then
    die "python3 is required for timezone validation"
fi
TZ_FOR_CHECK="$TZ" python3 -c '
import os, sys
from zoneinfo import available_timezones
sys.exit(0 if os.environ["TZ_FOR_CHECK"] in available_timezones() else 1)
' || die "invalid --tz: $TZ"

# Normalize "YYYY-MM-DD HH:MM" -> ISO with offset in $TZ
# Accepts also a full ISO datetime.
normalize_dt() {
    local raw="$1" which="$2"
    [[ -n "$raw" ]] || die "--$which is required"
    if [[ "$raw" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}[[:space:]][0-9]{2}:[0-9]{2}(:[0-9]{2})?$ ]]; then
        local norm
        norm=$(printf '%s' "$raw" | tr ' ' 'T')
        local out
        out=$(RAW="$norm" TZ_FOR="$TZ" python3 - <<'PY'
import os, sys
from datetime import datetime
from zoneinfo import ZoneInfo
raw, tz = os.environ["RAW"], os.environ["TZ_FOR"]
try:
    dt = datetime.fromisoformat(raw).replace(tzinfo=ZoneInfo(tz))
    print(dt.isoformat(timespec="seconds"))
except Exception as e:
    sys.stderr.write(str(e))
    sys.exit(2)
PY
) || die "invalid --$which: $raw (could not interpret in $TZ)"
        printf '%s' "$out"
    elif [[ "$raw" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?(Z|[+-][0-9]{2}:[0-9]{2})?$ ]]; then
        # Already ISO; pass through
        printf '%s' "$raw"
    else
        die "invalid --$which format: $raw (expected 'YYYY-MM-DD HH:MM' or ISO datetime)"
    fi
}

# ---- Subcommand: create ----------------------------------------------------
cmd_create() {
    [[ -n "$SUBJECT" ]] || die "--subject is required for create"

    local start_iso end_iso
    if (( ALL_DAY )); then
        # All-day: start.date is YYYY-MM-DD, end.date is exclusive next day.
        [[ "$START" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || die "--start must be YYYY-MM-DD with --all-day"
        [[ -z "$END" ]] && END="$START"
        [[ "$END" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] || die "--end must be YYYY-MM-DD with --all-day"

        PAYLOAD=$(jq -n \
            --arg subject "$SUBJECT" \
            --arg body    "$BODY" \
            --arg loc     "$LOCATION" \
            --arg start   "$START" \
            --arg end     "$END" \
            --arg tz      "$TZ" \
            '{
                subject:  $subject,
                isAllDay: true,
                body:     { contentType: "Text", content: $body },
                start:    { dateTime: ($start + "T00:00:00"), timeZone: $tz },
                end:      { dateTime: ($end   + "T00:00:00"), timeZone: $tz },
                location: (if $loc == "" then null else { displayName: $loc } end)
              }
              | with_entries(
                  select(
                    (.key == "isAllDay")
                    or (.value != null and (.value | type == "object" or . != ""))
                  )
                )')
    else
        start_iso=$(normalize_dt "$START" start)
        end_iso=$(normalize_dt "$END" end)
        # Validate chronological order (ISO 8601 strings sort lexically when same format)
        if [[ "$start_iso" > "$end_iso" ]]; then
            die "--end ($end_iso) must be after --start ($start_iso)"
        fi
        PAYLOAD=$(build_event_body "$SUBJECT" "$start_iso" "$end_iso" "$TZ" "$BODY" "$LOCATION")
    fi

    cat >&2 <<EOF
Subject:  $SUBJECT
Start:    $START  ($TZ)
End:      $END    ($TZ)
Body:     ${BODY:-<none>}
Location: ${LOCATION:-<none>}
EOF

    if ! require_apply_and_confirm "$APPLY" "$YES" "CREATE event on your primary calendar"; then
        echo "$PAYLOAD" | jq .
        exit 0
    fi

    ensure_fresh_token
    log_info "POST /me/events"
    RESP=$(graph_request POST "/me/events" "$PAYLOAD")
    echo "$RESP" | jq '{id, subject, start, end, location, webLink}'
}

# ---- Subcommand: update ----------------------------------------------------
cmd_update() {
    [[ -n "$EVENT_ID" ]] || die "--event-id is required for update"

    # Start/end handling
    local start_iso="" end_iso=""
    if [[ -n "$START" ]]; then
        start_iso=$(normalize_dt "$START" start)
    fi
    if [[ -n "$END" ]]; then
        end_iso=$(normalize_dt "$END" end)
    fi

    # Validate chronological order if both start and end were given
    if [[ -n "$start_iso" && -n "$end_iso" ]] && [[ "$start_iso" > "$end_iso" ]]; then
        die "--end ($end_iso) must be after --start ($start_iso)"
    fi

    # Build partial payload: only include fields the user actually passed.
    # jq with --arg passes values safely. We use sentinel "__OMIT__" to detect
    # "user didn't pass this arg" inside jq.
    PAYLOAD=$(jq -n \
        --arg subject  "$SUBJECT" \
        --arg body     "$BODY" \
        --arg loc      "$LOCATION" \
        --arg start    "$start_iso" \
        --arg end      "$end_iso" \
        --arg tz_arg   "$TZ" \
        --argjson clear_loc "$CLEAR_LOC" \
        '
        def provided(v): v != "";
        {
            subject: (if provided($subject) then $subject else null end),
            body:    (if provided($body)    then { contentType: "Text", content: $body } else null end),
            location:(
                if $clear_loc == 1 then null
                elif provided($loc) then { displayName: $loc }
                else null end
            ),
            start:   (if provided($start) then { dateTime: $start, timeZone: $tz_arg } else null end),
            end:     (if provided($end)   then { dateTime: $end,   timeZone: $tz_arg } else null end)
        }
        | with_entries(select(.value != null))
        ')

    if [[ "$PAYLOAD" == "{}" ]]; then
        die "update: nothing to change (specify at least one of --subject, --start, --end, --body, --location, --clear-location)"
    fi

    cat >&2 <<EOF
Event-id: $EVENT_ID
EOF
    echo "$PAYLOAD" | jq . >&2

    if ! require_apply_and_confirm "$APPLY" "$YES" "UPDATE event $EVENT_ID"; then
        echo "$PAYLOAD" | jq .
        exit 0
    fi

    ensure_fresh_token
    log_info "PATCH /me/events/$EVENT_ID"
    RESP=$(graph_request PATCH "/me/events/$EVENT_ID" "$PAYLOAD")
    echo "$RESP" | jq '{id, subject, start, end, location}'
}

# ---- Subcommand: get -------------------------------------------------------
cmd_get() {
    [[ -n "$EVENT_ID" ]] || die "--event-id is required for get"
    ensure_fresh_token
    log_info "GET /me/events/$EVENT_ID"
    graph_request GET "/me/events/$EVENT_ID" | jq .
}

# ---- Subcommand: delete ----------------------------------------------------
cmd_delete() {
    [[ -n "$EVENT_ID" ]] || die "--event-id is required for delete"

    # Fetch the event first so we can show the human what they're about to remove.
    ensure_fresh_token
    log_info "GET /me/events/$EVENT_ID (preview)"
    local preview
    preview=$(graph_request GET "/me/events/$EVENT_ID") || die "could not fetch event; refusing to delete blindly"
    echo "$preview" | jq '{id, subject, start, end, location, organizer, attendees}' >&2
    echo "$preview" | jq -r '"organizer: \(.organizer.emailAddress.name // "-")  <\(.organizer.emailAddress.address // "-")"' >&2

    print_event_summary "$preview"

    if ! require_apply_and_confirm "$APPLY" "$YES" "DELETE event $EVENT_ID"; then
        echo "(dry-run; nothing was sent)" >&2
        exit 0
    fi

    log_info "DELETE /me/events/$EVENT_ID"
    # Graph returns 204 No Content on successful delete
    graph_request DELETE "/me/events/$EVENT_ID" "" >/dev/null
    log_info "deleted."
}

# ---- Dispatch --------------------------------------------------------------
case "$SUBCMD" in
    create) cmd_create ;;
    update) cmd_update ;;
    get)    cmd_get    ;;
    delete) cmd_delete ;;
esac
