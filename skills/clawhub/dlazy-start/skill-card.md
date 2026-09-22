## Description:

Quickstart for AI orchestrators driving @dlazy/cli through installation, authentication, capability discovery, cloud and local tool invocation, async task polling, and common failure recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to install, authenticate, inspect, and invoke @dlazy/cli tools from orchestrators such as Claude Code, Cursor, Codex, Copilot, and OpenClaw. It helps agents discover available commands before use, submit JSON inputs, poll long-running generation tasks, and recover from common CLI failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs agents to install and run an unpinned external @dlazy/cli package.

Mitigation: Review the package before use and prefer a pinned package version in controlled environments.

Risk: Authentication can involve DLAZY_API_KEY and credentials stored in ~/.dlazy/config.json.

Mitigation: Keep API keys out of logs and shell history, restrict access to the config file, and use scoped credentials where available.

Risk: Some tool calls can incur costs or write generated assets to local paths.

Mitigation: Confirm provider, model, and cost before paid calls, and choose --save destinations deliberately.

Risk: The cookies_from_browser option can use local browser session data.

Mitigation: Use browser cookies only when necessary and only with accounts and environments approved for that workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [@dlazy/cli source metadata link](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agent-produced CLI invocations, JSON input-file usage, status polling, and failure recovery steps.]

## Skill Version(s):

2.0.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
