## Description:

乐享知识库 MCP 全功能 Skill，用于在 Lexiang knowledge bases 中搜索、读取、写入、编辑、上传文件、管理评论、处理草稿和操作智能表格。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, employees, and knowledge workers use this skill to operate a Lexiang workspace through an agent, including knowledge-base search, content creation, page editing, file upload, folder sync, draft publication, comments, and smart-sheet records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload local files and change or delete live Lexiang knowledge-base data.

Mitigation: Use a least-privilege token and require the agent to show exact targets, files, destinations, and affected records before uploads, syncs, deletes, schema changes, or meeting imports.

Risk: Broad triggers may cause the agent to act on the wrong workspace or knowledge-base target.

Mitigation: Require explicit URLs, IDs, or a user-confirmed target name before write operations, and do not let the agent choose a destination only from browsing workspace lists.

Risk: The inspected SKILL.md hash differs from the attestation hash noted by the security evidence.

Mitigation: Verify publisher identity, package integrity, and release hashes before installation or production use.

Risk: The MCP configuration uses a bearer token for Lexiang workspace access.

Mitigation: Protect the local MCP config, rotate or revoke tokens when access is no longer needed, and stop retries on authorization failures before reauthorizing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/lexiang-knowledge-base)
- [Publisher Profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Reference Index](references/index.md)
- [Lexiang MCP Basics](references/base.md)
- [Setup and Authentication](references/setup.md)
- [File Upload Management](references/files.md)
- [Script Usage](scripts/README.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with MCP tool-call descriptions, JSON examples, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate upload plans, sync plans, Lexiang URLs, MCP call arguments, and user-facing summaries.]

## Skill Version(s):

2.2.0 (source: frontmatter, release evidence, artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
