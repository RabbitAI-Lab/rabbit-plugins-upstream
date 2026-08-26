## Description:

Guides agents in using the Lexiang knowledge-base MCP integration for searching, reading, writing, editing, uploading files, managing comments and drafts, and working with structured tables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lexiang](https://clawhub.ai/user/lexiang)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and agents use this skill to operate a Lexiang tenant through the configured MCP connector, including knowledge search, content import, page and block edits, file upload, draft publishing, comments, and smartsheet workflows. It is intended for tenant-aware knowledge-base work where the user supplies or confirms the destination for write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent access and modify a Lexiang tenant.

Mitigation: Install it only for users who need Lexiang access, prefer the built-in OAuth connector where available, and protect mcp.json and tokens as secrets.

Risk: Writes, edits, deletes, and uploads can affect the wrong page, space, file, draft, or table if the target is guessed.

Mitigation: Require an explicit URL, ID, personal knowledge-base target, or user-confirmed search result before any write operation.

Risk: Folder sync and bulk upload workflows can upload many local files or exceed practical execution limits.

Mitigation: Use dry-run plans before upload or sync, review the generated plan, and batch larger operations before execution.

Risk: Answering from memory instead of tenant content can produce misleading knowledge-base summaries.

Mitigation: Search or fetch the relevant Lexiang content before summarizing, analyzing, or imitating existing documents.

## Reference(s):

- [Skill entrypoint](artifact/SKILL.md)
- [Artifact README](artifact/README.md)
- [Lexiang MCP setup](https://lexiangla.com/mcp)
- [Lexiang platform](https://lexiangla.com)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [Base rules and safety model](artifact/references/base.md)
- [Setup and authentication](artifact/references/setup.md)
- [Search and browsing](artifact/references/search.md)
- [Writing documents](artifact/references/writer.md)
- [Block editing](artifact/references/blocks.md)
- [File upload management](artifact/references/files.md)
- [Comments](artifact/references/comment.md)
- [Drafts](artifact/references/draft.md)
- [Smartsheets](artifact/references/smartsheet.md)
- [Script helpers](artifact/scripts/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool-call examples, JSON configuration, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include MCP tool arguments, generated links, upload plans, and draft or document content depending on the user request.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
