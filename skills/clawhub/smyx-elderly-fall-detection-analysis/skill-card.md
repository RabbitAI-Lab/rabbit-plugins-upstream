## Description:

Analyzes home-monitoring images or videos for possible falls and returns detection reports and historical report listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and home-monitoring operators use the skill to review possible falls in an older person's monitoring images or videos and retrieve prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home-monitoring media, URLs, and identity-linked report history may be sent to the Life Emergence cloud service.

Mitigation: Use only with informed consent from people monitored and after confirming the cloud service's handling of sensitive data.

Risk: The skill may silently create or reuse a local identity, register or log in remotely, and store access tokens in the workspace data directory.

Mitigation: Review identity creation and token storage before installation; restrict access to the workspace data directory.

Risk: Fall-detection results are safety alerts rather than confirmation of a medical emergency.

Mitigation: Have a person verify suspected falls promptly and follow an appropriate emergency response procedure.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-elderly-fall-detection-analysis)
- [Fall-detection API documentation](artifact/references/api_doc.md)
- [Skill usage demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured detection reports and Markdown historical report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include recommendations and links; results can optionally be saved to a file.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release; artifact frontmatter lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
