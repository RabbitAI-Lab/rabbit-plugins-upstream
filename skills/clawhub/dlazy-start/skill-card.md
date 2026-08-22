## Description:

Quickstart guidance for AI orchestrators using @dlazy/cli to install and authenticate the CLI, discover available tools, invoke cloud and local tools, poll asynchronous tasks, and recover from common failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI orchestration agents use this skill to operate @dlazy/cli: install and authenticate the CLI, inspect tool schemas and costs, run cloud or local tools, poll long-running jobs, and apply common recovery steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes guidance to use browser session cookies for video downloading, which can expose access to logged-in sessions if an agent reads them without clear user intent.

Mitigation: Only allow browser-cookie access when the user explicitly requests it and understands the session-access implications.

Risk: API keys may be exposed if placed directly in shell commands or logs.

Mitigation: Prefer device-code login and avoid passing API keys inline; use scoped environment configuration when key-based authentication is necessary.

## Reference(s):

- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [@dlazy/cli source](https://github.com/dlazyai/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands and JSON-oriented CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is intended for agent-mediated CLI use and includes discovery-before-invocation checks.]

## Skill Version(s):

2.0.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
