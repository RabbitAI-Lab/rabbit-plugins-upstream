## Description:

Drive OpenClaw from Claude Code, Codex, OpenCode, Trae, DSH, and other Agent Skills tools to command the local gateway, agents, and channels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent-tool users use this skill to let an external Agent Skills-compatible assistant operate a local XiaoyaoClaw/OpenClaw gateway. It helps locate the OpenClaw CLI, choose an explicit OpenClaw agent, query gateway state, and prepare channel-message commands when the user requests them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is a command bridge that can dispatch work to a local OpenClaw agent.

Mitigation: Require the user to identify the target OpenClaw agent and confirm the agent identity before running dispatch commands.

Risk: Channel-message commands can create externally visible messages in Feishu, Telegram, Slack, Discord, or similar channels.

Mitigation: Review and confirm both the recipient and message content before sending any channel message.

Risk: Gateway credentials and agent permissions are inherited from the local environment.

Mitigation: Do not store credentials in the skill and avoid local modes or direct service calls that bypass the configured OpenClaw gateway controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-commander)
- [README.en.md](README.en.md)
- [Design notes](docs/DESIGN.md)
- [Claude Code and OpenClaw research report](docs/research-report-claude-code-openclaw.md)
- [XiaoyaoClaw overview](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell and PowerShell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include OpenClaw CLI command proposals, environment variable setup, agent-selection guidance, and channel-message checks.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
