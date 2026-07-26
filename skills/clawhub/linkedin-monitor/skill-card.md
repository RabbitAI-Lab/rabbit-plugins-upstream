## Description: <br>
Monitors LinkedIn inbox messages on a schedule, drafts replies in the user's communication style, and alerts configured chat channels with progressive autonomy options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dylanbaker24](https://clawhub.ai/user/dylanbaker24) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and operators use this skill to monitor LinkedIn inboxes, prevent duplicate message alerts, and prepare replies for approval or limited automation through Clawdbot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires ongoing access to a LinkedIn account and inbox. <br>
Mitigation: Install only when this access is intended, monitor authentication health, and disable scheduled checks when continuous access is no longer needed. <br>
Risk: LinkedIn session cookies may be stored in a local credentials file. <br>
Mitigation: Treat ~/.clawdbot/linkedin-monitor/credentials.json as a sensitive secret, restrict local file access, and prefer environment-provided credentials where operationally practical. <br>
Risk: Inbox content and drafted replies can be forwarded to configured chat channels. <br>
Mitigation: Use private alert channels, verify channel targets during setup, and avoid routing alerts to shared or public spaces. <br>
Risk: Higher autonomy levels can send replies or perform scheduling with unclear approval boundaries. <br>
Mitigation: Keep the default approval-based level or monitor-only mode unless automatic replies and meeting booking are explicitly desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dylanbaker24/skills/linkedin-monitor) <br>
- [LinkedIn Monitor setup guide](docs/SETUP.md) <br>
- [LinkedIn Monitor troubleshooting guide](docs/TROUBLESHOOT.md) <br>
- [LinkedIn Monitor cron payload](CRON-PAYLOAD.md) <br>
- [Clawdbot project](https://github.com/clawdbot/clawdbot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown alerts, JSON configuration, shell commands, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include message previews, drafted replies, state summaries, health-check results, and setup or recovery commands.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
