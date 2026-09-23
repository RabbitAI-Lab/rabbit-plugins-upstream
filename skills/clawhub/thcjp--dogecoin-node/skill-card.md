## Description:

Helps agents set up and operate a Dogecoin Core full node with RPC access, blockchain tooling, and configurable automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to guide Dogecoin Core full-node setup, RPC configuration, status checks, and troubleshooting across common agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask an agent to run system commands, modify files, configure RPC access, expose ports, or start and stop services.

Mitigation: Require the agent to show each command, file change, RPC setting, exposed port, and service action for approval before execution.

Risk: The security summary flags vague operating boundaries and unsupported safety claims.

Mitigation: Review the planned node configuration and network exposure against local security requirements before installation or operation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/dogecoin-node)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON response examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file changes, RPC configuration, exposed ports, and service start or stop actions that require review before execution.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
