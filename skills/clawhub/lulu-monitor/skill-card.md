## Description: <br>
AI-powered LuLu Firewall companion for macOS that monitors firewall alerts, analyzes connections, sends Telegram notifications with Allow/Block buttons, and helps set up or troubleshoot LuLu integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[easonc13](https://clawhub.ai/user/easonc13) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and macOS users use this skill to install, configure, and operate a LuLu Firewall companion that forwards firewall alerts to Telegram and supports user-selected Allow or Block actions. It also provides troubleshooting guidance for LuLu, OpenClaw Gateway, Telegram callbacks, launchd service status, and Accessibility permissions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install script fetches and runs code outside the reviewed artifact and installs npm production dependencies. <br>
Mitigation: Review the remote repository and npm dependency tree before running the install script, and avoid installation if you require all executable code to be present in the reviewed artifact. <br>
Risk: The service can apply Allow or Block choices to LuLu firewall alerts, and optional auto-execute mode can allow traffic automatically. <br>
Mitigation: Keep auto-execute disabled by default, prefer temporary Allow Once or Block Once actions, and enable automatic changes only when you accept the firewall-rule impact. <br>
Risk: The monitor installs a persistent launchd service and requires Accessibility permission to control LuLu. <br>
Mitigation: Remove the LaunchAgent and revoke Accessibility permission when the monitor is no longer needed. <br>


## Reference(s): <br>
- [LuLu Firewall](https://objective-see.org/products/lulu.html) <br>
- [OpenClaw Telegram channel documentation](https://docs.openclaw.ai/channels/telegram) <br>
- [LuLu Monitor ClawHub page](https://clawhub.ai/easonc13/skills/lulu-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration snippets, and endpoint examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local service commands, launchd commands, OpenClaw configuration, Telegram callback examples, and install or uninstall guidance.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
