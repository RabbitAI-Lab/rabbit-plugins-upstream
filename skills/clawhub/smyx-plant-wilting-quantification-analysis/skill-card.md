## Description:

Analyzes plant images or videos to estimate wilting severity and suggest whether underwatering or overwatering may be involved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners, growers, and developers use plant images or videos to assess wilting, review possible causes, and obtain watering or drainage guidance and historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images and videos are sent to external analysis services.

Mitigation: Avoid sensitive media and confirm the provider's data retention practices before use.

Risk: An automatically managed identity links analysis with cloud report history.

Mitigation: Review account handling and report access with the publisher before using personal or shared media.

Risk: Authentication tokens are stored in a local workspace database.

Mitigation: Avoid shared workspaces unless token storage and access protections are understood.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-plant-wilting-quantification-analysis)
- [Plant wilting API documentation](artifact/references/api_doc.md)
- [Skill usage demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis report or Markdown history table with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wilting severity, possible cause, and suggested intervention; optional saved report.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
