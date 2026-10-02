## Description:

Analyzes infant sleep media for prone positioning and face covering, returning risk reports and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and developers use the skill to review infant sleep images or videos for potential suffocation risks and retrieve prior risk reports. It is an aid to monitoring, not a substitute for adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant or home footage and media URLs are sent to a cloud service for analysis.

Mitigation: Review the service's privacy terms and share media only with appropriate consent.

Risk: The skill silently creates or reuses an identity, logs in remotely, and stores authentication tokens locally.

Mitigation: Review identity and token handling before installation; restrict access to the workspace data directory.

Risk: History requests can retrieve sensitive prior reports from the cloud without explicit confirmation.

Mitigation: Require user confirmation before looking up report history.

Risk: Automated alerts may miss hazards or give a false sense of safety.

Mitigation: Continue direct adult supervision and promptly check the infant when a risk is reported.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-infant-suffocation-warning-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured report text or JSON; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk indicators, recommendations, and report links when available.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release; bundled frontmatter states 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
