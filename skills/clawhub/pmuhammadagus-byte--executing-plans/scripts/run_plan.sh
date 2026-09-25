#!/usr/bin/env bash
# Walk a SHARP plan step by step, ENFORCING verification before the next step.
# Safe: read-only on the plan file; never runs destructive ops itself.
#
# Usage:
#   bash scripts/run_plan.sh path/to/plan.md
#
# For every step it shows the Acceptance + Verify, then asks you to run the
# verify command yourself and paste the result. A step is only "done" when you
# confirm the verify command passed. No verify = you must supply one.
set -euo pipefail

PLAN="${1:-}"
if [ -z "$PLAN" ] || [ ! -f "$PLAN" ]; then
  echo "Usage: bash scripts/run_plan.sh <plan.md>" >&2
  exit 1
fi

# extract sharpness score if present
score=$(grep -oE 'sharpness score: [0-9]+/100' "$PLAN" | grep -oE '[0-9]+' | head -1 || true)
[ -n "$score" ] && echo "== Plan sharpness score: $score/100 (need >=80 before executing) =="

echo "=== Executing plan: $PLAN ==="
echo "Per step: read Acceptance + run the Verify command. Confirm the verify PASSED."
echo

step_no=0
while IFS= read -r line; do
  if [[ "$line" =~ ^[[:space:]]*\|\ ?([0-9]+)\ \| ]]; then
    # table row step from make_plan.py output
    step_no=$((step_no + 1))
    step_txt=$(echo "$line" | awk -F'|' '{print $3}' | sed 's/^ *//;s/ *$//')
    acc=$(echo "$line" | awk -F'|' '{print $4}' | sed 's/^ *//;s/ *$//')
    ver=$(echo "$line" | awk -F'|' '{print $5}' | sed 's/^ *//;s/ *$//')
    echo "--- STEP $step_no: $step_txt ---"
    [ "$acc" != "—" ] && echo "  Acceptance: $acc"
    if [ "$ver" != "—" ] && [ -n "$ver" ]; then
      echo "  Verify:     $ver"
      # read confirmation from the real terminal, not the plan file
      if [ -t 0 ]; then exec 3<&0; else exec 3</dev/tty 2>/dev/null || exec 3<&0; fi
      echo "  >> Run the verify command above. Did it PASS? [y/N]: "
      read -r ans <&3
      case "$ans" in
        y|Y) echo "  [ok] step $step_no verified" ;;
        *) echo "  [stop] step $step_no NOT verified — record deviation, do not fake success, stop."; exit 2 ;;
      esac
    else
      echo "  [!] No verify command for this step. Plan is not SHARP. Stop and fix plan."
      exit 3
    fi
  elif [[ "$line" =~ ^[[:space:]]*([0-9]+)\.\  ]]; then
    # fallback: plain "1. text" steps (no matrix)
    step_no=$((step_no + 1))
    echo "--- STEP $step_no (plain): $line ---"
    if [ -t 0 ]; then exec 3<&0; else exec 3</dev/tty 2>/dev/null || exec 3<&0; fi
    echo "  No verification matrix found. Supply a verify command to proceed [y/N]: "
    read -r ans <&3
    case "$ans" in
      y|Y) echo "  [ok] step $step_no recorded (verify provided manually)" ;;
      *) echo "  [stop] step $step_no unverified — stop."; exit 2 ;;
    esac
  fi
done < "$PLAN"

echo
echo "=== Plan walk complete ($step_no steps) ==="
echo "Stop at review checkpoints. Report before merging/deleting. Record deviations."
