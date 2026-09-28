## Description:

ClickUp API integration with managed OAuth for accessing ClickUp tasks, lists, folders, spaces, workspaces, users, and webhooks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage ClickUp work items, inspect project hierarchy, and build approved ClickUp automations through Maton-authenticated API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify ClickUp work data through user-authorized connections.

Mitigation: Prefer OAuth, review connected accounts and scopes, default to read/list operations, and require explicit approval before any write or deletion.

Risk: Webhooks, trigger destinations, and hosted functions can keep forwarding data or acting on future events after setup.

Mitigation: Confirm the exact destination, scope, data flow, and persistence before creation; review existing automations and remove any that are no longer needed.

Risk: Raw API responses and webhook payloads can include personal or sensitive work data.

Mitigation: Return only fields needed for the task and avoid logging, storing, or echoing full responses unless the user explicitly requests it.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/clickup-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClickUp API Overview](https://developer.clickup.com/docs/Getting%20Started.md)
- [ClickUp Get Tasks](https://developer.clickup.com/reference/gettasks.md)
- [ClickUp Create Task](https://developer.clickup.com/reference/createtask.md)
- [ClickUp Update Task](https://developer.clickup.com/reference/updatetask.md)
- [ClickUp Delete Task](https://developer.clickup.com/reference/deletetask.md)
- [ClickUp Create Webhook](https://developer.clickup.com/reference/createwebhook.md)
- [ClickUp Rate Limits](https://developer.clickup.com/docs/rate-limits.md)
- [Calendly Trigger Reference](artifact/references/calendly/triggers.md)
- [GitHub Trigger Reference](artifact/references/github/triggers.md)
- [Gmail Trigger Reference](artifact/references/google-mail/triggers.md)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Linear Trigger Reference](artifact/references/linear/triggers.md)
- [Notion Trigger Reference](artifact/references/notion/triggers.md)
- [Slack Trigger Reference](artifact/references/slack/triggers.md)
- [Stripe Trigger Reference](artifact/references/stripe/triggers.md)
- [Time Trigger Reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should favor read/list calls first, require explicit user approval for writes, and avoid exposing raw credentials or unnecessary response data.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
