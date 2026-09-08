## Description:

Quickstart guidance for AI orchestrators using @dlazy/cli to install and authenticate the CLI, discover tools, invoke cloud and local tools, poll asynchronous tasks, and recover common failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to drive @dlazy/cli from setup through tool discovery, invocation, async status polling, and failure recovery. It is intended for agents that need concise operational guidance for cloud and local dLazy tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install and run an external npm package and optional local runtimes.

Mitigation: Install only when the dLazy CLI publisher is trusted, review the package and runtime requirements first, and run it in an environment appropriate for external tooling.

Risk: Authentication can involve API keys and a local config file at ~/.dlazy/config.json.

Mitigation: Prefer device-code login, avoid placing API keys in commands or logs, and protect the local dLazy configuration file.

Risk: Some workflows may request access to browser cookies for video downloads.

Mitigation: Use a dedicated browser profile or scoped cookie export, and approve cookie access only for workflows that truly need it.

Risk: Cloud generation tools may incur cost or run against changing provider registries.

Mitigation: Run dlazy tools list and dlazy tools describe before invocation, check cost shape when available, and use dry-run validation before paid calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [@dlazy/cli source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes command patterns for npm or npx install, device-code or API-key authentication, JSON input files, dry runs, asset saving, and async task polling.]

## Skill Version(s):

2.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
