## Description: <br>
Use this skill when you need to control Slack from Clawdbot via the slack tool, including reacting to messages or pinning and unpinning items in Slack channels or DMs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents use this skill to perform Slack workspace actions such as reacting to messages, sending or editing messages, reading recent messages, managing pins, fetching member information, and listing custom emoji. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read, send, edit, delete, pin, and unpin Slack content when the configured bot token has those permissions. <br>
Mitigation: Install it only where the bot token has the minimum Slack scopes needed, and confirm the channel, message timestamp, and user intent before write actions or reading sensitive conversations. <br>


## Reference(s): <br>
- [ClawHub Slack skill listing](https://clawhub.ai/steipete/skills/slack) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Guidance] <br>
**Output Format:** [JSON action payloads and concise Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Slack channel, message, user, emoji, and content identifiers appropriate to the requested action.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
