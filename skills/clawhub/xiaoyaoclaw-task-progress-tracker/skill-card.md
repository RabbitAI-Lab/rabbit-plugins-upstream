## Description:

OpenClaw Task Progress Tracker helps an agent maintain local task and project progress cards in workspace tasks/ and projects/ directories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to create, update, review, and close lightweight file-based task or project records. It is intended for multi-step work that benefits from persistent progress logs and document indexes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes and updates local workspace progress files, so mistaken task selection could alter the wrong task or project record.

Mitigation: Confirm the target task or project name before updates, and review the generated PROGRESS.md changes.

Risk: Document attachment may copy, move, or reference files depending on user intent.

Mitigation: Specify whether documents should be copied, moved, or only referenced before asking the agent to attach them.

Risk: Completion actions may write memory notes for later distillation.

Mitigation: Review completion summaries before they are kept as memory material.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-task-progress-tracker)
- [Project Documentation](https://github.com/dtsola/xiaoyaoclaw-task-progress-tracker)
- [OpenClaw Article](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)
- [Task Card Template](artifact/templates/task-card.md)
- [Project Card Template](artifact/templates/project-card.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [Markdown progress files with YAML frontmatter and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates local task, project, document-index, and memory-note files when the user requests progress tracking actions.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
