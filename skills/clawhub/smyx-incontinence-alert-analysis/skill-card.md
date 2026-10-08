## Description:

Analyzes care images, videos, or media URLs for possible wet clothing and excretion, returning alerts and care reports for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and care teams use the skill to assess images or videos of older adults, bedridden patients, or infants for possible incontinence and to review prior care reports. Results support, rather than replace, hands-on checks and professional judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive care images, videos, URLs, and report data may be sent to lifeemergence.com services.

Mitigation: Use only with patient, guardian, or authorized caregiver consent; confirm cloud retention and access controls before use.

Risk: The skill may silently create or reuse an account identity and store tokens in a local SQLite database.

Mitigation: Review account creation and protect local token storage before deployment in a caregiving setting.

Risk: Cloud history retrieval has limited user control and may expose prior care reports.

Mitigation: Limit report access to authorized caregivers and verify the records returned for the intended patient.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-incontinence-alert-analysis)
- [Skill API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured care analysis, alerts, recommendations, and Markdown-linked historical reports; optional JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings require human confirmation; historical reports are retrieved from the cloud.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata; bundled frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
