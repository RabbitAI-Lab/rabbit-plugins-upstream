## Description: <br>
Send messages, upload files, list channels, query users, manage scheduled messages, search messages, and set bot status in Slack using the Web API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gaolfun](https://clawhub.ai/user/gaolfun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and Slack workspace operators use this skill to let an agent perform Slack Web API tasks such as posting messages, finding channels or users, uploading files, searching messages, and managing scheduled messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Slack scopes can expose more workspace content than a task requires. <br>
Mitigation: Grant only the scopes needed for enabled features, and avoid private-channel, DM, or search scopes unless they are necessary. <br>
Risk: Slack bot tokens can allow workspace actions if exposed. <br>
Mitigation: Store tokens securely, do not paste real tokens into chats or tracked files, and revoke or regenerate compromised tokens. <br>
Risk: File or URL uploads can share unintended content in Slack. <br>
Mitigation: Confirm local files and URL content before uploading them to a Slack channel or direct message. <br>


## Reference(s): <br>
- [Slack App Setup](https://api.slack.com/apps) <br>
- [Slack chat.postMessage API](https://slack.com/api/chat.postMessage) <br>
- [Slack conversations.list API](https://slack.com/api/conversations.list) <br>
- [Slack users.info API](https://slack.com/api/users.info) <br>
- [Slack files.uploadV2 API](https://slack.com/api/files.uploadV2) <br>
- [Slack chat.scheduleMessage API](https://slack.com/api/chat.scheduleMessage) <br>
- [Slack search.messages API](https://slack.com/api/search.messages) <br>
- [Slack users.profile.set API](https://slack.com/api/users.profile.set) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API Calls, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown-style status messages with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Slack bot token and the Slack scopes needed for the requested API methods.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
