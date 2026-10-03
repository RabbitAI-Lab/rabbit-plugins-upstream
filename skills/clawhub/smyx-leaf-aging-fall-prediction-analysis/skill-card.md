## Description:

Analyzes houseplant leaf images or video to estimate aging trends and predict when leaves may fall, with care suggestions and report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Plant owners, greenhouse staff, and plant-care services use this skill to review leaf aging and near-term shedding risk from images or video and consult prior reports for care planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images or video and related metadata are sent to configured cloud services.

Mitigation: Confirm the service operator and data handling before submitting private media.

Risk: The skill silently creates or reuses an identity and stores service tokens locally.

Mitigation: Review the account used, token storage, and how to remove local identity data before installation.

Risk: Historical reports are linked to the service account and may expose prior media analysis.

Mitigation: Limit access to report history and confirm how to delete cloud reports.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-leaf-aging-fall-prediction-analysis)
- [Leaf aging prediction API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured report text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include care suggestions and report links; predictions are for plant-care guidance.]

## Skill Version(s):

1.0.16 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
