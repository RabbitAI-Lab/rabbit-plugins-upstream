## Description:

Provides SharePoint API access through Microsoft Graph and Maton-managed OAuth for sites, lists, document libraries, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and operations teams use this skill to work with SharePoint sites, lists, document libraries, files, permissions, and approved automations through Microsoft Graph calls. It is suited for document management, list operations, site content review, and user-confirmed SharePoint changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad SharePoint scopes or ambiguous account selection can expose more tenant content than the task requires.

Mitigation: Prefer OAuth with the narrowest available scope, specify the intended connection or profile when more than one exists, and revoke unused connections promptly.

Risk: Write operations, deletions, and sharing-link changes can modify content or widen access to SharePoint files and folders.

Mitigation: Default to read/list calls first, then get explicit user confirmation for the target resource, payload, and intended effect before any POST, PUT, PATCH, DELETE, or sharing-link action.

Risk: API keys, signing secrets, or destination credentials can leak through command-line arguments, environment inheritance, stored destination fields, or logs.

Mitigation: Use Maton OAuth and the OS credential store where possible, avoid placing real secrets directly in commands or templates, and rotate any secret that was entered into a terminal command or log.

Risk: Persistent trigger destinations can continuously forward event payloads to a URL after setup.

Mitigation: Use platform destinations when possible, send only required fields, disclose the destination host and payload fields, and require separate approval for each destination create or update.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/sharepoint)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [SharePoint Sites API](https://learn.microsoft.com/en-us/graph/api/resources/sharepoint)
- [DriveItem API](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [List API](https://learn.microsoft.com/en-us/graph/api/resources/list)
- [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, Python, and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should default to read/list guidance and require explicit user confirmation before writes, sharing-link changes, connection creation, hosted functions, or persistent trigger destinations.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
