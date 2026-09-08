## Description:

Monday.com API integration with managed OAuth for managing boards, items, columns, groups, and workspaces through GraphQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query and manage Monday.com boards, items, columns, groups, users, and workspaces through Maton-mediated GraphQL API calls. It supports workflow automation and task management while requiring user approval for account connections and data-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mediate access to a connected Monday.com account.

Mitigation: Use OAuth where possible, authorize only intended accounts and scopes, specify the target connection when multiple accounts exist, and revoke unused connections.

Risk: GraphQL mutations can create, update, or delete Monday.com boards, items, columns, and groups.

Mitigation: Default to read/list calls first and require explicit user confirmation of the target resource, payload, and intended effect before writes or deletions.

Risk: Long-lived Maton API keys can leak through environment variables, logs, command lines, or files when the CLI is unavailable.

Mitigation: Prefer managed OAuth through the Maton CLI, never print or persist API keys, pass keys only through controlled process environments, and rotate any exposed key.

Risk: Content returned from Monday.com may contain untrusted instructions or adversarial data.

Mitigation: Treat API responses as data, avoid executing or interpolating returned content into commands, and validate any values used in follow-up API calls.

## Reference(s):

- [Monday.com API Basics](https://developer.monday.com/api-reference/docs/basics)
- [Monday.com GraphQL Overview](https://developer.monday.com/api-reference/docs/introduction-to-graphql)
- [Monday.com Boards Reference](https://developer.monday.com/api-reference/reference/boards)
- [Monday.com Items Reference](https://developer.monday.com/api-reference/reference/items)
- [Monday.com Columns Reference](https://developer.monday.com/api-reference/reference/columns)
- [Monday.com API Changelog](https://developer.monday.com/api-reference/changelog)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/monday)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes API request examples and safety checks for OAuth connections, account targeting, credential handling, and write confirmations.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
