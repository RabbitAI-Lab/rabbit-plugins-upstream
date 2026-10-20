## Description:

Analyzes plant images or videos to estimate wilting severity and suggest whether underwatering or overwatering may be responsible.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners, greenhouse operators, and developers use the skill to assess plant wilting from images or videos, review possible watering causes, and retrieve historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images or videos and report queries are sent to the LifeEmergence cloud service.

Mitigation: Share only content you are comfortable sending to the service; check its data handling before use.

Risk: The skill silently creates or reuses a cloud identity and stores service tokens locally.

Mitigation: Before installing, confirm how identities, historical reports, the local database, and tokens can be viewed, deleted, or disabled.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-plant-wilting-quantification-analysis)
- [Plant wilting API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report or JSON; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wilting severity, possible cause, care suggestions, and report links; optional saved result file.]

## Skill Version(s):

1.0.17 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
