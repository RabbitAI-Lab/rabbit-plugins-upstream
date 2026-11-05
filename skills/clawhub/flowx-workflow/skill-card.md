## Description:

Use when building, inspecting, running, repairing, or evolving FlowX workflows with the FlowX MCP server or Python SDK. Covers background builds, human review, node repair, and service lifecycle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiechuxi](https://clawhub.ai/user/xiechuxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to turn process descriptions into reusable FlowX workflows, inspect generated artifacts, and run or evolve workflows with human review and controlled service lifecycle steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated workflow code may access files or expose a service when run.

Mitigation: Use a restricted workspace, inspect generated code before starting services, and check the service bind address and port before exposing it.

Risk: Workflow requirements and logs may be sent to the configured LLM provider, and external FlowX code and dependencies were not audited in this bundle.

Mitigation: Keep sensitive information out of prompts and logs unless authorized, and review the upstream version and dependencies before installation.

## Reference(s):

- [FlowX ClawHub skill page](https://clawhub.ai/xiechuxi/skills/flowx-workflow)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code, shell commands, and workflow artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated workflow code and service configuration for review.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
