## Description:

Linear API integration with managed OAuth for querying and managing issues, projects, teams, cycles, labels, and comments using GraphQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query and manage Linear work items through a user-approved Maton connection. It is suited for Linear issue, project, team, cycle, label, comment, and automation workflows that the user explicitly requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive Linear issue data through OAuth or API-key-backed Maton connections.

Mitigation: Approve only the Linear account and scopes needed for the task, prefer OAuth over long-lived API keys, and avoid exposing raw responses unless the user asks for them.

Risk: Linear mutations and hosted automations can change business records or create ongoing actions.

Mitigation: Confirm every mutation, new connection, function, trigger, destination, and replay before it runs, including the target resource, payload, and intended effect.

Risk: Trigger destinations can forward Linear event payloads containing personal data and confidential issue content.

Mitigation: Scope triggers narrowly, forward only required fields, avoid unapproved third-party destinations, and do not log payloads verbatim.

## Reference(s):

- [Linear API Overview](https://linear.app/developers)
- [Linear GraphQL Getting Started](https://linear.app/developers/graphql)
- [Linear GraphQL Schema](https://studio.apollographql.com/public/Linear-API/schema/reference?variant=current)
- [Linear API and Webhooks](https://linear.app/docs/api-and-webhooks)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Linear Trigger Reference](references/linear/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with CLI commands, GraphQL examples, JSON snippets, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May perform authenticated Linear API calls through Maton when the user has approved the connection, mutation, or automation.]

## Skill Version(s):

1.2.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
