## Description:

GDPR Check helps agents preview a 12-item GDPR compliance checklist and, with an API key, submit answers to compliancehub.cn for scored compliance guidance and local report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users, compliance teams, and developers use this skill to run a structured GDPR readiness check, preview checklist items locally, and produce text, JSON, or HTML reports from scored runs. The skill is general compliance guidance and not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored runs send GDPR checklist answers and an API key to compliancehub.cn.

Mitigation: Confirm the destination and data-sharing posture before a scored run; use preview mode when answers should remain local.

Risk: The generated compliance report may be mistaken for legal advice.

Mitigation: Use the report as compliance guidance only and have qualified counsel review legal conclusions.

Risk: API key handling can expose access if stored or shared carelessly.

Mitigation: Provide the key through COMPLIANCEHUB_API_KEY or the documented per-user key file with restrictive permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/gdpr-check)
- [ComplianceHub account and API key page](https://compliancehub.cn/account.html?skill=gdpr-check)
- [ComplianceHub service endpoint](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [text, json, html, files, shell commands, configuration, guidance]

**Output Format:** [Terminal text, JSON preview data, HTML reports, and optional report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preview mode lists checklist items without sending answers; scored runs require an API key and send checklist answers to compliancehub.cn.]

## Skill Version(s):

1.1.0 (source: package.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
