## Description: <br>
Send messages to Google Chat spaces and users via webhooks or OAuth for notifications, alerts, channel updates, and direct messages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[darconada](https://clawhub.ai/user/darconada) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operations teams use this skill to send Google Chat notifications, alerts, and messages to known spaces or existing direct-message spaces. It supports fast static channel delivery through incoming webhooks and dynamic space discovery or posting through OAuth. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Webhook URLs, OAuth credentials, and OAuth token files can authorize posting to Google Chat destinations. <br>
Mitigation: Store these values as secrets, restrict access to them, and rotate them if they are exposed. <br>
Risk: Messages can be sent to the wrong Google Chat space, direct-message space, or webhook destination. <br>
Mitigation: Verify the target space, space ID, or webhook URL before sending, especially for alerts or sensitive operational updates. <br>
Risk: OAuth setup can grant broad messaging and space-discovery access for the selected Google account or Chat app. <br>
Mitigation: Use the least-privileged account or Chat app that can complete the workflow and review the requested Google Chat scopes before authorizing. <br>
Risk: Sensitive message content may be posted into shared Google Chat spaces. <br>
Mitigation: Avoid sending secrets, personal data, or restricted business information unless the destination and approval path are appropriate. <br>


## Reference(s): <br>
- [Configuration Example](references/config-example.json) <br>
- [Google Cloud Console](https://console.cloud.google.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces messaging instructions and command invocations for webhook or OAuth-based Google Chat delivery.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
