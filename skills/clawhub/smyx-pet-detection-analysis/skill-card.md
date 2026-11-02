## Description:

Detects cats, dogs, and birds appearing in the target area; supports video stream and image detection, suitable for home pet monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users can analyze household images and videos to detect and count cats, dogs, and birds, then review structured results or query prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Household media is sent to Life Emergence cloud services, and report history may expose data across users.

Mitigation: Review retention and billing terms before uploading private footage, and require separate sender identities when the agent is shared.

Risk: Credentials may be mishandled or confused with account identifiers.

Mitigation: Keep API secrets separate from account identifiers, protect token storage, and verify that export-only mode works as expected.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill walkthrough](https://lifeemergence.com/sample.html)
- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-pet-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON and readable analysis reports; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include detection counts and confidence details; history results may include report links.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
