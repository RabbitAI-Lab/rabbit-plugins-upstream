## Description:

MindVault archives agent conversations, extracts reusable memory rules, creates project snapshots, and provides an optional DRAS-V thinking protocol for long-running agent work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhouxin121](https://clawhub.ai/user/zhouxin121)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use MindVault to preserve local conversation archives, extract reusable memory rules, and restore project context across new sessions in OpenClaw, Marvis, CherryStudio, Coze, and related agent environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently stores conversation history, which may include credentials, regulated data, or sensitive project context.

Mitigation: Use scoped project directories, avoid entering secrets or regulated data, and review archive and derived memory files before reuse or sharing.

Risk: The security review notes that local-only privacy claims conflict with documented support for cloud-connected platforms and paid automation/reporting workflows.

Mitigation: Confirm each platform's data flow before deployment, especially Coze and any paid automation or reporting workflow.

Risk: The artifact includes local scripts that read and write archive, index, memory, and export files; one optional Markdown/HTML export path references an undeclared CLI option.

Mitigation: Run scripts only on trusted local archives, back up data before mutation, and test export commands in a disposable directory before using them on important history.

## Reference(s):

- [MindVault ClawHub release page](https://clawhub.ai/zhouxin121/skills/mindvault-agent-memory)
- [Publisher profile](https://clawhub.ai/user/zhouxin121)
- [Paid deployment documentation](https://pay.ldxp.cn/item/p0r2lb)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with Python CLI commands and generated JSONL/Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local archive files, memory/FACT.md, PROJECT_SNAPSHOT.md, PROJECT.md, and Markdown exports when invoked by the user.]

## Skill Version(s):

1.0.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
