## Description:

Helps agents search, read, create, and manage Tencent Lexiang knowledge-base content, including documents, files, drafts, and smart tables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lexiang](https://clawhub.ai/user/lexiang)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to find information in a Lexiang knowledge base and, when authorized, create or update documents, files, drafts, and smart tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local connection credentials could be exposed.

Mitigation: Keep tokens private and prefer connector or OAuth setup where available.

Risk: Uploads could disclose unintended local files.

Mitigation: Upload only explicitly selected files or narrow folders after checking the destination.

Risk: Remote writes, deletes, or rollbacks could change or remove knowledge-base content.

Mitigation: Confirm each write, delete, or rollback before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/lexiang/skills/lexiang-mcp-skill)
- [Lexiang MCP setup](https://lexiangla.com/mcp)
- [Connection and authentication guide](artifact/references/setup.md)
- [Search and reading guide](artifact/references/search.md)
- [Writing guide](artifact/references/writer.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions]

**Output Format:** [Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to retrieved or changed knowledge-base items.]

## Skill Version(s):

2.2.1 (source: ClawHub release metadata; bundled SKILL.md says 2.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
