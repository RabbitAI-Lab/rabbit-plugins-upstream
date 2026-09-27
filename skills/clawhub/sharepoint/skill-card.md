## Description:

SharePoint API integration via Microsoft Graph with managed OAuth for accessing SharePoint sites, lists, document libraries, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users use this skill to work with SharePoint content through Microsoft Graph, including reading sites, lists, libraries, files, permissions, versions, and selected write operations. It also guides approved SharePoint automation through Maton connections, hosted functions, and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SharePoint actions can read or modify business data through the user's authorized connection.

Mitigation: Default to read and list calls, request explicit user approval before POST, PUT, PATCH, DELETE, new connections, sharing links, hosted functions, triggers, or destinations, and use the narrowest SharePoint scope available.

Risk: Long-lived API keys and raw response bodies can expose credentials or sensitive SharePoint content.

Mitigation: Prefer OAuth, store credentials through the Maton credential store, avoid exporting MATON_API_KEY except where the CLI cannot be installed, and extract only task-required response fields instead of logging or saving full payloads.

Risk: Hosted functions and triggers can create ongoing automation that forwards data without repeated review.

Mitigation: Use user-authored or user-reviewed handlers, deploy SharePoint functions with DENY_ALL network policy by default, prefer Maton destinations, minimize trigger payloads with body templates, and delete unused connections, functions, triggers, and destinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/sharepoint)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [SharePoint Sites API](https://learn.microsoft.com/en-us/graph/api/resources/sharepoint)
- [DriveItem API](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [List API](https://learn.microsoft.com/en-us/graph/api/resources/list)
- [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
- [Time Trigger Reference](references/time/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration instructions]

**Output Format:** [Markdown with inline bash, JSON, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton CLI or raw HTTP examples and recommends OAuth, least-privilege scopes, and explicit approval for writes, connections, functions, triggers, and destinations.]

## Skill Version(s):

1.2.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
