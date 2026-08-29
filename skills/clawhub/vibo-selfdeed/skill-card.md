## Description:

ViBo SelfDeed helps an agent run an explicitly delegated multi-step mission by clarifying intent, restoring local ViBo memory, scanning a scoped workspace, proposing fixes, applying confirmed changes with backups, iterating toward a target, saving lessons, and reporting results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

ViBo EULA commercial terms; MIT-0 for hosted showcase copy

## Use Case:

Developers and technical users use this skill when they explicitly delegate a concrete multi-step task, such as finding and fixing project issues, reviewing documentation, or checking configuration consistency. The skill structures the mission through clarification, scoped scanning, proposed changes, backups, iteration, memory updates, and a final report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to change files in a project workspace.

Mitigation: Run it only in a tightly scoped workspace, review proposed diffs before fixes, and rely on backups or version control before applying changes.

Risk: Using --auto can apply changes without per-fix confirmation.

Mitigation: Avoid --auto for sensitive repositories and use the normal confirmation flow when changes affect important code or data.

Risk: Mission memory and checkpoints can persist task details locally.

Mitigation: Tell users what will be stored before starting, avoid directories containing secrets, and delete mission state, backups, or memory records when retention is no longer desired.

Risk: Optional Telegram controls can send mission details to an external chat service.

Mitigation: Enable Telegram only when the user accepts that mission details may be sent to the configured chat and service.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/vnbochkarev-netizen/skills/vibo-selfdeed)
- [Publisher profile](https://clawhub.ai/user/vnbochkarev-netizen)
- [ViBo Memory website](https://wwwvibo.com)
- [Artifact README](artifact/README.md)
- [Artifact install guide](artifact/INSTALL.md)
- [Artifact examples](artifact/examples/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown status summaries, plan cards, shell commands, diffs or code edits, checkpoint data, and final mission reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local mission state, backups, and memory records inside the scoped mission workspace when used by an agent.]

## Skill Version(s):

1.0.11 (source: server release evidence and SKILL.md frontmatter; package.json reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
