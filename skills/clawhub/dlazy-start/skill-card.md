## Description:

Quickstart for AI orchestrators using @dlazy/cli, covering installation, authentication, capability discovery, cloud and local tool invocation, async task polling, and common failure recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to install and authenticate @dlazy/cli, discover available cloud and local tools, invoke them through structured CLI commands, poll async jobs, and recover from common failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys can be exposed through prompts, command history, or shared logs.

Mitigation: Prefer the device-code login flow, avoid placing API keys directly in prompts or shell commands, and store credentials only in the intended configuration or environment locations.

Risk: Browser cookie access can expose active web sessions.

Mitigation: Use cookies_from_browser only when deliberately needed, treat exported cookies like passwords, and prefer a dedicated browser profile for this workflow.

Risk: Generated media workflows may call cloud services and consume credits.

Mitigation: Run tool discovery and dry-run validation first, check cost information with dlazy tools describe, and record the expected provider, model, and cost before paid calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source link from skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes CLI discovery, authentication, tool invocation, async polling, dry-run, cost-check, and recovery guidance.]

## Skill Version(s):

2.0.12 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
