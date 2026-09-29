## Description:

Analyzes video for gaze direction and facial pose to estimate focus, distraction, and mind-wandering in classroom, office, and driving scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit classroom, office, or driving video for concentration analysis and receive structured focus metrics, observations, recommendations, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload videos or video URLs containing people to lifeemergence.com services for cloud processing.

Mitigation: Use it only with consent from recorded people and when cloud processing and report retention are acceptable for the deployment.

Risk: The skill can silently create or reuse an internal user identity and persist authentication tokens in a local workspace database.

Mitigation: Run it in an isolated workspace, restrict workspace access, and clear stored identity or token data when changing users or environments.

Risk: Historical report queries can retrieve cloud-stored analysis records associated with the resolved user identity.

Mitigation: Limit use to authorized report owners and review report links before sharing outputs outside the intended audience.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-focus-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown report with structured JSON results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the generated analysis output to a user-specified file path.]

## Skill Version(s):

1.0.15 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
