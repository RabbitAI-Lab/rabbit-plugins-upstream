## Description:

Discover Lingry words, generate immutable candidates, and coin only the currently selected candidate after explicit user publication intent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[svetlyoh](https://clawhub.ai/user/svetlyoh)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and their agents discover public words, develop new word candidates from concepts, and publish a selected candidate only on explicit request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generating a candidate sends its concept to Lingry's external service.

Mitigation: Avoid including sensitive concepts, and never provide wallet secrets.

Risk: Coining publishes a candidate publicly and cannot be undone.

Mitigation: Show the selected candidate and require an explicit request to publish it before coining.

## Reference(s):

- [Lingry service](https://lingry.net)
- [Lingry ClawHub release](https://clawhub.ai/svetlyoh/skills/lingry)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown prose with word and candidate details; CLI responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Publication returns a transaction ID; candidate generation does not publish.]

## Skill Version(s):

2.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
