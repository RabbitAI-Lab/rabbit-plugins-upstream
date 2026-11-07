## Description:

Use when building, auditing, inspecting, repairing, evolving, or running FlowX workflows with the Python SDK and bundled command-line scripts, including human-guided build repair and interactive workflow steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiechuxi](https://clawhub.ai/user/xiechuxi)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers use this skill to build, inspect, repair, evolve, and run FlowX workflows through its Python SDK and bundled command-line tools. It guides interactive build repair and workflow steps while emphasizing review of generated code and control of sensitive inputs and logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workflow requirements and logs may be sent to an LLM.

Mitigation: Approve which information may be shared and avoid sending sensitive data without authorization.

Risk: Generated tests and workflow services may execute code.

Mitigation: Use a dedicated environment with limited access, review generated services before launch, and bind local services to 127.0.0.1.

Risk: API keys and output logs may contain sensitive information.

Mitigation: Keep secrets out of command arguments and protect both output logs and process streams.

## Reference(s):

- [FlowX project repository](https://github.com/AIpRoBuilder/FlowX)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline shell commands, Python examples, and JSON-lines examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
