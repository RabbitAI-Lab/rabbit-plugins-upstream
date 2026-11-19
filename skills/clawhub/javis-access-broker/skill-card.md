## Description:

For each outside-agent request, Javis's access broker asks for clarification when needed and returns only the minimum answer supported by the prepared data slice, citing each point.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samuel-wei](https://clawhub.ai/user/samuel-wei)

### License/Terms of Use:

MIT-0

## Use Case:

External agents use this skill to answer a scoped question about a user's Javis data while limiting disclosure to facts needed for the stated task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan has medium confidence: an undeclared tool scope and partial inspection leave uncertainty about effective access.

Mitigation: Review the incompletely inspected components and confirm that granted tools and network or shell access are limited to the task.

## Reference(s):

- [Submit answer schema](references/submit-answer.schema.json)
- [ClawHub skill listing](https://clawhub.ai/samuel-wei/skills/javis-access-broker)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON answer payload with concise summary points or exact segment references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each shared point cites a slice item; answers are limited to the stated task.]

## Skill Version(s):

0.2.0 (source: package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
