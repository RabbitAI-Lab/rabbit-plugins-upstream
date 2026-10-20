## Description:

Analyzes home-monitoring images or videos for possible falls and provides detection reports and access to report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and developers use this skill to check home-monitoring images or videos for possible falls and review detection reports. Alerts require prompt human confirmation and appropriate emergency follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive in-home images, videos, and media URLs are sent to cloud services.

Mitigation: Obtain consent and confirm service retention and deletion practices before processing real monitoring footage.

Risk: A persistent account identity may be created or reused, with service tokens stored locally.

Mitigation: Review account isolation and protect access to the workspace and its stored tokens.

Risk: Fall-detection results may be mistaken for definitive safety assessments.

Mitigation: Confirm alerts with a person and follow the appropriate emergency response procedure.

## Reference(s):

- [Fall detection API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured detection reports and Markdown tables of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk guidance and links to reports; results can be saved to a file.]

## Skill Version(s):

1.0.17 (source: ClawHub release metadata; artifact frontmatter says 1.0.21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
