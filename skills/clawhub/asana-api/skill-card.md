## Description:

Asana API integration with managed OAuth for accessing tasks, projects, workspaces, users, and webhooks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external operators, and developers use this skill to manage Asana work items, track projects, inspect workspaces and users, and create approved Asana automation through Maton connections, functions, and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Asana OAuth or API-key access can expose business data available to the connected account.

Mitigation: Prefer OAuth, select the narrowest Asana scopes available, and use only the connection required for the current task.

Risk: Write, delete, webhook, function, or trigger actions can change Asana state or create persistent automation.

Mitigation: Confirm the exact action, target, connection, and scope with the user before execution; default to read and list operations.

Risk: Persistent webhooks or triggers can continue forwarding business data after setup.

Mitigation: Create them only after explicit approval, document the destination, and remove them when the automation is no longer needed.

## Reference(s):

- [ClawHub Asana skill page](https://clawhub.ai/byungkyu/skills/asana-api)
- [Maton homepage](https://maton.ai)
- [Asana API Documentation](https://developers.asana.com)
- [Asana API Reference](https://developers.asana.com/reference)
- [Tasks API](https://developers.asana.com/reference/tasks)
- [Projects API](https://developers.asana.com/reference/projects)
- [Workspaces API](https://developers.asana.com/reference/workspaces)
- [Webhooks API](https://developers.asana.com/reference/webhooks)
- [Asana LLM Reference](https://developers.asana.com/llms.txt)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly trigger catalog](references/calendly/triggers.md)
- [GitHub trigger catalog](references/github/triggers.md)
- [Gmail trigger catalog](references/google-mail/triggers.md)
- [HubSpot trigger catalog](references/hubspot/triggers.md)
- [Linear trigger catalog](references/linear/triggers.md)
- [Notion trigger catalog](references/notion/triggers.md)
- [Slack trigger catalog](references/slack/triggers.md)
- [Stripe trigger catalog](references/stripe/triggers.md)
- [Time trigger catalog](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-reviewed Maton CLI or HTTP actions that can call Asana APIs through the user's authorized connection.]

## Skill Version(s):

1.2.4 (source: server release metadata; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
