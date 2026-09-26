## Description:

Monday.com API integration with managed OAuth for managing boards, items, columns, groups, workspaces, and account context through GraphQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query, create, and update Monday.com boards and items through a Maton-managed OAuth connection. It is also used to build approved hosted functions and trigger-based automations around Monday.com actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read or change Monday.com business data through the connected account.

Mitigation: Use OAuth where possible, keep connections and OAuth scopes narrowly scoped, default to read and list calls, and require explicit approval before mutations or new connections.

Risk: Long-lived API keys or exported credentials can expose account access beyond the intended task.

Mitigation: Prefer Maton OAuth and the operating system credential store; do not read, export, log, or search credential files or environment secrets.

Risk: Hosted functions or triggers can create ongoing access paths to Monday.com data or event payloads.

Mitigation: Create hosted functions and triggers only after user approval, use narrow destinations and body templates, prefer DENY_ALL network policy for Monday.com functions, and remove unused automation.

Risk: Monday.com GraphQL mutations can alter shared boards, items, groups, columns, or workflow state.

Mitigation: Confirm the target resource, payload, and intended effect with the user before each mutation, especially board structure changes or deletes.

## Reference(s):

- [Monday.com API Basics](https://developer.monday.com/api-reference/docs/basics)
- [GraphQL Overview](https://developer.monday.com/api-reference/docs/introduction-to-graphql)
- [Boards Reference](https://developer.monday.com/api-reference/reference/boards)
- [Items Reference](https://developer.monday.com/api-reference/reference/items)
- [Columns Reference](https://developer.monday.com/api-reference/reference/columns)
- [Monday.com API Changelog](https://developer.monday.com/api-reference/changelog)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/monday)
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

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline bash, JSON, and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an approved Monday.com connection; write operations and new connections require explicit user approval.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
