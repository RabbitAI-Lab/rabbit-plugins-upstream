## Description:

weixin-debounce20s enables an OpenClaw agent to install, configure, restart, and verify 20-second WeChat burst debouncing for the local WeChat channel.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yechang1450](https://clawhub.ai/user/yechang1450)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw operators use this skill to enable or repair WeChat burst-message merging by installing the ClawBot WeChat fork when needed, setting the inbound debounce window to 20000 ms, restarting the gateway, and verifying behavior with logs and a live test.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill can replace the official WeChat channel plugin with an unpinned third-party fork and restart the OpenClaw gateway.

Mitigation: Install only after confirming the intended plugin package and version, keep a rollback plan for reinstalling the official plugin and restoring prior OpenClaw configuration, and obtain user approval before installing the plugin package.

Risk: The debounce behavior may be ineffective if the OpenClaw inbound settings are not set to 20000 ms or the gateway is not restarted.

Mitigation: Validate the OpenClaw configuration, restart the gateway, and verify that logs and a live WeChat burst test show the 20000 ms debounce window working.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yechang1450/skills/weixin-debounce20s)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose OpenClaw plugin installation, OpenClaw configuration edits, gateway restart, and verification steps.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
