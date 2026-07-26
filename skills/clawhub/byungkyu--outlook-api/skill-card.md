## Description: <br>
Outlook provides a Maton-managed Microsoft Graph integration for reading, sending, and managing Outlook mail, folders, calendar events, and contacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to work with a connected Outlook account through Maton, including mailbox review, email sending, folder management, calendar event operations, and contact management. It is useful when a workflow needs Outlook access through CLI commands, direct API calls, or short code examples. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access and change email, folders, calendar events, and contacts in the connected Outlook account. <br>
Mitigation: Install only if you trust Maton to broker Outlook access, and review recipients, message contents, folders, events, and contacts before approving write or delete actions. <br>
Risk: When multiple Outlook accounts are connected, an action may target the wrong account. <br>
Mitigation: Use a specific connection ID whenever more than one Outlook account is available. <br>


## Reference(s): <br>
- [ClawHub Outlook skill listing](https://clawhub.ai/byungkyu/skills/outlook-api) <br>
- [Microsoft Graph API overview](https://learn.microsoft.com/en-us/graph/api/overview) <br>
- [Microsoft Graph Mail API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview) <br>
- [Microsoft Graph Calendar API](https://learn.microsoft.com/en-us/graph/api/resources/calendar) <br>
- [Microsoft Graph Contacts API](https://learn.microsoft.com/en-us/graph/api/resources/contact) <br>
- [Microsoft Graph query parameters](https://learn.microsoft.com/en-us/graph/query-parameters) <br>
- [Maton CLI manual](https://cli.maton.ai/manual) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Code, Configuration guidance] <br>
**Output Format:** [Markdown guidance with shell, HTTP, Python, and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and an active Outlook OAuth connection.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
