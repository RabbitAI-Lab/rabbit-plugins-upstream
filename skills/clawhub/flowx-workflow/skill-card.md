## Description:

Use when building, auditing, inspecting, repairing, evolving, or running FlowX workflows with the Python SDK and bundled command-line scripts, including human-guided build repair and interactive workflow steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiechuxi](https://clawhub.ai/user/xiechuxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build, inspect, repair, evolve, and run FlowX workflows. It guides human review of generated code and workflow execution, including interactive repair and runtime steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow generation and repair can produce code that is later executed, and the skill documents file, network, and shell capabilities.

Mitigation: Review generated code and tests before execution, use a workspace and credentials with only the needed access, and keep interactive repair enabled when human guidance is required.

Risk: A generated workflow service may bind to a network interface, and the documented default host is 0.0.0.0.

Mitigation: Use 127.0.0.1 for local-only service binding unless broader access is intended and authorized.

Risk: Workflow requirements and logs may be sent to the configured language model during generation or repair.

Mitigation: Avoid sending sensitive requirements or logs unless their use with the configured provider is authorized.

## Reference(s):

- [FlowX website](https://flow-x.work)
- [ClawHub release page](https://clawhub.ai/xiechuxi/skills/flowx-workflow)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance, Python code and commands, and JSON-lines interaction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide generation and execution of workflow code; review generated code before running it.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
