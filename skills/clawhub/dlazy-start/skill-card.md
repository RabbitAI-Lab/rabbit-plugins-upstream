## Description:

A quickstart for AI agents using the dLazy CLI to discover and run cloud and local media tools, authenticate, and monitor long-running tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users follow this quickstart to install and authenticate the dLazy CLI, inspect available tools and their costs, invoke media tools, and troubleshoot asynchronous tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the CLI or optional runtimes executes third-party packages in the local environment.

Mitigation: Install only from trusted sources, and pin or preinstall dependencies in controlled environments.

Risk: API keys or browser cookies could expose credentials and active browser sessions.

Mitigation: Prefer device-code login over command-line keys; allow browser-cookie access only when explicitly intended for the target service.

Risk: Cloud tool calls may consume paid credits or access remote media services.

Mitigation: Inspect the tool and its cost before invocation; use dry runs where available.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy website](https://dlazy.com)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool responses may include JSON results or media URLs; long-running tasks require status polling.]

## Skill Version(s):

2.0.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
