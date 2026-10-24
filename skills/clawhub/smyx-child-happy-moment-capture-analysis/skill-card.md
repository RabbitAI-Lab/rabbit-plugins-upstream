## Description:

Analyzes child activity videos for joyful moments and returns event reports and suggested positive reinforcement for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and authorized childcare teams use the skill to analyze child activity videos, review joyful-moment reports, and retrieve historical reports. Child footage is sent to a cloud service, so use requires guardian consent and appropriate privacy controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child video files or URLs are sent to a cloud service.

Mitigation: Obtain guardian consent, verify authorization and masking controls before public or childcare use, and confirm retention and deletion policies before sending footage.

Risk: The skill creates or reuses a local identity and stores service tokens in the workspace.

Mitigation: Restrict access to the workspace and review stored identities and tokens before deployment.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or Markdown reports, with JSON detail available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event details, report links, and a Markdown table of historical reports.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; bundled frontmatter says 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
