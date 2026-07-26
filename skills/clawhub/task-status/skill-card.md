## Description: <br>
Send short status descriptions in chat for long-running tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mightyprime1](https://clawhub.ai/user/mightyprime1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to send brief progress, success, warning, or error updates during long-running agent or command-line tasks, including optional periodic heartbeat messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Status text may be sent through Clawdbot to Telegram, including to a default recipient when TELEGRAM_TARGET is not set. <br>
Mitigation: Set TELEGRAM_TARGET explicitly, confirm the Clawdbot gateway token is appropriate, and test delivery in a controlled channel before using the skill for real task updates. <br>
Risk: Status messages, task names, details, local state, and JSONL logs may reveal sensitive filenames, operational context, or task progress. <br>
Mitigation: Do not include secrets or sensitive filenames in status text, and clean up monitor state files and JSONL logs after use. <br>
Risk: Background monitors can continue sending heartbeat updates until stopped or cancelled. <br>
Mitigation: Stop each monitor with a final status or run the cancellation command when a task is interrupted or complete. <br>


## Reference(s): <br>
- [Task Status Usage Guide](references/usage.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/mightyprime1/skills/task-status) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples and short status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Status messages are intended to stay under 140 characters; delivery can depend on Clawdbot gateway, Telegram target, and monitor interval settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
