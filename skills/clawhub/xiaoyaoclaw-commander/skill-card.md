## Description:

Drive OpenClaw from Agent Skills-compatible tools such as Claude Code, Codex, OpenCode, Trae, and DSH, limited to user-named agents, channels, or status queries with confirmation before externally visible or side-effecting actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to let an external agent tool command a local XiaoyaoClaw/OpenClaw gateway, list health and agents, dispatch work to a specified agent, or send a confirmed channel message.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent dispatch and channel messaging can affect local files or real recipients.

Mitigation: Confirm the exact agent or channel, target, and message before allowing side-effecting or externally visible commands.

Risk: Installing the skill enables external tools to command a local OpenClaw gateway.

Mitigation: Install only when that cross-tool command path is intended, and treat read-only status checks separately from actions that dispatch agents or send messages.

Risk: Incorrect command construction can expose user text to shell interpretation.

Mitigation: Pass user-controlled text as argv data with quoted variables or explicit flag values, and avoid eval, sh -c, Invoke-Expression, or string-concatenated commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-commander)
- [GitHub documentation](https://github.com/dtsola/xiaoyaoclaw-commander)
- [XiaoyaoClaw overview](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended to be executed only for user-specified targets, with confirmation before agent dispatch or channel messages.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
