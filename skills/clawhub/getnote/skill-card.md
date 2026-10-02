## Description:

Connects an agent to 得到大脑 through the official getnote CLI for browser authorization, connection diagnostics, CLI updates, and real note saving, search, retrieval, and organization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iswalle](https://clawhub.ai/user/iswalle)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub/OpenClaw users use this skill to let an agent operate their authorized 得到大脑 account through the official getnote CLI. It supports connection setup, diagnostics, upgrades, note capture, search, detail reading, knowledge-base organization, file upload workflows, blogger or live subscriptions, and tag management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and manage data in the user's authorized GetNote account through the official getnote CLI.

Mitigation: Install and use it only when account access is intended; rely on browser authorization and do not request or expose API keys, cookies, Authorization headers, or full credentials in chat.

Risk: Deletes, overwrites, public sharing, uploads, setup, update, and similar operations can change remote notes or local CLI state.

Mitigation: Review prompts carefully and require explicit user confirmation for destructive, public, overwrite, bulk removal, upload, setup, and update actions.

Risk: Asynchronous saves, uploads, and uncertain write results can otherwise be mistaken for completed work.

Mitigation: Check command exit status, success fields, returned note IDs or URLs, and follow-up reads before reporting completion; preserve request IDs and real error reasons when operations fail.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iswalle/skills/getnote)
- [得到大脑连接、诊断与升级](references/auth.md)
- [得到大脑笔记](references/note.md)
- [得到大脑搜索](references/search.md)
- [得到大脑知识库](references/kb.md)
- [得到大脑标签](references/tag.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown]

**Output Format:** [Markdown guidance with getnote CLI command patterns and JSON result checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the getnote CLI and an authorized user account for live account operations.]

## Skill Version(s):

2.1.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
