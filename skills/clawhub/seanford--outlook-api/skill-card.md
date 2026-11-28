## Description:

Microsoft Outlook API integration with managed OAuth for reading, sending, and managing emails, folders, calendar events, and contacts via Microsoft Graph.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to interact with Outlook through Maton's managed Microsoft Graph gateway, including mailbox, calendar, contact, and connection workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a Maton API key connected to Outlook resources, creating exposure if the key is logged, shared, or overly broad.

Mitigation: Keep MATON_API_KEY out of logs and chat output, store it only in the runtime environment, and use narrowly scoped Microsoft permissions where possible.

Risk: Documented operations include sending, moving, deleting, and connection-management actions that can change mailbox, calendar, contact, or OAuth connection state.

Mitigation: Explicitly confirm send, move, delete, and connection-management actions before execution, including the target resource and intended account.

Risk: When multiple Outlook connections exist, omitted connection selection may use an unintended default account.

Mitigation: Specify the intended Outlook connection with the Maton-Connection header whenever more than one active connection may exist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seanford/skills/outlook-api)
- [Microsoft Graph API overview](https://learn.microsoft.com/en-us/graph/api/overview)
- [Microsoft Graph Mail API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview)
- [Microsoft Graph Calendar API](https://learn.microsoft.com/en-us/graph/api/resources/calendar)
- [Microsoft Graph Contacts API](https://learn.microsoft.com/en-us/graph/api/resources/contact)
- [Microsoft Graph query parameters](https://learn.microsoft.com/en-us/graph/query-parameters)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Python, JavaScript, shell, HTTP, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; can produce actions against Outlook resources through Microsoft Graph.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
