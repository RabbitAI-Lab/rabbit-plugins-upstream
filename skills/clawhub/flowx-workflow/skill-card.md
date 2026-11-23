## Description:

flowX is a tool to build your agent's own reusable workflows through conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiechuxi](https://clawhub.ai/user/xiechuxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use FlowX to build, inspect, repair, and run reusable workflows by writing artifacts against task contracts and reviewing tested services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review has medium confidence and incomplete analysis, so its benign verdict is not a guarantee of safety.

Mitigation: Review tool access and inspect workflow artifacts before running a service.

Risk: Generated workflows can make external or paid provider calls and may use configured credentials.

Mitigation: Inspect generated code, configure only needed credentials, and authorize paid or external calls before real runs.

## Reference(s):

- [flowX on ClawHub](https://clawhub.ai/xiechuxi/skills/flowx-workflow)

## Skill Output:

**Output Type(s):** [Code, Configuration, Shell commands, Markdown guidance]

**Output Format:** [Code, JSON, shell commands, and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow artifacts vary by task and may include executable service code and tests.]

## Skill Version(s):

1.0.12 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
