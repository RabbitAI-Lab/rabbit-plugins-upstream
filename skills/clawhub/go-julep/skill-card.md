## Description:

Helps Go developers use a typed client to call the Julep API for agents, sessions, tasks, and related resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to add Julep API calls to an application, including managing agents and sessions, chatting, and inspecting task executions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Julep API key could be exposed in source code or logs.

Mitigation: Read the key from an environment variable; do not commit, log, or print it or request headers.

Risk: Create, update, delete, secret, or execution calls may change the Julep account or start billed work.

Mitigation: Review generated code and run account-changing calls only when explicitly requested for resources the task owns.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-julep)
- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-julep)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use a configured Julep API endpoint and an environment-provided API key.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
