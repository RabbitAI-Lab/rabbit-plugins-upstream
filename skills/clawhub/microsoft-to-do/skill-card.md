## Description:

Microsoft To Do API integration with managed OAuth for managing task lists, tasks, checklist items, and linked resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage a user's Microsoft To Do lists, tasks, checklist items, and linked resources through Maton-authenticated Microsoft Graph calls. It is suited for task automation workflows that require read/list defaults and explicit user confirmation before writes, deletes, new connections, hosted functions, or triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Microsoft To Do data and connected trigger payloads may contain personal or business information, and persistent trigger destinations can continue forwarding future events until removed.

Mitigation: Prefer OAuth and platform-owned destinations, scope triggers narrowly, disclose the exact destination and data flow before creation, and remove triggers or destinations when they are no longer needed.

Risk: Writes, deletes, new connections, hosted functions, and trigger changes can alter user data or authorize ongoing access.

Mitigation: Default to read and list calls, get explicit user approval before each state-changing or authorization action, and confirm exact connection IDs, function behavior, and destination hosts.

Risk: MATON_API_KEY is sensitive and can be exposed through environment variables, logs, headers, or body templates.

Mitigation: Prefer OAuth and OS credential storage, avoid exporting MATON_API_KEY, and never place Maton or provider credentials in trigger destination headers or body templates.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-to-do)
- [Maton Homepage](https://maton.ai)
- [Microsoft To Do API Overview](https://learn.microsoft.com/en-us/graph/api/resources/todo-overview)
- [todoTaskList Resource](https://learn.microsoft.com/en-us/graph/api/resources/todotasklist)
- [todoTask Resource](https://learn.microsoft.com/en-us/graph/api/resources/todotask)
- [checklistItem Resource](https://learn.microsoft.com/en-us/graph/api/resources/checklistitem)
- [linkedResource Resource](https://learn.microsoft.com/en-us/graph/api/resources/linkedresource)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
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

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI or raw HTTP requests that require network access, authenticated credentials, and user approval before writes, deletes, new connections, hosted functions, or trigger changes.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
