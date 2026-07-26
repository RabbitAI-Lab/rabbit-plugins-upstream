## Description: <br>
Monitor CamelCamelCamel price drop alerts via RSS and send Telegram notifications when items go on sale. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jgramajo4](https://clawhub.ai/user/jgramajo4) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to set up scheduled monitoring of their own CamelCamelCamel RSS price-alert feed and receive Telegram-ready notifications for new Amazon price drops. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CamelCamelCamel RSS URL is personal and can reveal the user's product watchlist if shared. <br>
Mitigation: Use only the user's own feed URL, keep it private, and review scheduled commands before storing them in cron. <br>
Risk: A cron entry continues running until it is removed and may keep fetching the feed after it is no longer wanted. <br>
Mitigation: Review the cron schedule during setup and remove or disable the job when monitoring is no longer needed. <br>
Risk: The local alert cache controls duplicate detection, so deleting or corrupting it can retrigger old notifications. <br>
Mitigation: Clear the cache only for testing or reset scenarios and keep the cache directory under the user's control. <br>


## Reference(s): <br>
- [CamelCamelCamel Alerts Setup Guide](references/SETUP.md) <br>
- [CamelCamelCamel](https://camelcamelcamel.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash examples and JSON alert output from the RSS fetch script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches a user-provided RSS URL, writes a local cache file, and emits alert records suitable for notification handling.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
