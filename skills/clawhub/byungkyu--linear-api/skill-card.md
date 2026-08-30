## Description:

Linear API integration with managed OAuth for querying and managing issues, projects, teams, cycles, labels, and comments through the Maton CLI or GraphQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and manage Linear work items, projects, teams, cycles, labels, and comments from a connected Linear workspace. It is best suited for task tracking workflows that need read-first API access with explicit approval before connection creation or writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can grant Maton-mediated access to a Linear workspace.

Mitigation: Prefer OAuth through the Maton CLI, confirm connection creation with the user, and use least-privilege scopes where Linear offers scope selection.

Risk: Write operations can create, update, delete, or comment on Linear records.

Mitigation: Default to read and list calls, verify identifiers and account context first, and require explicit user approval before any write or connection-changing action.

Risk: Multiple Maton accounts or Linear connections can send actions to the wrong workspace.

Mitigation: Specify the intended profile or connection when more than one exists, especially before write operations.

Risk: Using the raw API key fallback can expose a long-lived credential.

Mitigation: Avoid the raw MATON_API_KEY path unless the CLI cannot be used, never print or log the key, and send it only to api.maton.ai.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/linear-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Linear API Overview](https://linear.app/developers)
- [Linear GraphQL Getting Started](https://linear.app/developers/graphql)
- [Linear GraphQL Schema](https://studio.apollographql.com/public/Linear-API/schema/reference?variant=current)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and GraphQL snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for Maton CLI, SDK, and GraphQL API usage; network access and an authenticated Maton account are required.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
