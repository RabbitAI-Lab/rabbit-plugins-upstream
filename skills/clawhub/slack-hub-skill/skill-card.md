## Description: <br>
Send messages, reply in threads, search workspace content, and list Slack channels through a Slack Bot integration with rate-limit handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[icyfrosty](https://clawhub.ai/user/icyfrosty) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and workspace automation users can use this skill to let an agent post Slack messages, reply in threads, search workspace content, and list channels where the configured bot token has access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A configured Slack bot token can allow the agent to post messages and search workspace content. <br>
Mitigation: Use a narrowly scoped Slack bot token, store it as a secret, and enable the skill only in workspaces where agents are allowed to post and search. <br>
Risk: The implementation can request private-channel listing even though the documentation describes listing public channels. <br>
Mitigation: Review the requested Slack scopes and channel-listing behavior before installation, and restrict token permissions to the minimum channels and metadata needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/icyfrosty/skills/slack-hub-skill) <br>
- [Publisher profile](https://clawhub.ai/user/icyfrosty) <br>
- [Slack chat.postMessage API](https://slack.com/api/chat.postMessage) <br>
- [Slack search.messages API](https://slack.com/api/search.messages) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API calls, JSON, Guidance] <br>
**Output Format:** [JSON responses and concise Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Slack bot token supplied through SLACK_BOT_TOKEN.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
