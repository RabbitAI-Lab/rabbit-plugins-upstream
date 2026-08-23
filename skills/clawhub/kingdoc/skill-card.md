## Description:

KingDoc lets an agent create, edit, search, compare, govern, and manage WPS/Kingsoft online documents across document, spreadsheet, presentation, smart canvas, multidimensional table, form, visualization, history, full-text search, and attachment workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document-workflow operators use KingDoc to let an agent generate local document assets, call WPS/Kingsoft document APIs, manage cloud files and permissions, search document content, perform OCR, and support document review workflows. It is intended for online office automation where users can review high-impact actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud collaboration requires local App Secret storage and grants the skill read/write access to WPS/KingDoc documents.

Mitigation: Store the App Secret carefully, restrict permissions on config.json, and avoid running the skill in shared workspaces.

Risk: The skill can perform high-impact document actions, including permanent deletion, sharing links, permission changes, uploads, downloads, notifications, webhooks, and template refreshes.

Mitigation: Require explicit human confirmation before these actions and review the target files, users, links, callbacks, and operation impact before execution.

Risk: Local file-write and document upload behavior can affect user files or cloud documents if invoked with the wrong target.

Mitigation: Review generated files and destination identifiers before upload or overwrite, and use dry-run or confirmation settings for write-heavy workflows.

## Reference(s):

- [KingDoc ClawHub listing](https://clawhub.ai/fyniujin/skills/kingdoc)
- [KDocs Open Platform](https://developer.kdocs.cn)
- [KDocs OpenAPI endpoint reference](https://developer.kdocs.cn/api/v1/openapi)
- [Security design](references/security.md)
- [Authentication reference](references/auth.md)
- [Rate limit and hardware adaptation](references/rate_limit.md)
- [Common workflows](references/workflows.md)
- [Office conversion references](references/office_references.md)
- [Spreadsheet API references](references/et_references.md)
- [Multidimensional table API references](references/dbt_references.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown and text responses with tool-call results, generated document files, local configuration guidance, and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require local configuration for cloud collaboration credentials; local generation, OCR, hardware profiling, and fallback WPS AI behavior can run without cloud keys.]

## Skill Version(s):

3.8.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
