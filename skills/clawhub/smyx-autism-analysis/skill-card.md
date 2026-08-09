## Description:

Analyzes child autism-spectrum behavior in images or videos, identifies potential core symptom features, and returns structured reports with intervention suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators can use this skill to submit child behavior media for preliminary ASD behavior screening support, structured findings, report links, and intervention suggestions. The output is screening support and should not be treated as a clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child video or image data may be uploaded to the publisher's cloud service.

Mitigation: Use only with appropriate consent and privacy review; avoid submitting identifiable child content unless the publisher's retention, deletion, and medical-disclaimer policies are acceptable.

Risk: The skill may silently create or reuse an account identity and store tokens locally.

Mitigation: Review identity and token storage behavior before installation, and remove or rotate stored tokens according to local policy.

Risk: Autism-analysis output may be mistaken for a clinical diagnosis.

Mitigation: Present results as preliminary screening support and direct users to qualified medical professionals for diagnosis or care decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-autism-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON structured analysis reports, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a publisher cloud service and may store or retrieve report history associated with an internal identity.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
