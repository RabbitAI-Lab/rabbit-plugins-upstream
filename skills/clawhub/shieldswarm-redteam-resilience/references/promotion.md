# References: Ethical promotion, publishing gate, refusal (load in ethical_promotion mode)

## Pre-publish gate (all required)
1. bash scripts/shieldswarm_validate.sh over every shipped command example.
2. python3 tools/shieldswarm_selftest.py → ALL CHECKS PASSED.
3. Redaction pass over every artifact: templates/redaction_checklist.md.
4. README.md contains: functionality, permissions, security & privacy,
   verification hash (sha256 of stable files).

## Ethical promotion rules
- Honest docs, demos, changelog. No spam, no fake reviews, no
  impersonation, no bulk rating/download farming.
- Community sharing is opt-in only; the skill does not authorize
  autonomous promotion of any kind.
- This skill is community-built. Never claim endorsement by, staff access
  to, or privileged access from Arena/OpenClaw/ClawHub.

## Refusal and redirection (use verbatim, then redirect)
If asked for prohibited offensive work: state the boundary in one short
sentence, refuse, and redirect to a lawful alternative:
"ShieldSwarm is defensive-only: no attack traffic, no login bypass, no
credential collection. I can help with lawful troubleshooting,
privacy-preserving documentation, official support channels, or authorized
resilience work under a written ROE."
Redirect targets: authorized resilience work (ROE), detection review,
hardening, privacy-preserving docs, accessibility, official support.
