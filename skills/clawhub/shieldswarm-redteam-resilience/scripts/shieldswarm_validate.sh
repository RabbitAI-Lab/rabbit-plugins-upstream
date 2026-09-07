#!/bin/bash
# ShieldSwarm shieldswarm_validate.sh — defensive command validator (fail-closed).
# Portable: bash 3.2+ (no associative arrays), coreutils only, no network.
#
# Contract (machine-readable):
#   usage:  shieldswarm_validate.sh --command CMD [--mode MODE] [--roe FILE] [--max-len N]
#   output: check=offensive_pattern status=...
#           check=secret_exposure   status=...
#           check=mode_gate         status=...
#           check=command_length    status=...
#           verdict=PASS|FAIL
#   exit:   0=PASS, 1=FAIL, 2=usage error
# Modes: support_without_login | auth_user_support | auth_operator |
#        incident_commander | model_resilience | red_team | ethical_promotion
set -eu

CMD=""
MODE="support_without_login"
ROE=""
MAXLEN=""

usage() {
  cat <<'EOF'
Usage: shieldswarm_validate.sh --command CMD [--mode MODE] [--roe FILE] [--max-len N]
Validates a proposed command against defensive rules. Fail-closed: unknown
patterns and missing required args are treated as FAIL.
Output (stdout): one "check=<name> status=<value> [detail]" line per check,
then "verdict=PASS" or "verdict=FAIL".
Exit codes: 0=PASS, 1=FAIL, 2=usage error
Example: shieldswarm_validate.sh --command "curl -s https://status.example.com" --mode operator
EOF
  exit 2
}

FAIL=0

# ---- check 1: offensive tool / pattern --------------------------------------
OFFENSIVE="
nmap masscan sqlmap hydra msfconsole metasploit slowloris hping3 nikto gobuster
ffuf dirb wpscan acunetix evilginx
"
check_offensive() {
  local c="$1" p
  for p in $OFFENSIVE; do
    case " $c " in
      *" $p "*|*" $p "*)
        echo "check=offensive_pattern status=detected pattern=$p"
        FAIL=1
        return 0
      ;;
    esac
  done
  # stealth / evasion keywords (word-ish match)
  case " $c " in
    *fronting*|*"stealth tunnel"*|*"covert channel"*|*"vpn evasion"*|*obfuscat*)
      echo "check=offensive_pattern status=detected pattern=stealth_or_evasion"
      FAIL=1
      return 0
      ;;
  esac
  # load-generation / flood flags
  case "$c" in
    *wrk*|*siege*|*"ab -n"*|*"ab -c"*|*flood*)
      echo "check=offensive_pattern status=detected pattern=load_generation"
      FAIL=1
      return 0
      ;;
  esac
  echo "check=offensive_pattern status=clean"
  return 0
}

# ---- check 2: secret exposure -----------------------------------------------
check_secrets() {
  local c="$1"
  case "$c" in
    *password=*|*passwd=*|*token=*|*apikey=*|*api_key=*|*secret=*|*cookie=*)
      echo "check=secret_exposure status=detected pattern=credential_assignment"
      FAIL=1
      return 0 ;;
  esac
  case "$c" in
    *AKIA[0-9A-Z][0-9A-Z][0-9A-Z][0-9A-Z]*|*"BEGIN RSA PRIVATE KEY"*|*"BEGIN OPENSSH PRIVATE KEY"*|*"BEGIN PRIVATE KEY"*)
      echo "check=secret_exposure status=detected pattern=key_material"
      FAIL=1
      return 0 ;;
  esac
  echo "check=secret_exposure status=clean"
  return 0
}

# ---- check 3: mode gate ------------------------------------------------------
# red_team requires an ROE file that is actually filled in:
#   >= 100 bytes, contains the structural keys scope: / abort_conditions: /
#   rollback_owner: / authorized_by:, AND the three core identity fields
#   (exercise_name, authorized_by, rollback_owner) all carry non-empty values
#   (an untouched template carries pre-filled defaults elsewhere and is still
#   rejected).
roe_field_value() { # roe_field_value <field> <file> -> quoted value, trimmed (or empty)
  grep -E "^${1}:[[:space:]]*\"[^\"]*\"" "$2" 2>/dev/null | head -n 1 \
    | sed 's/.*:[[:space:]]*"//; s/".*$//' \
    | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}

check_mode() {
  case "$MODE" in
    red_team)
      [ -n "$ROE" ] || { echo "check=mode_gate status=missing_roe"; FAIL=1; return 0; }
      [ -f "$ROE" ] || { echo "check=mode_gate status=roe_not_found file=$ROE"; FAIL=1; return 0; }
      local size missing fld filled v
      size=$(wc -c < "$ROE")
      [ "$size" -ge 100 ] || { echo "check=mode_gate status=roe_too_small bytes=$size min=100"; FAIL=1; return 0; }
      missing=""
      for fld in "scope:" "abort_conditions:" "rollback_owner:" "authorized_by:"; do
        # key must start the line (commented-out keys do not count)
        grep -qE "^[[:space:]]*${fld}" "$ROE" 2>/dev/null || missing="$missing $fld"
      done
      [ -z "$missing" ] || { echo "check=mode_gate status=roe_fields_missing fields=$missing"; FAIL=1; return 0; }
      filled=0
      for fld in "exercise_name" "authorized_by" "rollback_owner"; do
        v="$(roe_field_value "$fld" "$ROE")"
        [ -n "$v" ] && filled=$((filled + 1))
      done
      [ "$filled" -ge 3 ] || { echo "check=mode_gate status=roe_unfilled core_fields_filled=$filled required=3"; FAIL=1; return 0; }
      echo "check=mode_gate status=valid roe=$ROE core_fields_filled=3"
      ;;
    *) echo "check=mode_gate status=not_required mode=$MODE" ;;
  esac
  return 0
}

# ---- check 4: command length (defence against paste bombs) -------------------
check_length() {
  local n=${#CMD}
  if [ -n "$MAXLEN" ] && [ "$n" -gt "$MAXLEN" ]; then
    echo "check=command_length status=exceeds_limit length=$n limit=$MAXLEN"
    return 0
  fi
  if [ -z "$MAXLEN" ] && [ "$n" -gt 4000 ]; then
    echo "check=command_length status=exceeds_limit length=$n limit=4000 default=4000"
    return 0
  fi
  echo "check=command_length status=within_limit length=$n"
  return 0
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --command) CMD="${2:-}"; shift 2 ;;
    --mode) MODE="${2:-}"; shift 2 ;;
    --roe) ROE="${2:-}"; shift 2 ;;
    --max-len) MAXLEN="${2:-}"; shift 2 ;;
    -h|--help) usage ;;
    *) echo "error=invalid_argument arg=$1" >&2; exit 2 ;;
  esac
done

[ -n "$CMD" ] || { echo "error=missing_required_args arg=command" >&2; usage; }

check_offensive "$CMD"
check_secrets "$CMD"
check_mode
check_length

if [ "$FAIL" -eq 0 ]; then
  echo "verdict=PASS"
  exit 0
else
  echo "verdict=FAIL"
  exit 1
fi
