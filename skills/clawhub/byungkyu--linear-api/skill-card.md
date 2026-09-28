## Description:

Linear API integration with managed OAuth for querying and managing Linear issues, projects, teams, cycles, labels, and comments through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to inspect and update Linear work items, manage Linear OAuth connections, and configure approved Linear automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Linear workspace data through a Maton-authenticated connection.

Mitigation: Prefer OAuth, connect only needed accounts and scopes, and confirm new connections before authorization.

Risk: Linear mutations and automation setup can change records or create ongoing workflows.

Mitigation: Default to read/list calls, verify target resources first, and require explicit approval for writes, function deployment, triggers, and persistent destinations.

Risk: API keys and trigger destinations can expose credentials or business data if mishandled.

Mitigation: Avoid long-lived API keys when OAuth is available, never print credentials, keep destinations on trusted hosts, and scope triggers narrowly.

## Reference(s):

- [ClawHub Linear skill](https://clawhub.ai/byungkyu/skills/linear-api)
- [Maton homepage](https://maton.ai)
- [Linear trigger reference](references/linear/triggers.md)
- [Linear API Overview](https://linear.app/developers)
- [Linear GraphQL Getting Started](https://linear.app/developers/graphql)
- [Linear GraphQL Schema](https://studio.apollographql.com/public/Linear-API/schema/reference?variant=current)
- [Linear API and Webhooks](https://linear.app/docs/api-and-webhooks)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with shell, JSON, GraphQL, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Linear connection; defaults to read/list calls and requires approval for writes, connections, and automation.]

## Skill Version(s):

1.2.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
