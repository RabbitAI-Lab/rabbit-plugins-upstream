## Description:

Analyzes thermal-camera footage of gatherings to identify people whose forehead temperatures differ from the group and recommend a thermometer recheck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Households and operators of shared activity spaces can use the skill to screen groups in thermal-camera footage for relative temperature differences and review analysis reports. It provides preliminary screening guidance and recommends confirming alerts with a calibrated thermometer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configuration-only runs can upload private footage, and the provider's upload, retention, and deletion practices are unverified.

Mitigation: Avoid private footage until the configuration-only issue is fixed; obtain participant consent and confirm the provider's upload, retention, account-deletion, and credential-storage policies.

Risk: Shared accounts can mix report histories, and request handling may expose credentials.

Mitigation: Avoid shared workspaces until sender isolation is fixed, and verify credential destinations before use.

Risk: Relative thermal readings can be affected by visibility and environmental conditions and are not a medical diagnosis.

Mitigation: Use clear thermal footage, treat alerts as preliminary screening, and recheck with a calibrated thermometer.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-thermal-fever-screening-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis reports, Markdown report lists, alerts, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports describe relative thermal differences and do not provide a medical diagnosis.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
