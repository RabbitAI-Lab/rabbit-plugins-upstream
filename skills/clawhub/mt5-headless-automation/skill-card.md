## Description:

Run MetaTrader 5 headlessly on Linux or a VPS with Wine, Xvfb, xdotool, OCR, EA deployment, heartbeat monitoring, and auto-restart workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, engineers, and traders use this skill to configure and operate headless MetaTrader 5 automation for Expert Advisor attachment, deployment, heartbeat checks, and recovery on Linux or VPS environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles broker credentials and live trading operations.

Mitigation: Use a dedicated VPS or isolated display, test first with a demo or read-only account, keep credentials out of shell history and logs, and restrict credential file permissions.

Risk: Screen capture and OCR may collect sensitive trading, account, or desktop information.

Mitigation: Treat screenshots as sensitive artifacts, keep them in private temporary directories, remove them after use, and avoid running the automation on a shared desktop.

Risk: GUI automation may send keystrokes or clicks to the wrong MT5 window or UI element.

Mitigation: Verify the correct X display and MT5 window are active before running xdotool-based scripts, and review OCR matches before relying on unattended operation.

Risk: The watchdog can restart MT5 or reattach an EA during active trading.

Mitigation: Review watchdog behavior before production use, monitor heartbeat and EA logs, and understand that restarts can interrupt active strategies or detach automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/mt5-headless-automation)
- [Telegram Bot API endpoint](https://api.telegram.org)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands, shell scripts, configuration requirements, and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Wine, Xvfb, xdotool, OCR tooling, MT5 credentials, and local configuration files.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
