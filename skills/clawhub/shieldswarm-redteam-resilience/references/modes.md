# References: Mode playbooks (load only after mode selection)

Machine-readable summary first, prose second.

| mode | evidence | required template | forbidden |
|---|---|---|---|
| support_without_login | public | templates/no_login_diagnostic.md | private API calls, hidden endpoints, scraping, repeated probes, load |
| auth_user_support | user | templates/support_ticket.md | credential collection, session access, quota evasion, one-time-code requests |
| auth_operator | operator | templates/operator_authorization.yaml | unapproved prod changes, broad blocking, secret exposure |
| incident_commander | operator | templates/incident_report.md | optimizing before stabilizing, parallel changes |
| model_resilience | any | templates/quality_floor_matrix.yaml | silent downgrade below floor |
| red_team | operator | templates/red_team_roe.yaml | any test before ROE; DDoS/WAF-bypass/exploitation/stealth |
| ethical_promotion | any | templates/promotion_copy.md | spam, fake reviews, impersonation |

## support_without_login
1. Collect user-side evidence only: redacted error text, access type,
   known-good comparison, timestamp, broad location if volunteered.
2. Rate limit: maximum three single GET or HEAD requests in 10 minutes on
   public status pages. No load, no probing, no enumeration.
3. Output: templates/no_login_diagnostic.md, redacted per templates/redaction_checklist.md.
4. Escalation path: if the user can log in via the official UI, switch to
   auth_user_support and guide the official login flow (UI/OAuth/SSO/device
   flow). Never request passwords or one-time codes directly.

## auth_user_support
1. Scope: Agent Mode workspaces, skills, prompts, issue reports, product
   usage. No credential or session access; no quota evasion.
2. Help the user file a proper report: templates/support_ticket.md.
3. Pineapple mitigation (arena-power-user-playbook): for degraded/gateway
   symptoms, switch to model_resilience mode and enforce the quality floor
   instead of retrying blindly.

## auth_operator (approval-gated)
1. Fill templates/operator_authorization.yaml: scope, owner, approval,
   risk, validation metric, rollback trigger, abort conditions.
2. Every risky change: record an approval first
   (scripts/approval_gate.sh), run the command through
   scripts/shieldswarm_validate.sh, change one thing at a time.
3. Use templates/model_router_change_review.md for model routing changes and
   templates/rollback_plan.md before any production change.
4. Authorized: telemetry, config diffs, approved commands, rollback,
   hardening, model resilience, observability.
   Forbidden: unapproved prod changes, broad blocking, secret exposure.

## red_team (ROE REQUIRED — STOP SHIELDSWARM EXERCISE NOW is the emergency abort phrase)
1. Before ANY test: fill templates/red_team_roe.yaml — scope ("staging
   only" by default), abort conditions ("latency > 5 s or errors > 1 %"),
   approver, rollback owner, no-scan/no-flood/no-bypass clauses.
2. Allowed: tabletop exercises, config review, staging/lab validation,
   detection review, WAF rule review (templates/waf_rule_review.md).
3. Forbidden: public DDoS testing, WAF bypass, exploitation, stealth,
   login bypass, credential collection.
4. Record findings with templates/red_team_finding.md; every exercise ends
   with a templates/exercise_go_no_go.md decision.

## ethical_promotion
See references/promotion.md.
