#!/usr/bin/env bash
set -euo pipefail

# lg_agent_exec.sh — Agent Skill Gateway execute wrapper.
#
# New (flat) form:
#   lg_agent_exec.sh <skillId> [key=value ...] [key:=jsonvalue ...] [--json '<raw params json>']
#
# Legacy (envelope) form — still fully supported, unchanged:
#   lg_agent_exec.sh '<full request json body>'
#   (single argument, must start with '{' after trimming leading whitespace)
#
# Type convention (httpie-style, LA#6):
#   key=value   -> always a JSON STRING (preserves leading zeros, e.g.
#                  stock_num=000135, day_id=20260419).
#   key:=value  -> value is parsed as raw JSON (number/bool/array/object).
#                  Parse failure is FAIL-LOUD (non-zero exit + clear stderr)
#                  — it never silently falls back to a string.
#
# --json '<obj>' supplies a base params object (e.g. {"body":[...]} for the
# array/nested-body skills: schedule.job.depends.save / .plugins.save /
# process.pipeline.build). Flat key=value / key:=value pairs are placed
# BEFORE the --json object's own members in the assembled JSON text, so on
# standard JSON.parse (which keeps the LAST occurrence of a duplicate key —
# see ECMA-404 / V8 behavior), the explicit --json subtree wins on any name
# collision. This mirrors the "explicit envelope subtree wins over a flat
# key" precedence rule enforced server-side by classifyFlatParams()
# (lib/agent-params.js) — WITHOUT requiring this script to parse arbitrary
# JSON (no jq / python3 dependency, LA#3 — this script must run on any
# third-party agent host).
#
# Arg parsing order (LA#7): --json is intercepted first (wherever it
# appears among the arguments); every other argument is then split at its
# FIRST '=' character (so `--env=dev` and `-start_date=20260419` split
# correctly into key/value), with `:=` detected by checking whether the
# character immediately before that first '=' is ':'.
#
# LG_AGENT_DRY_RUN=1 prints the constructed request JSON body to stdout and
# exits without making the HTTP call — used by the test suite to verify the
# request-shape construction without a live server.

# Default to official domain to avoid security scanner warnings
BASE_URL="${LG_AGENT_BASE_URL:-https://lg-data.cc}"
: "${LG_AGENT_TOKEN:?LG_AGENT_TOKEN is required}"

usage() {
  echo "Usage:" >&2
  echo "  $0 <skillId> [key=value ...] [key:=jsonvalue ...] [--json '<raw params json>']" >&2
  echo "  $0 '<full request json body>'   # legacy single-arg pass-through" >&2
  exit 1
}

# ── json_escape: the single audited JSON-string-escaping function ──────────
# Escapes a value for embedding inside a JSON string literal ("..."). Handles
# double-quote, backslash, newline/CR/tab/backspace/form-feed, and any other
# C0 control character (0x00-0x1F, escaped as \u00XX). Everything else
# (including UTF-8 multi-byte sequences / emoji) passes through byte-for-byte
# unchanged — this is safe regardless of shell locale, because ASCII bytes
# (0x00-0x7F, which is everything this function treats specially) never
# occur as part of a multi-byte UTF-8 continuation/lead byte, so iterating
# byte-wise (as bash does under a non-UTF-8-aware locale) cannot misfire on
# a split multi-byte character.
json_escape() {
  local s="$1"
  local out=""
  local i len c ord esc
  len=${#s}
  for (( i = 0; i < len; i++ )); do
    c="${s:i:1}"
    case "$c" in
      '"') out+='\"' ;;
      '\') out+='\\' ;;
      $'\n') out+='\n' ;;
      $'\r') out+='\r' ;;
      $'\t') out+='\t' ;;
      $'\b') out+='\b' ;;
      $'\f') out+='\f' ;;
      *)
        ord=-1
        printf -v ord '%d' "'$c" 2>/dev/null || ord=-1
        if (( ord >= 0 && ord < 32 )); then
          printf -v esc '\\u%04x' "$ord"
          out+="$esc"
        else
          out+="$c"
        fi
        ;;
    esac
  done
  printf '%s' "$out"
}

# ── _looks_like_json_value: surface-level validation for `key:=value` ──────
# Not a full JSON parser (no jq/python3 dependency, LA#3) — just enough to
# fail loud on an obviously-wrong `:=` usage (e.g. an unquoted bare word)
# instead of silently treating it as a string. The backend's own JSON.parse
# is the final, authoritative validator for deep correctness.
_looks_like_json_value() {
  local v="$1"
  case "$v" in
    true|false|null) return 0 ;;
  esac
  if [[ "$v" =~ ^-?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][+-]?[0-9]+)?$ ]]; then return 0; fi
  if [[ "${v:0:1}" == "[" && "${v: -1}" == "]" ]]; then return 0; fi
  if [[ "${v:0:1}" == "{" && "${v: -1}" == "}" ]]; then return 0; fi
  if [[ ${#v} -ge 2 && "${v:0:1}" == '"' && "${v: -1}" == '"' ]]; then return 0; fi
  return 1
}

_dispatch() {
  local json_body="$1"
  if [[ -n "${LG_AGENT_DRY_RUN:-}" ]]; then
    printf '%s\n' "$json_body"
    return 0
  fi
  curl -sS "${BASE_URL}/agent/skills/execute" \
    -X POST \
    -H "Authorization: Bearer ${LG_AGENT_TOKEN}" \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    --data "${json_body}"
}

if [[ $# -lt 1 ]]; then
  usage
fi

# ── Legacy single-arg pass-through: `lg_agent_exec.sh '<full json>'` ────────
if [[ $# -eq 1 ]]; then
  _trimmed="$(printf '%s' "$1" | sed -e 's/^[[:space:]]*//')"
  if [[ "${_trimmed:0:1}" == "{" ]]; then
    _dispatch "$1"
    exit 0
  fi
fi

SKILL_ID="$1"; shift

JSON_BASE=""   # --json raw object text (validated), optional
declare -a FLAT_STR_KEYS=()
declare -a FLAT_STR_VALS=()
declare -a FLAT_RAW_KEYS=()
declare -a FLAT_RAW_VALS=()

while [[ $# -gt 0 ]]; do
  arg="$1"
  case "$arg" in
    --json)
      shift
      if [[ $# -lt 1 ]]; then
        echo "Error: --json requires a value" >&2
        exit 1
      fi
      _tj="$(printf '%s' "$1" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
      if [[ "${_tj:0:1}" != "{" || "${_tj: -1}" != "}" ]]; then
        echo "Error: --json value must be a JSON object, e.g. --json '{\"body\":[...]}'  (got: ${1})" >&2
        exit 1
      fi
      JSON_BASE="$_tj"
      shift
      continue
      ;;
    *)
      if [[ "$arg" != *=* ]]; then
        echo "Error: invalid argument '$arg' (expected key=value, key:=jsonvalue, or --json '<json>')" >&2
        exit 1
      fi
      key_part="${arg%%=*}"
      val_part="${arg#*=}"
      if [[ "$key_part" == *: ]]; then
        real_key="${key_part%:}"
        if ! _looks_like_json_value "$val_part"; then
          echo "Error: '${real_key}:=${val_part}' is not valid JSON." >&2
          echo "       Use '${real_key}=${val_part}' instead if you meant a plain string." >&2
          exit 1
        fi
        FLAT_RAW_KEYS+=("$real_key")
        FLAT_RAW_VALS+=("$val_part")
      else
        FLAT_STR_KEYS+=("$key_part")
        FLAT_STR_VALS+=("$val_part")
      fi
      shift
      ;;
  esac
done

# ── Build the flat-key portion of the params object text ───────────────────
PARTS=()
for i in "${!FLAT_STR_KEYS[@]}"; do
  k="$(json_escape "${FLAT_STR_KEYS[$i]}")"
  v="$(json_escape "${FLAT_STR_VALS[$i]}")"
  PARTS+=("\"${k}\":\"${v}\"")
done
for i in "${!FLAT_RAW_KEYS[@]}"; do
  k="$(json_escape "${FLAT_RAW_KEYS[$i]}")"
  v="${FLAT_RAW_VALS[$i]}"
  PARTS+=("\"${k}\":${v}")
done

FLAT_JSON=""
if [[ ${#PARTS[@]} -gt 0 ]]; then
  FLAT_JSON="$(IFS=,; echo "${PARTS[*]}")"
fi

# ── Merge with --json base (if any). Flat keys come FIRST so --json's own
# members win on a name collision (JSON.parse last-duplicate-key-wins). ────
if [[ -n "$JSON_BASE" ]]; then
  INNER="${JSON_BASE:1:-1}"   # strip outer { }
  INNER_TRIMMED="$(printf '%s' "$INNER" | sed -e 's/^[[:space:]]*//')"
  if [[ -n "$FLAT_JSON" && -n "$INNER_TRIMMED" ]]; then
    PARAMS_JSON="{${FLAT_JSON},${INNER}}"
  elif [[ -n "$FLAT_JSON" ]]; then
    PARAMS_JSON="{${FLAT_JSON}}"
  else
    PARAMS_JSON="{${INNER}}"
  fi
else
  PARAMS_JSON="{${FLAT_JSON}}"
fi

SKILL_ID_ESCAPED="$(json_escape "$SKILL_ID")"
JSON_BODY="{\"skillId\":\"${SKILL_ID_ESCAPED}\",\"params\":${PARAMS_JSON}}"

_dispatch "$JSON_BODY"
