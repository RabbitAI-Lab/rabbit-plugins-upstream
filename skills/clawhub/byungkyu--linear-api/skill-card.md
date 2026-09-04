## Description:

Linear API integration with managed OAuth for querying and managing issues, projects, teams, cycles, labels, comments, and related workspace data through GraphQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and manage Linear workspace data through Maton-managed OAuth. It supports read/list workflows by default and requires explicit user approval for new connections or write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Linear workspace data through Maton/OAuth.

Mitigation: Install only when Linear access through Maton is intended, prefer OAuth, and connect only the account required for the task.

Risk: Write operations can modify Linear issues, comments, projects, teams, cycles, labels, or related workspace data.

Mitigation: Use read/list calls first, then require explicit user confirmation of the target resource, payload, and intended effect before any write operation.

Risk: Multiple Maton profiles or Linear connections can send requests to the wrong account.

Mitigation: Pin the intended profile and connection when more than one account or connection exists.

Risk: Raw API-key fallback increases credential handling exposure.

Mitigation: Avoid the API-key fallback unless the CLI cannot be used, and never print, log, persist, or pass credentials through command-line arguments.

## Reference(s):

- [ClawHub Linear Skill](https://clawhub.ai/byungkyu/skills/linear-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Linear API Overview](https://linear.app/developers)
- [Linear GraphQL Getting Started](https://linear.app/developers/graphql)
- [Linear GraphQL Schema](https://studio.apollographql.com/public/Linear-API/schema/reference?variant=current)
- [Linear API and Webhooks](https://linear.app/docs/api-and-webhooks)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, GraphQL examples, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an active Linear connection.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
