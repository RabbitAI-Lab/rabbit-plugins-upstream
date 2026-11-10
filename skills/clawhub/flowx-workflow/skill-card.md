## Description:

Use when building, auditing, inspecting, repairing, evolving, or running FlowX workflows with the Python SDK and bundled command-line scripts, including human-guided build repair and interactive workflow steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiechuxi](https://clawhub.ai/user/xiechuxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, inspect, repair, and run FlowX workflows, including reviewing generated code and guiding interactive repairs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow generation may send requirements and logs to an LLM and may execute generated tests or service code.

Mitigation: Authorize sensitive data and side effects before generation, protect keys and logs, and review generated code before launching a service.

Risk: The security evidence reports a partial scan with unresolved local path-like references, and advises checking command execution, tool scope, and automatic repair behavior.

Mitigation: Review referenced paths and the skill's requested tool scope before installation; inspect any proposed repairs and generated code before execution.

## Reference(s):

- [FlowX website](https://www.flow-x.work)
- [ClawHub flowX release](https://clawhub.ai/xiechuxi/skills/flowx-workflow)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands, JSON examples, and workflow code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated workflow code and artifact files.]

## Skill Version(s):

1.0.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
