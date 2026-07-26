## Description: <br>
Send push notifications via Gotify when long-running tasks complete or important events occur. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmagar](https://clawhub.ai/user/jmagar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to send Gotify notifications for task completion, status updates, important events, and errors from agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Gotify app tokens are stored locally and used to create notification messages. <br>
Mitigation: Keep the credential file private, use a Gotify token limited to message creation, and rotate the token if it is exposed. <br>
Risk: Notification text is sent over the network to the configured Gotify server and may include task details. <br>
Mitigation: Use HTTPS and avoid putting secrets or highly sensitive task details in notification messages. <br>


## Reference(s): <br>
- [Gotify API documentation](https://gotify.net/docs/) <br>
- [ClawHub Gotify skill page](https://clawhub.ai/jmagar/skills/gotify) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with bash commands and Gotify JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, network access to the configured Gotify server, and a local Gotify app token configuration.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md frontmatter and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
