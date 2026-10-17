## Description:

Helps agents search, read, create, and manage content and files in a Tencent Lexiang knowledge base through its MCP integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lexiang](https://clawhub.ai/user/lexiang)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams with access to a Lexiang workspace use this skill to find and read knowledge-base content, create or edit pages, and handle files, comments, drafts, and structured content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad workspace write, delete, revert, and import actions could affect unintended content.

Mitigation: Confirm target space and page IDs before changes; review sensitive content and use small batches for bulk operations.

Risk: Uploads and folder sync could send confidential or personal files to an unintended destination.

Mitigation: Check source paths, destination host, and content sensitivity before uploading or syncing.

Risk: Local configuration access or shared logs could expose credentials.

Mitigation: Do not inspect or quote mcp.json beyond the non-secret company_from value; never expose bearer tokens in chat or logs.

## Reference(s):

- [Lexiang skill release](https://clawhub.ai/lexiang/skills/lexiang-mcp-skill)
- [Lexiang MCP setup](https://lexiangla.com/mcp)
- [Setup and authentication](references/setup.md)
- [Searching and reading](references/search.md)
- [Writing and editing](references/writer.md)
- [File operations](references/files.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance, Shell commands, Code]

**Output Format:** [Markdown with links, code, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide links to Lexiang pages and files.]

## Skill Version(s):

2.2.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
