## Description:

Use when choosing, reusing, naming, building, auditing, inspecting, repairing, evolving, or running FlowX workflows for a user request, including passing inputs and human-guided build repair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiechuxi](https://clawhub.ai/user/xiechuxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to select and operate FlowX workflows or build and repair workflows for a user's request, including reviewing generated code and service behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial, and runtime permission enforcement was not verified.

Mitigation: Review the skill's capabilities and tool scope before installation, and confirm the target runtime enforces appropriate permissions.

Risk: Workflow generation can send requirements or logs to an LLM and may execute generated tests; generated code can have side effects.

Mitigation: Avoid sending sensitive data without authorization, inspect generated code and logs, and review code before starting its service.

## Reference(s):

- [FlowX ClawHub release](https://clawhub.ai/xiechuxi/skills/flowx-workflow)
- [FlowX repository (linked in the skill)](https://github.com/AIpRoBuilder/FlowX)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands, JSON inputs, and generated workflow files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated code and workflow artifacts for review.]

## Skill Version(s):

1.0.8 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
