## Description:

Analyzes patient images and videos for tremors, convulsions, stiffness, and gait abnormalities to support home monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams and developers use this skill to review patient footage for possible movement abnormalities and retrieve prior monitoring reports. Results support monitoring, not clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive patient videos, image URLs, and report history requests are sent to a cloud service.

Mitigation: Confirm patient consent and review the service's privacy, retention, and data-handling terms before use with real footage.

Risk: The skill creates or reuses a local workspace identity database that may store service tokens.

Mitigation: Review local data storage and account-linking expectations; protect access to the workspace.

Risk: Monitoring results may be mistaken for a medical diagnosis.

Mitigation: Treat results as monitoring aids and refer clinical decisions to qualified healthcare professionals.

## Reference(s):

- [Analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links or be saved to a file.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata; bundled SKILL.md declares 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
