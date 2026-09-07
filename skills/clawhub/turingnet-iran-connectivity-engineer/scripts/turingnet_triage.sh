#!/usr/bin/env bash
# turingnet_triage.sh — 60-second triage checklist (non-interactive by default).
# Prints the checklist; --collect writes operator answers into a redacted-safe
# evidence file. Never prompts for secrets. Never networks. Exit 0.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
MODE="${1:-}"

cat <<'EOF'
TuringNet 60-second triage — Observe carefully. Protect people. Repair what is authorized.
[1] Safety  : own device/network/service or written authorization? NO → user-support mode only.
[2] Scope   : one device / one network / one service / many services?
[3] Time    : last known working? observed time + timezone? intermittent or constant?
[4] Evidence: redacted error text (run scripts/redact_pii.py before sharing);
              city/province at most, never precise location; access type; known-good comparison.
[5] Classify: device/LAN · Wi-Fi · mobile data · ISP/last-mile · DNS · TLS · service/CDN · routing/upstream · unknown.
[6] Act     : least disruptive reversible step first; provider escalation; authorized change plan
              (templates/change_review.md + rollback_plan.md) for operator work.
Prohibited: no bypass/circumvention, no scanning, no flooding, no credential collection.
Next: templates/evidence_intake_bilingual.md → classify via SKILL.md §6 → playbook.
EOF

if [ "$MODE" = "--collect" ]; then
  OUT="evidence_$(date +%Y%m%d_%H%M%S).md"
  {
    echo "# TuringNet triage record (auto-redacted on write)"
    for q in "Safety: own/authorized? (yes/no)" "Scope (device/network/service/many)" \
             "Last known working (time + tz)" "Observed time (time + tz)" \
             "Intermittent or constant" "Access type (mobile/broadband/office/wifi)" \
             "Redacted error text (no secrets, no numbers)" "Known-good comparison"; do
      printf '%s\n' "$q"
      read -r ANSW
      printf 'A: %s\n\n' "$ANSW"
    done
  } >> /tmp/turingnet_triage_raw.$$ 2>/dev/null || true
  # FAIL CLOSED: if redaction cannot run, never write unredacted answers.
  if python3 "$HERE/redact_pii.py" --input /tmp/turingnet_triage_raw.$$ --output "$OUT" --mode standard 2>/dev/null; then
    :
  else
    printf '# triage record withheld: redaction failed\n# (raw answers were NOT written; re-run and re-answer)\n' > "$OUT"
  fi
  rm -f /tmp/turingnet_triage_raw.$$
  echo "wrote $OUT (run scripts/guard.py --input $OUT before sharing)"
fi
exit 0
