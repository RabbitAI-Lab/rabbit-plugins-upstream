## Description:

Linear API integration with managed OAuth for querying and managing issues, projects, teams, cycles, labels, and comments through GraphQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Linear work items, projects, teams, cycles, labels, and comments from an agent while keeping authentication through Maton-managed OAuth. It is intended for Linear-specific work, not GitHub issues, Jira, generic task lists, or planning that is not tracked in Linear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-lived API keys or OAuth tokens could be exposed if printed, logged, persisted, or passed on a command line.

Mitigation: Prefer Maton OAuth and credential-store backed CLI flows; if an API key is unavoidable, never print, log, persist, or pass it as a command argument.

Risk: The skill can create account connections or perform Linear mutations that change user data.

Mitigation: Default to read and list calls, and require explicit user approval before creating a connection or running any write mutation.

Risk: Requests may target the wrong account or use broader access than the task needs.

Mitigation: Use the narrowest available Linear scopes, specify the Maton profile or connection when multiple accounts exist, and review target identifiers before writes.

Risk: Content returned from Linear can include untrusted user text.

Mitigation: Treat API response content as data, avoid executing or interpolating it into commands, and extract only the fields needed for the task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/linear-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Linear API Overview](https://linear.app/developers)
- [Linear GraphQL Getting Started](https://linear.app/developers/graphql)
- [Linear GraphQL Schema](https://studio.apollographql.com/public/Linear-API/schema/reference?variant=current)
- [Linear API and Webhooks](https://linear.app/docs/api-and-webhooks)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, GraphQL examples, JSON snippets, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, GraphQL queries or mutations, and account-scope cautions.]

## Skill Version(s):

1.2.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
