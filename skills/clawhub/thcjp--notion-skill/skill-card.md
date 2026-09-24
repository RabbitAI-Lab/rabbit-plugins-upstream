## Description:

This skill helps agents work with Notion pages and databases through the official Notion API, including CRUD operations, database queries, content block edits, and Markdown-to-Notion conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and automation users can use this skill to create, query, update, and organize Notion pages, databases, and content blocks from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Notion integration token and can modify Notion pages or databases.

Mitigation: Store the token in NOTION_API_KEY, share the integration only with the exact pages or databases needed, and confirm update or delete operations before execution.

Risk: Server security evidence flags the release as suspicious because it describes command execution and broad file handling beyond its Notion purpose.

Mitigation: Run it in a constrained agent environment, avoid arbitrary shell commands or broad local file paths, and review proposed commands before allowing execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/notion-skill)
- [Notion integrations setup](https://www.notion.so/my-integrations)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request and response examples plus inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require NOTION_API_KEY and target Notion page, database, or block identifiers.]

## Skill Version(s):

1.0.1 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
