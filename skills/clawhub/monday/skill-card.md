## Description:

Monday.com API integration with managed OAuth for managing boards, items, columns, groups, users, and workspaces using GraphQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query, create, update, and delete Monday.com boards, items, columns, groups, users, and workspaces through Maton's managed OAuth gateway. It is suited for task management and workflow automation where the agent must confirm write actions and target resources with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Monday.com workspace data through Maton.

Mitigation: Prefer read/list calls first and require explicit user confirmation with exact resource IDs, payloads, and intended effects before create, update, or delete operations.

Risk: OAuth connections and API keys can grant access to Monday.com account data.

Mitigation: Prefer OAuth, select the narrowest available scopes, keep credentials in the CLI or operating system credential store, and avoid printing, logging, or persisting tokens.

Risk: Using the wrong connection or profile could apply changes to the wrong Monday.com account.

Mitigation: Specify the target connection and Maton profile when multiple accounts are available, and avoid deleting a connection unless the target has been confirmed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/monday)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Monday.com API Basics](https://developer.monday.com/api-reference/docs/basics)
- [Monday.com GraphQL Overview](https://developer.monday.com/api-reference/docs/introduction-to-graphql)
- [Monday.com Boards Reference](https://developer.monday.com/api-reference/reference/boards)
- [Monday.com Items Reference](https://developer.monday.com/api-reference/reference/items)
- [Monday.com Columns Reference](https://developer.monday.com/api-reference/reference/columns)
- [Monday.com API Changelog](https://developer.monday.com/api-reference/changelog)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions, Code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK examples for Monday.com GraphQL operations; write operations require explicit user confirmation.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
