## Description:

Analyzes submitted videos of children's activity areas for possible contact with preset dangerous objects or electrical sockets and returns structured findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and childcare staff can review submitted video for possible child contact with hazardous household objects or electrical sockets and receive a structured alert report. Treat the findings as an auxiliary review aid.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private child footage may be processed unexpectedly.

Mitigation: Wait for fixes to identity isolation and the environment-only option before using private footage; confirm the provider's storage and deletion practices.

Risk: Different users may share access to reports.

Mitigation: Avoid shared accounts and use a separate, non-secret identity.

Risk: Continuous safety monitoring and automatic emergency alerts are not established.

Mitigation: Use this for submitted-video analysis only; do not rely on it for continuous protection or emergency alerts.

## Reference(s):

- [API documentation](references/api_doc.md)
- [ClawHub release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-dangerous-object-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text, Markdown]

**Output Format:** [Structured analysis report in JSON or text; Markdown tables for history queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected object and action, confidence, event time, alert level, snapshot, and report link when returned by the service.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
