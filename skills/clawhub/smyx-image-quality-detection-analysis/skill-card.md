## Description:

Analyzes camera images and video for black or white screens, color casts, stripes, noise, and blur to support surveillance maintenance and camera self-checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Security camera operators and maintenance teams use this skill to identify image-quality faults in camera captures or video and review analysis reports and historical results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images or provided media URLs are sent to LifeEmergence cloud APIs, potentially exposing sensitive surveillance footage.

Mitigation: Obtain consent and review data sensitivity and cloud handling before submitting camera media; avoid sensitive surveillance media unless approved.

Risk: The skill silently creates or reuses a local account identity and stores account tokens.

Mitigation: Review identity and token storage before installation; restrict access to local account data and use only in approved workspaces.

Risk: Shared workspaces may expose another user's cloud report history through a reused identity.

Mitigation: Avoid multi-user deployments until identity isolation and access controls are established.

## Reference(s):

- [Image quality analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured text or JSON, with report links; optionally saved to a file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can list historical cloud reports; results are for maintenance guidance, not a substitute for hardware inspection.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
