## Description:

通过官方 getnote CLI 连接得到大脑，完成浏览器授权、连接诊断、CLI 升级，以及保存、查询、搜索、整理和管理用户的真实笔记。

This skill is ready for commercial/non-commercial use.

## Publisher:

[iswalle](https://clawhub.ai/user/iswalle)

### License/Terms of Use:

MIT

## Use Case:

External users use this skill to let an AI agent operate the official GetNote CLI for connecting an account, diagnosing access, saving notes, searching existing notes, organizing knowledge bases and folders, subscribing to sources, and managing tags.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can let an agent read or modify data in the user's authorized GetNote account.

Mitigation: Install only when account operation is intended, complete authorization in the browser, and review confirmations before write operations.

Risk: Deletion, public sharing, tag replacement, and bulk organization changes may have broad effects on user content.

Mitigation: Require explicit confirmation for sensitive actions and verify final state through the CLI before reporting success.

Risk: Local CLI authorization stores credentials on the user's machine.

Mitigation: Do not request or display API keys, cookies, Authorization headers, or complete credentials in chat.

## Reference(s):

- [得到大脑连接、诊断与升级](references/auth.md)
- [得到大脑笔记](references/note.md)
- [得到大脑搜索](references/search.md)
- [得到大脑知识库](references/kb.md)
- [得到大脑标签](references/tag.md)
- [ClawHub skill page](https://clawhub.ai/iswalle/skills/getnote)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline CLI commands and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include real note titles, string IDs, links, summaries, diagnostics, error codes, and request IDs returned by the GetNote CLI.]

## Skill Version(s):

2.0.4 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
