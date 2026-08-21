## Description:

通过官方 getnote CLI 连接得到大脑，完成浏览器授权、连接诊断、CLI 升级，以及保存、查询、搜索、整理和管理用户的真实笔记。

This skill is ready for commercial/non-commercial use.

## Publisher:

[iswalle](https://clawhub.ai/user/iswalle)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to let an agent operate their own GetNote/得到大脑 account through the official getnote CLI, including authentication, diagnostics, note capture, search, knowledge-base organization, subscriptions, and tag management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized CLI actions can change remote GetNote account data, including saves, updates, archives, shares, deletes, tag replacement, folder removals, subscriptions, and updates.

Mitigation: Require explicit user approval for destructive, public, replacement, subscription, folder-removal, and update actions, then verify the final server state with getnote JSON results before reporting success.

Risk: Authentication or private note content could be exposed if handled directly in chat.

Mitigation: Use browser-based getnote CLI authorization, never request or display API keys, cookies, or Authorization values, and avoid expanding private full text in shared contexts unless the user explicitly requests it.

Risk: Asynchronous saves, network failures, or partial command results can leave write outcomes uncertain.

Mitigation: Check exit codes and success fields, poll task IDs to final status, preserve request IDs on failure, and query existing results before retrying writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iswalle/skills/getnote)
- [Skill instructions](artifact/SKILL.md)
- [Authentication, diagnostics, and updates](artifact/references/auth.md)
- [Notes](artifact/references/note.md)
- [Search](artifact/references/search.md)
- [Knowledge bases](artifact/references/kb.md)
- [Tags](artifact/references/tag.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with inline shell commands and JSON-derived command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include real note titles, note IDs, note URLs, summaries, status messages, confirmation prompts, and request IDs.]

## Skill Version(s):

2.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
