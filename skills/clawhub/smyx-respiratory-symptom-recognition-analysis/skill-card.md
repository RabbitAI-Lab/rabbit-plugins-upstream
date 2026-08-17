## Description:

Based on computer vision, this skill analyzes respiratory videos or video URLs to detect coughing, phlegm, and wheezing frequency, count symptom episodes, and return early health-monitoring alerts and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to submit respiratory monitoring videos or video URLs for cloud analysis of coughing, sputum, wheezing, and related risk signals. It can also retrieve cloud-hosted historical analysis reports associated with the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Respiratory videos, video URLs, identity-linked request metadata, and report-history queries are sent to a LifeEmergence cloud service.

Mitigation: Evaluate with non-sensitive media first and install only after confirming acceptable privacy, retention, deletion, and account-control terms.

Risk: The skill can silently create or reuse identities, store access tokens locally, and retrieve health report history.

Mitigation: Use a dedicated workspace or test identity for evaluation, review local token storage, and avoid using production identities until the behavior is approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis)
- [Publisher Profile](https://clawhub.ai/user/18072937735)
- [Respiratory Symptom Recognition API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown text with structured JSON analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report history entries and report-image export URLs when listing prior analyses.]

## Skill Version(s):

1.0.13 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
