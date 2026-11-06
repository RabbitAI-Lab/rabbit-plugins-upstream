## Description:

Analyzes succulent photos and videos for black rot, water-soaked tissue, and stretching, and returns a structured report with severity and confidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home succulent growers, greenhouse operators, and flower shops can use the skill to assess plant images or videos for common abnormal states and review previous reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The service automatically registers accounts and retains login tokens.

Mitigation: Confirm account creation, retention, and token deletion terms before use.

Risk: Analysis sends media to lifeemergence.com, and export-only or endpoint options may not work as intended.

Mitigation: Submit only media you intend to send to that service, and wait for fixes before relying on those options.

Risk: Identity and credential fields may not be separated.

Mitigation: Avoid configuring valuable API secrets until those fields are separated.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-succulent-special-state-detection-analysis)
- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured JSON analysis report; Markdown table for history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports detected state, severity, confidence, affected area, and report link when available.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
