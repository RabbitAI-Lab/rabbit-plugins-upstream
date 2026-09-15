## Description:

Quickstart for AI orchestrators driving @dlazy/cli, covering installation, authentication, capability discovery, cloud and local tool invocation, asynchronous task polling, and common failure recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent operators use this skill to install and authenticate @dlazy/cli, discover available tools, invoke cloud and local commands, poll long-running tasks, and recover from common CLI failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install mutable CLI and runtime code.

Mitigation: Use a pinned and verified @dlazy/cli version where possible, avoid elevated global installs, and review installation commands before execution.

Risk: The skill can involve sensitive authentication values and browser-session data.

Mitigation: Keep API keys out of prompts and logs, do not enable browser-cookie access unless needed, and prefer an isolated browser profile.

Risk: Tool calls may send inputs to remote API endpoints or write downloaded outputs locally.

Mitigation: Confirm the selected tool, provider, model, cost shape, and output path before invocation, and use a restricted working directory for downloads and local runtimes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [@dlazy/cli source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that install mutable CLI/runtime code, authenticate with API keys, call cloud endpoints, download files, or use browser-session data.]

## Skill Version(s):

2.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
