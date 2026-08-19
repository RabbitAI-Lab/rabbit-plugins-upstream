## Description:

基于 Notion API 创建和管理页面、数据库及内容块，支持属性配置、批量操作和中文交互。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and team workspace users can use this skill to guide Notion API automation for creating pages, querying databases, appending blocks, and configuring structured Notion content. It is intended for Notion workspaces where an integration token has been explicitly granted access to the target pages or databases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security verdict is suspicious because the skill requests broad command execution and Notion mutation authority without clear safeguards.

Mitigation: Review the skill carefully before installing, grant only least-privilege Notion integration access, and avoid enabling shell execution unless a concrete command allowlist is enforced.

Risk: Notion update or delete operations can alter workspace content if the target page or database is shared with the integration.

Mitigation: Require explicit confirmation for destructive operations and verify target page or database identifiers before executing mutations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/notion)
- [Notion Integrations](https://notion.so/my-integrations)
- [Declared Skill Homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Notion API request bodies, operation guidance, configuration steps, and troubleshooting advice.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
