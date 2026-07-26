## Description: <br>
Tracks Microsoft Outlook email and optional Microsoft Teams messages on Windows, reminds the user about likely replies or action items, and helps draft concise Outlook email replies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abhinavjp](https://clawhub.ai/user/abhinavjp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees and professionals who use Outlook Desktop and Teams use this skill to monitor recent communication, surface messages that likely need action, generate reminder text, and draft short email replies for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access private Outlook mailbox data and, when enabled, Teams chat data. <br>
Mitigation: Install only when that access is acceptable, configure only the needed accounts and scopes, and review generated drafts or reminders before acting on them. <br>
Risk: Configuration, token cache, state, and thread context files may contain sensitive communication data. <br>
Mitigation: Keep those files out of shared or synced folders and periodically delete cached scan and draft context files. <br>
Risk: Telegram reminders can expose message details outside Outlook or Teams. <br>
Mitigation: Review reminder content before sending it to Telegram and avoid broad subject searches on sensitive threads. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/abhinavjp/skills/ms-outlook-teams-assistant) <br>
- [Publisher profile](https://clawhub.ai/user/abhinavjp) <br>
- [Configuration example](references/config.example.json) <br>
- [Teams Graph setup](references/teams-graph-setup.md) <br>
- [Writing style](references/writing-style.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text and Markdown guidance, JSON cache files, shell commands, configuration snippets, and optional Outlook draft containers.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not auto-send email or Teams messages; reminder and draft content is intended for user review before sending.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
