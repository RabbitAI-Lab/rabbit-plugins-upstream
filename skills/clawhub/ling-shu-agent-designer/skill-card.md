## Description:

Ling Shu Agent Designer helps users turn business requirements into runnable OpenClaw agents by producing scenario outlines, workspace configuration, and dedicated skill packages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[perrykono-debug](https://clawhub.ai/user/perrykono-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business teams use this skill to design industry-specific agents from requirements, confirm a scenario outline, and create an initial OpenClaw workspace with supporting skill packages and configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated OpenClaw workspace files, configuration, and skill packages may change an agent's behavior if accepted without review.

Mitigation: Confirm the generated outline before allowing file creation, and review generated skill or publishing output before binding it into an Agent setup.

Risk: A generated agent outline may contain incorrect scope, data-source, delivery, schedule, skill, security, or approval assumptions.

Mitigation: Require review and confirmation of the seven scenario outline files before creating the base agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/perrykono-debug/skills/ling-shu-agent-designer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown files, JSON configuration, and skill package guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation of the scenario outline before creating the base agent skeleton.]

## Skill Version(s):

2.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
