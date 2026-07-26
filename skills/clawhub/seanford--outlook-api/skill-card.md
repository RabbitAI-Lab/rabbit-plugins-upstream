## Description: <br>
Microsoft Outlook API integration with managed OAuth for reading, sending, and managing email, folders, calendar events, and contacts through Microsoft Graph. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to make authenticated Outlook and Microsoft Graph requests through Maton for mailbox, calendar, and contact workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authorized Outlook actions can send email or modify or delete messages, folders, calendar events, and contacts. <br>
Mitigation: Require the agent to show recipients, message content, target items, requested operation, and account connection before write or delete actions are approved. <br>
Risk: A Maton API key allows the agent to act through the user's authorized Outlook connection. <br>
Mitigation: Store MATON_API_KEY securely, avoid pasting it into prompts or logs, and rotate it if it may have been exposed. <br>
Risk: When multiple Outlook connections exist, omitting the Maton-Connection header can use the default active connection. <br>
Mitigation: Specify the intended connection ID with the Maton-Connection header for account-sensitive requests. <br>


## Reference(s): <br>
- [Microsoft Graph API Overview](https://learn.microsoft.com/en-us/graph/api/overview) <br>
- [Microsoft Graph Mail API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview) <br>
- [Microsoft Graph Calendar API](https://learn.microsoft.com/en-us/graph/api/resources/calendar) <br>
- [Microsoft Graph Contacts API](https://learn.microsoft.com/en-us/graph/api/resources/contact) <br>
- [Microsoft Graph Query Parameters](https://learn.microsoft.com/en-us/graph/query-parameters) <br>
- [ClawHub Outlook API Listing](https://clawhub.ai/seanford/skills/outlook-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with HTTP endpoint descriptions and Python, JavaScript, and shell examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY for live Outlook requests] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
