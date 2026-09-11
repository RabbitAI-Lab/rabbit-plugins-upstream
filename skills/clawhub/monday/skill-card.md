## Description:

Monday.com API integration with managed OAuth for managing boards, items, columns, groups, and workspaces using GraphQL, and reading account context through the `me` and `users` queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query and manage Monday.com boards, items, columns, groups, users, and workspaces through Maton-managed OAuth/API access. It is intended for workflow automation and task management operations where reads are preferred by default and writes require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Monday.com mutations can create, change, delete, notify, share, or create webhooks in a connected workspace.

Mitigation: Review each mutation carefully and confirm the target account, resource, payload, and intended effect with the user before execution.

Risk: Long-lived API keys or exposed credentials could grant access to Monday.com or Maton resources.

Mitigation: Prefer OAuth, avoid printing or storing credentials, and install only from official Maton package locations.

Risk: Multiple Maton accounts or Monday.com connections can make the target workspace ambiguous.

Mitigation: Confirm the exact Monday.com account or connection before use and specify the intended connection when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/monday)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Monday.com API Basics](https://developer.monday.com/api-reference/docs/basics)
- [Monday.com GraphQL Overview](https://developer.monday.com/api-reference/docs/introduction-to-graphql)
- [Monday.com Boards Reference](https://developer.monday.com/api-reference/reference/boards)
- [Monday.com Items Reference](https://developer.monday.com/api-reference/reference/items)
- [Monday.com Columns Reference](https://developer.monday.com/api-reference/reference/columns)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include GraphQL query or mutation bodies for Monday.com API calls through Maton.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
