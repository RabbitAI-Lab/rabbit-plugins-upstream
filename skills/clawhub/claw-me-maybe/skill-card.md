## Description: <br>
Beeper integration for Clawdbot that helps agents search chats, send messages, summarize unread messages, manage reactions and reminders, download attachments, and mark chats as read across connected messaging platforms through the local Beeper Desktop API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickhamze](https://clawhub.ai/user/nickhamze) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let a Clawdbot-enabled agent work with their local Beeper Desktop API for cross-platform chat search, message sending, unread-message triage, reactions, reminders, attachments, and read-state updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change messages across connected Beeper chat accounts. <br>
Mitigation: Install only when this access is intended, and confirm recipients, platform, message text, and state-changing actions before execution. <br>
Risk: A Beeper access token grants sensitive local API access. <br>
Mitigation: Treat BEEPER_ACCESS_TOKEN like a password and store it only in the user's local Clawdbot configuration. <br>
Risk: Changing the local API URL could expose messaging automation beyond the intended local Beeper Desktop API. <br>
Mitigation: Keep the API local unless intentionally changing BEEPER_API_URL and understanding the exposure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nickhamze/skills/claw-me-maybe) <br>
- [Publisher profile](https://clawhub.ai/user/nickhamze) <br>
- [Beeper](https://www.beeper.com) <br>
- [Beeper download](https://www.beeper.com/download) <br>
- [Beeper Developer Docs](https://developers.beeper.com) <br>
- [Beeper MCP](https://www.beeper.com/mcp) <br>
- [Beeper Desktop API Reference](https://developers.beeper.com/desktop-api-reference/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Beeper Desktop with the local Desktop API enabled and curl available.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata; artifact frontmatter reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
