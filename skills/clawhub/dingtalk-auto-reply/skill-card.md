## Description:

Monitors unread DingTalk conversations, generates AI replies for single chats in the user's own voice, and sends WeChat notifications for group or excluded conversations instead of auto-replying.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to monitor DingTalk unread messages, generate single-chat replies with CodeBuddy Agent SDK, and route group messages or risky cases to WeChat for manual handling. It is intended for users who deliberately want an unattended workplace chat assistant with configurable dry-run, grounding, and safety controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-send DingTalk single-chat replies as the user.

Mitigation: Begin with DRY_RUN=1, validate generated replies with _validate.py, and only enable live sending after confirming the persona, skip lists, and manual-escalation behavior.

Risk: The assistant can read workplace messages and media and may use broad tools through CodeBuddy, gbrain, dws, and optional local code search.

Mitigation: Keep CODE_SEARCH_ROOTS empty unless source-code search is required, disable gbrain or extra tools for sensitive chats, and limit DingTalk permissions to the documented message and contact scopes.

Risk: The installation can modify PATH and create a Windows Startup launcher for unattended persistence.

Mitigation: Review generated startup files and PATH changes before live use, and use stop_monitor.ps1 or the platform process manager to stop the monitor when unattended operation is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/dingtalk-auto-reply)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [dws-reply-examples.md](artifact/dws-reply-examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration values, Python scripts, and generated chat reply text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local configuration, logs, media cache, audit records, and a Windows startup launcher when installed and run.]

## Skill Version(s):

0.1.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
