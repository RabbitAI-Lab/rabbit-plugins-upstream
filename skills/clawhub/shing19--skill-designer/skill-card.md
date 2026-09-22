## Description:

Skill Designer helps users gather requirements and design an OpenClaw agent skill package, producing a SKILL.md and installation guide only after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shing19](https://clawhub.ai/user/shing19)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to turn a skill idea into a structured OpenClaw skill package with requirements, trigger conditions, implementation steps, constraints, and installation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skill packages may contain incomplete or unsuitable instructions if requirements or the selected plan are wrong.

Mitigation: Review and test the generated SKILL.md and README before installing the package into an agent.

Risk: The skill may create generated files in an output directory after the user confirms the design.

Mitigation: Confirm the design summary first, then inspect generated files before moving them into any agent skills directory.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a file package under output/<skill-id>/ after user confirmation; does not install or modify agent files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
