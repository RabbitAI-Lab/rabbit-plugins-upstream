## Description: <br>
Enables an agent to send plain-text Slack messages to channels or users and read recent channel history through a configured Slack bot token. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workspace operators use this skill to automate basic Slack notifications and inspect recent channel messages from an agent. It is suited to simple channel updates, direct reminders, and lightweight channel-history review when the bot has the required Slack scopes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can post messages to Slack channels or users, so an incorrect destination or message can disclose information or create unwanted workspace noise. <br>
Mitigation: Confirm the target channel or user and review message content before sending. <br>
Risk: Reading channel history can expose sensitive workspace conversations to the agent session. <br>
Mitigation: Use the smallest practical read limit and only retrieve Slack history from workspaces and channels where the operator has permission. <br>
Risk: Slack operations depend on bot membership and scopes such as chat:write and channels:read. <br>
Mitigation: Authorize the bot only for relevant channels and scopes, and resolve Slack permission errors before retrying. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/slack-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON action payloads and Slack tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces plain-text Slack messages and recent-message records containing text, user IDs, and timestamps.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
