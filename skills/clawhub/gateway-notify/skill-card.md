## Description: <br>
Set up automatic notifications when OpenClaw gateway restarts. Use when user wants to be notified of gateway startup events via any messaging channel (iMessage, WhatsApp, Telegram, Discord, etc.). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deemoartisan](https://clawhub.ai/user/deemoartisan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to install a persistent gateway startup hook that sends restart notifications to a selected messaging channel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The hook is persistent and sends a notification on every gateway startup. <br>
Mitigation: Confirm the user wants persistent startup notifications before setup, and use the uninstall script plus a gateway restart to disable the hook. <br>
Risk: Notifications pass through the selected third-party messaging provider and may expose message metadata. <br>
Mitigation: Verify the destination channel and address before installation and keep the default timestamp-only notification unless additional data sharing is explicitly accepted. <br>
Risk: Customizing the handler can add local model, port, or configuration details to outbound messages. <br>
Mitigation: Treat any customization that includes local details as opt-in data egress and review the handler before deployment. <br>


## Reference(s): <br>
- [Manual Setup Guide](references/MANUAL.md) <br>
- [Supported Channels](references/CHANNELS.md) <br>
- [Security & Privacy](SECURITY.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Code, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and generated hook configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup and uninstall guidance for a persistent OpenClaw gateway startup notification hook.] <br>

## Skill Version(s): <br>
2.1.5 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
