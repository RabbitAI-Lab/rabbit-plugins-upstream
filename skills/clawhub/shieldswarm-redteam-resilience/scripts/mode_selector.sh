#!/bin/bash
# ShieldSwarm mode_selector.sh — deterministic mode + first-action selection.
# Portable: bash 3.2+ (no associative arrays), coreutils only, no network.
#
# Contract (machine-readable):
#   usage:  mode_selector.sh --symptom TEXT --evidence {public|user|operator}
#   output: mode=<mode>  action=<first_action>  required=<file>  next=<hint>
#   exit:   0 = selected, 2 = usage error
# Modes: support_without_login | auth_user_support | auth_operator |
#        incident_commander | model_resilience | red_team | ethical_promotion
set -eu

SYMPTOM=""
EVIDENCE=""

usage() {
  cat <<'EOF'
Usage: mode_selector.sh --symptom TEXT --evidence {public|user|operator}
Deterministic selection of defensive mode and first action.
Output (stdout, one key=value per line): mode=, action=, required=, next=
Exit codes: 0=selected, 2=usage error
Example: mode_selector.sh --symptom "cannot login" --evidence public
EOF
  exit 2
}

emit() { # emit <mode> <action> <required> <next>
  echo "mode=$1"
  echo "action=$2"
  echo "required=$3"
  echo "next=$4"
  exit 0
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --symptom) SYMPTOM="${2:-}"; shift 2 ;;
    --evidence) EVIDENCE="${2:-}"; shift 2 ;;
    -h|--help) usage ;;
    *) echo "error=invalid_argument arg=$1" >&2; exit 2 ;;
  esac
done

[ -n "$SYMPTOM" ] || { echo "error=missing_required_args arg=symptom" >&2; usage; }
case "$EVIDENCE" in
  public|user|operator) ;;
  *) echo "error=invalid_evidence value=$EVIDENCE allowed=public|user|operator" >&2; exit 2 ;;
esac

s="$SYMPTOM"

# Priority-ordered, first match wins. Order: explicit roles before generic words.
case "$s" in
  *red\ team*|*redteam*|*purple*|*"tabletop"*)
    emit red_team "write_roe_before_any_test" "templates/red_team_roe.yaml" "fill templates/red_team_roe.yaml (scope, abort, approver, rollback owner) BEFORE any test" ;;
  *outage*|*"is down"*|*degraded*|*5xx*|*502*|*503*|*504*)
    if [ "$EVIDENCE" = "public" ]; then
      emit incident_commander "collect_public_status_evidence" "templates/status_page_update.md" "public evidence only; rate limit 3 GET/HEAD per 10 min"
    else
      emit incident_commander "stabilize_before_optimize" "templates/incident_report.md" "assign Commander+Scribe; one change at a time; see references/incident.md"
    fi ;;
  *fallback*|*model*slow*|*overloaded*|*quality\ floor*|*gateway*|*"too many errors"*)
    emit model_resilience "enforce_quality_floor" "templates/quality_floor_matrix.yaml" "run scripts/quality_floor_check.sh before any model change; never silently downgrade" ;;
  *promot*|*marketing*|*"advertise"*)
    emit ethical_promotion "prepare_honest_copy" "templates/promotion_copy.md" "opt-in sharing only; no spam/impersonation; see references/promotion.md" ;;
  *"cannot login"*|*"can't login"*|*"can not login"*|*login*|*sign\ in*|*credential*)
    case "$EVIDENCE" in
      public)   emit support_without_login "collect_user_side_evidence" "templates/no_login_diagnostic.md" "redacted user-side evidence only; no private probing" ;;
      user)     emit auth_user_support "guide_official_login_flow" "templates/support_ticket.md" "official UI/OAuth/SSO/device flow; never request credentials or one-time codes" ;;
      operator) emit auth_operator "confirm_scope_and_approval" "templates/operator_authorization.yaml" "confirm scope, permissions, approval, rollback owner before any action" ;;
    esac ;;
  *slow*|*latency*|*timeout*|*throttl*|*rate\ limit*)
    case "$EVIDENCE" in
      public)   emit support_without_login "collect_public_performance_evidence" "templates/no_login_diagnostic.md" "public metrics only; no load generation" ;;
      user)     emit auth_user_support "document_user_side_impact" "templates/support_ticket.md" "user-side timestamps and error text (redacted)" ;;
      operator) emit incident_commander "capacity_and_backoff_review" "templates/incident_report.md" "CDN cache, rate limits, queue backoff; see references/modes.md" ;;
    esac ;;
  *)
    case "$EVIDENCE" in
      public)   emit support_without_login "collect_user_side_evidence" "templates/no_login_diagnostic.md" "no keyword matched; treat as public support" ;;
      user)     emit auth_user_support "document_user_side_impact" "templates/support_ticket.md" "no keyword matched; treat as authenticated user support" ;;
      operator) emit auth_operator "confirm_scope_and_approval" "templates/operator_authorization.yaml" "no keyword matched; confirm authorization before proceeding" ;;
    esac ;;
esac
