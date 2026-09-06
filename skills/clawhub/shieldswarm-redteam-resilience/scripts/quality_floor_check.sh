#!/bin/bash
# ShieldSwarm quality_floor_check.sh — model quality-floor gate (cloud-only).
# Portable: bash 3.2+ (no associative arrays), coreutils only, no network.
#
# Contract (machine-readable):
#   usage:  quality_floor_check.sh --task TEXT --proposed-model NAME [--matrix FILE]
#   matrix: flat "key: value" YAML (default: ../templates/quality_floor_matrix.yaml)
#           tier1_models: comma list, tier2_models: comma list
#           task_<name>: tierN  (first keyword match wins; task_default is last)
#   output: task_floor=tierN
#           model_tier=tierN        (unknown model -> tier3)
#           verdict=PASS|FAIL
#           below_floor=yes|no
#           policy=cloud_only       (local/gguf models always FAIL)
#   exit:   0=PASS, 1=FAIL (below floor or local model), 2=usage error
set -eu

TASK="" MODEL="" SCRIPT_DIR=""

usage() {
  cat <<'EOF'
Usage: quality_floor_check.sh --task TEXT --proposed-model NAME [--matrix FILE]
Checks a proposed model against the task's quality floor.
Default matrix: <skill>/templates/quality_floor_matrix.yaml (flat key: value).
Output (stdout): task_floor=, model_tier=, verdict=PASS|FAIL,
                 below_floor=yes|no, policy=cloud_only
Exit codes: 0=PASS, 1=FAIL, 2=usage error
Example: quality_floor_check.sh --task "security code review" --proposed-model "claude-opus-5"
EOF
  exit 2
}

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

TIER1="" TIER2=""
get() { # get <key> from MATRIX_FILE
  awk -v k="$1:" 'index($0, k)==1 { sub(/^[^:]*:[ \t]*/, ""); print; exit }' "$MATRIX_FILE" 2>/dev/null
}

load_matrix() {
  TIER1="$(get tier1_models)"
  TIER2="$(get tier2_models)"
  [ -n "$TIER1" ] && [ -n "$TIER2" ] || { echo "error=matrix_invalid reason=missing_tier_lists file=$MATRIX_FILE" >&2; exit 2; }
}

model_tier() { # model_tier <name> -> tier1|tier2|tier3
  local m="$1" x
  for x in $(echo "$TIER1" | tr ',' ' '); do
    [ "$m" = "$x" ] && { echo "tier1"; return 0; }
  done
  for x in $(echo "$TIER2" | tr ',' ' '); do
    [ "$m" = "$x" ] && { echo "tier2"; return 0; }
  done
  echo "tier3"
  return 0
}

task_floor() { # task_floor <task> -> tierN (keyword match on task_* keys)
  local t="$1" line key val
  local t_n
  t_n="$(printf '%s' "$t" | tr ' ' '_')"
  local fallback=""
  while IFS= read -r line; do
    case "$line" in
      task_*:*)
        key="${line%%:*}"
        val="$(printf '%s' "${line#*:}" | sed 's/^[ \t]*//;s/[ \t]*$//')"
        case "$key" in
          task_default) fallback="$val"; continue ;;
          *) kw="${key#task_}"
             case "$t_n" in
               *"$kw"*) echo "$val"; return 0 ;;
             esac ;;
        esac
        ;;
    esac
  done < "$MATRIX_FILE"
  if [ -n "$fallback" ]; then echo "$fallback"; else echo "tier2"; fi
  return 0
}

tier_num() { echo "$1" | sed 's/tier//'; }

while [ "$#" -gt 0 ]; do
  case "$1" in
    --task) TASK="${2:-}"; shift 2 ;;
    --proposed-model) MODEL="${2:-}"; shift 2 ;;
    --matrix) MATRIX_FILE="${2:-}"; shift 2 ;;
    -h|--help) usage ;;
    *) echo "error=invalid_argument arg=$1" >&2; exit 2 ;;
  esac
done

[ -n "$TASK" ] || { echo "error=missing_required_args arg=task" >&2; usage; }
[ -n "$MODEL" ] || { echo "error=missing_required_args arg=proposed-model" >&2; usage; }
[ -n "${MATRIX_FILE:-}" ] || MATRIX_FILE="$SCRIPT_DIR/../templates/quality_floor_matrix.yaml"
[ -f "$MATRIX_FILE" ] || { echo "error=matrix_not_found file=$MATRIX_FILE" >&2; exit 2; }
load_matrix

# policy: local / offline models are never allowed (deployment policy: cloud only)
case "$MODEL" in
  *gguf*|*ollama*|*llama.cpp*|*local*|*tinyllama*|*onnx*)
    echo "task_floor=na"
    echo "model_tier=local"
    echo "verdict=FAIL"
    echo "below_floor=n/a"
    echo "policy=cloud_only"
    echo "reason=local_or_offline_model_forbidden"
    exit 1
    ;;
esac

FLOOR="$(task_floor "$TASK")"
MT="$(model_tier "$MODEL")"
FN="$(tier_num "$FLOOR")"
MN="$(tier_num "$MT")"

echo "task_floor=$FLOOR"
echo "model_tier=$MT"
# lower tier number = stronger. model tier number must be <= floor number.
if [ "$MN" -le "$FN" ]; then
  echo "verdict=PASS"
  echo "below_floor=no"
  echo "policy=cloud_only"
  exit 0
else
  echo "verdict=FAIL"
  echo "below_floor=yes"
  echo "policy=cloud_only"
  echo "degraded_mode=disclose_quality_reduction_to_user_and_suggest_retry"
  exit 1
fi
