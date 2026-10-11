## Description:

Analyzes resting pet videos to estimate breathing rate, flag deviations from species-specific ranges, and provide a report without making a veterinary diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, veterinary staff, and boarding providers use the skill to review resting breathing rates from pet videos, receive abnormal-rate alerts, and retrieve prior reports. Results are informational and do not replace veterinary assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos and video URLs are processed by lifeemergence.com cloud services and could include identifiable home or clinic footage.

Mitigation: Use only footage approved for cloud processing; obtain consent and confirm the publisher's retention and privacy practices before using sensitive recordings.

Risk: The skill silently creates or reuses an account identity and stores account tokens in a local workspace database.

Mitigation: Review identity and token handling before installation, and restrict access to the workspace and stored credentials.

Risk: Cloud history queries can retrieve reports linked to the automatically selected account context.

Mitigation: Confirm account identity and access controls before requesting or sharing historical reports.

Risk: Breathing-rate alerts may be mistaken for a diagnosis.

Mitigation: Treat results as a screening aid and seek veterinary evaluation for persistent or concerning symptoms.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-respiratory-rate-abnormal-detect-analysis)
- [Respiratory analysis API reference](artifact/references/api_doc.md)
- [Publisher's skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown reports and tables, or JSON analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include breathing-rate alerts, report links, and cloud report history.]

## Skill Version(s):

1.0.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
