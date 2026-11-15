## Description:

Creates, queries, updates, and appends Notion pages, databases, and blocks through the Notion API with Chinese-language usage guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and productivity teams use this skill to automate Notion workspace tasks such as creating project pages, querying databases, appending structured blocks, and importing CSV or JSON-like data into Notion records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local command execution capability.

Mitigation: Run it only in an agent runtime with command confirmation, sandboxing, and scoped filesystem access.

Risk: The skill can perform real Notion changes such as creating, updating, or appending pages, databases, and blocks.

Mitigation: Require review before destructive or large batch operations and limit the Notion integration token to the minimum pages and databases needed.

Risk: A leaked or over-permissioned Notion integration token could expose workspace content.

Mitigation: Store the token in an environment variable, keep it out of version control, rotate it when needed, and avoid broad page or database sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/notion)
- [Notion integration setup](https://notion.so/my-integrations)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples and shell environment configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Notion API request bodies and structured result examples for page, database, block, and search operations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
