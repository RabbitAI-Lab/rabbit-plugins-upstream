## Description: <br>
A defensive, authorization-gated template pack for SRE and SecOps incident response, purple-team planning, model resilience reviews, approval records, rollback planning, and redacted evidence handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
SRE, SecOps, and platform operators use this skill to plan authorized defensive resilience work, incident response, purple-team exercises, model fallback reviews, and production change controls. It provides templates and guidance for approvals, rules of engagement, rollback plans, redaction, status updates, and postmortems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Use outside an authorized defensive scope could create operational or policy risk. <br>
Mitigation: Install and use the skill only for authorized defensive operations with explicit scope, rules of engagement, and abort criteria. <br>
Risk: Advertised validation or approval gates may be incomplete or unavailable in a consuming environment. <br>
Mitigation: Treat bundled templates as aids, not enforcement; require real human approval, rollback ownership, and independent review before production-impacting action. <br>
Risk: Incident evidence, logs, screenshots, or support artifacts may contain secrets or personal data. <br>
Mitigation: Redact credentials, tokens, private prompts, logs, screenshots, and other sensitive data before sharing or storing evidence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/shieldswarm-redteam-resilience) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>
- [Agent discovery card](artifact/AGENT_DISCOVERY.md) <br>
- [Quickstart template](artifact/templates/quickstart.md) <br>
- [Authorization intake template](artifact/templates/authorization_intake.yaml) <br>
- [Red-team rules of engagement template](artifact/templates/red_team_roe.yaml) <br>
- [Model resilience policy template](artifact/templates/model_resilience_policy.yaml) <br>
- [Validation checklist](artifact/templates/validation_checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown templates, YAML templates, Python self-test code, and concise operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Authorization-gated and defensive-only; production-impacting action should require human approval, rollback ownership, and secret redaction.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter/changelog states 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
