## Description:

Asana API integration with managed OAuth for accessing tasks, projects, workspaces, users, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to let an agent list or manage Asana work items, projects, workspaces, users, and approved webhooks through a Maton-authenticated Asana connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the integration grants Maton access to the selected Asana account and the data allowed by that connection.

Mitigation: Prefer OAuth, use the least privilege scopes and accounts available for the task, and revoke unused connections.

Risk: Write operations, webhooks, functions, and triggers can change Asana state or create ongoing automation.

Mitigation: Confirm the target resource, payload, destination, and intended effect with the user before each modifying or automation action.

Risk: Webhooks and trigger destinations can persistently forward future work data to another host.

Mitigation: Use only destinations the user explicitly names and approves, avoid unscoped cross-app forwarding, and delete destinations that are no longer needed.

Risk: Long-lived API keys and raw API responses can expose account or business data if copied into environments, logs, or files.

Mitigation: Prefer OAuth over API keys, avoid exporting MATON_API_KEY when possible, and extract only task-relevant response fields.

## Reference(s):

- [Asana skill on ClawHub](https://clawhub.ai/byungkyu/skills/asana-api)
- [Maton homepage](https://maton.ai)
- [Asana API Documentation](https://developers.asana.com)
- [Asana API Reference](https://developers.asana.com/reference)
- [Asana Tasks API](https://developers.asana.com/reference/tasks)
- [Asana Projects API](https://developers.asana.com/reference/projects)
- [Asana Workspaces API](https://developers.asana.com/reference/workspaces)
- [Asana Webhooks API](https://developers.asana.com/reference/webhooks)
- [Asana LLM Reference](https://developers.asana.com/llms.txt)
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

**Output Format:** [Markdown guidance with CLI commands, JSON examples, and small code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides authenticated Asana API calls and requires user approval before new connections, writes, webhooks, functions, triggers, or persistent destinations.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
