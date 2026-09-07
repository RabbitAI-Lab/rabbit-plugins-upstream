# References: Incident command playbook (load in incident_commander mode)

Roles: Commander (mode + change approval) · Scribe (timeline + redaction) ·
Responder (approved diagnostics, 30–90 s timeouts) · Validator
(scripts/shieldswarm_validate.sh) · Quality-Floor Enforcer
(scripts/quality_floor_check.sh).

## Sequence
1. Declare the incident; assign Commander + Scribe; start the timeline
   (templates/incident_report.md).
2. Stabilize before optimize. One change at a time.
3. Every production change needs a rollback owner and a recorded approval
   (scripts/approval_gate.sh --risk high ...) BEFORE execution.
4. Diagnostics are bounded: 30–90 s timeouts; public endpoints at most three
   GET/HEAD per 10 minutes.
5. Communicate from templates/status_page_update.md and
   templates/stakeholder_update.md (redacted).
6. Close with templates/postmortem.md: timeline, roles, impact, root cause
   (or "unknown" — never invent), actions, model-resilience lessons.

## Rules of thumb
- Latency spikes → capacity/queue/backoff review, not code changes.
- Fallback storms → model_resilience mode + quality floor, then
  templates/model_fallback_audit.md.
- If two consecutive changes make it worse → revert both (recorded),
  re-triage.
