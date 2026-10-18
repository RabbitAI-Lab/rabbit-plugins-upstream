## Description:

Archives agent conversations locally and helps turn past conversations into reusable rules and project snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT

## Use Case:

People using local agent tools archive conversations for later retrieval, extract recurring preferences into memory rules, and prepare project snapshots to resume work in new sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local plaintext archives may retain sensitive conversations and tool metadata.

Mitigation: Avoid archiving chats containing secrets unless plaintext storage is acceptable; review or delete sensitive archive files.

Risk: Archive files may be placed in an unintended location or synced to cloud storage.

Mitigation: Specify source paths and session IDs explicitly, and keep the archive directory out of cloud sync unless intentional.

## Reference(s):

- [MindVault ClawHub release](https://clawhub.ai/zhouxin121/skills/mindvault)
- [MindVault feature details](https://www.jinengpu.chat/mindvault-detail.html)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Guidance]

**Output Format:** [Local JSONL archives and Markdown memory files, with text guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Archives and memory files remain on the user's local filesystem.]

## Skill Version(s):

1.2.7 (source: server release, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
