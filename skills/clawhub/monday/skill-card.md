## Description:

Monday.com API integration with managed OAuth for managing boards, items, columns, groups, and workspaces using GraphQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to query and manage Monday.com workspace objects through Maton-managed OAuth. It supports read-first workflows and confirmed changes for boards, items, columns, groups, users, and workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Monday.com account may allow reads and changes to workspace data.

Mitigation: Use OAuth where possible, choose the narrowest available Monday.com scopes, default to read/list calls, and require explicit confirmation for write or delete operations.

Risk: Generic pass-through HTTP instructions broaden what an agent may try beyond the documented GraphQL workflow.

Mitigation: Prefer the documented Maton CLI GraphQL calls to /monday/v2 and use raw HTTP only when the CLI cannot be installed.

Risk: Multiple Maton or Monday.com connections can cause actions to land in the wrong account or workspace.

Mitigation: Specify the intended Maton profile and connection before any operation with side effects.

Risk: Long-lived API keys and provider tokens can leak through logs, command lines, files, or shell history.

Mitigation: Prefer OAuth-backed CLI credential storage, never print or persist credentials, and rotate any key that was exposed.

## Reference(s):

- [ClawHub Monday.com Skill](https://clawhub.ai/byungkyu/skills/monday)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Monday.com API Basics](https://developer.monday.com/api-reference/docs/basics)
- [Monday.com GraphQL Overview](https://developer.monday.com/api-reference/docs/introduction-to-graphql)
- [Monday.com Boards Reference](https://developer.monday.com/api-reference/reference/boards)
- [Monday.com Items Reference](https://developer.monday.com/api-reference/reference/items)
- [Monday.com Columns Reference](https://developer.monday.com/api-reference/reference/columns)
- [Monday.com API Changelog](https://developer.monday.com/api-reference/changelog)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with inline bash, GraphQL, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes Maton CLI and SDK examples; write, delete, connection, and raw HTTP operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release evidence; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
