## Description:

Use when choosing, reusing, naming, building, auditing, inspecting, repairing, evolving, or running FlowX workflows for a user request, including prompt/image/video media workflows, passing inputs, and human-guided build repair.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiechuxi](https://clawhub.ai/user/xiechuxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to select, create, inspect, repair, and run FlowX workflows for tasks such as media generation and other repeatable processes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated workflow code and tests may execute locally, media provider calls may incur costs, and automated analysis was partial.

Mitigation: Review generated code before running it, authorize paid provider calls, and treat generated or provider-returned content as untrusted.

## Reference(s):

- [FlowX workflow skill on ClawHub](https://clawhub.ai/xiechuxi/skills/flowx-workflow)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files]

**Output Format:** [Markdown guidance, shell commands, and generated workflow code and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local workflow generation and execution; outputs depend on the requested workflow.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
