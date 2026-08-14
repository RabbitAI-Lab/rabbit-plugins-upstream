## Description:

Feishu enables agents to read, create, update, and delete Feishu data through the OOMOL-connected `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to operate a connected Feishu account from an agent, including messages, chats, documents, Drive, wiki, calendar, mail, sheets, slides, approvals, tasks, OKRs, bases, and minutes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Feishu access can read, change, or delete account data when the connected account has permission.

Mitigation: Install only for users who want agent operation of their Feishu account, and review prompts before approving write or destructive actions.

Risk: Destructive operations can remove Feishu records, documents, permissions, calendar events, mail drafts, sheets, slides, wiki nodes, or other workspace data.

Mitigation: Confirm the exact target and payload before running actions tagged destructive.

Risk: Incorrect payloads can update the wrong fields or produce unintended Feishu-side effects.

Mitigation: Fetch the live action schema before building each payload and match the JSON request to that schema.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-feishu)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Feishu](https://www.feishu.cn)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
