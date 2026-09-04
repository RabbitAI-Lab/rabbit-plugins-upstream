## Description:

MindVault is an Agent conversation archiving and thinking-assistance skill that exports chats to JSONL, extracts memory rules, creates project snapshots, and optionally runs the DRAS-V five-step reasoning protocol.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use MindVault to preserve long-running conversations, recover project context across sessions, and convert archived conversations into reusable rules or snapshots. It is especially aimed at agent workflows where local JSONL archives, markdown summaries, and explicit user-triggered memory updates are useful.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversation archives can retain broad chat content, including sensitive personal, proprietary, regulated, or credential-like information.

Mitigation: Review chats before archival where practical, avoid entering secrets in conversations, and protect or delete archive directories when retention is no longer needed.

Risk: The skill can preserve internal reasoning and tool-use context that may expose private project details or decision traces.

Mitigation: Limit use to conversations appropriate for retention, review exported JSONL and Markdown before sharing, and keep archives in access-controlled local storage.

Risk: Local-only and user-control claims may not fully hold in cloud knowledge-base or automation scenarios.

Mitigation: Use explicit user-directed archival by default, and avoid Coze or other cloud knowledge-base modes unless the operator has confirmed what data leaves the device.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhouxin121/skills/mindvault-agent-memory)
- [README](README.md)
- [Deployment Guide and Appreciation Edition Notes](readme1.md)
- [Elite Longterm Memory](https://clawhub.ai/nextfrontierbuilds/elite-longterm-memory)
- [Memory Tiering](https://clawhub.ai/sarielwang93/memory-tiering)
- [Fluid Memory](https://clawhub.ai/againta/fluid-memory)
- [Smart Memory Manager](https://clawhub.ai/ayalili/smart-memory-manager)
- [Memory Qdrant](https://clawhub.ai/zuiho-kai/memory-qdrant)
- [Extended Usage Instructions](https://pay.ldxp.cn/item/p0r2lb)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands; supporting scripts produce JSONL archives, JSON indexes, and Markdown exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local archives are split every 15 rounds and indexed per conversation; the base Markdown converter emits minimal user and agent views.]

## Skill Version(s):

1.0.6 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
