## Description:

Quickstart for AI orchestrators (Claude Code / Cursor / Codex / Copilot) driving @dlazy/cli, covering install, auth, capability discovery, cloud and local tool invocation, async task polling, and common failure recovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to install and authenticate @dlazy/cli, discover available tools, invoke cloud and local media/text tools, poll asynchronous tasks, and recover from common CLI failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-cookie use for video downloading can expose account session data to the tool.

Mitigation: Review cookie-based workflows before installing or running the skill, use only accounts and browsers approved for that exposure, and prefer normal authentication or non-cookie inputs when possible.

Risk: Registered CLI tools and cost shapes may change over time, which can lead to incorrect or unexpected tool calls.

Mitigation: Run dlazy tools list and dlazy tools describe before claiming a tool exists or invoking paid generation, and record provider, model, and cost information before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-start)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source link from artifact metadata](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with inline bash commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to verify tool availability with dlazy tools list and dlazy tools describe before invocation.]

## Skill Version(s):

2.0.8 (source: server release metadata; artifact frontmatter lists 2.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
