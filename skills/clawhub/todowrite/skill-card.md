## Description:

Routes TODO checklists to session tasks, persistent files, or shared issues and guides task reporting and synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users use this skill to choose the right home for TODOs, maintain task checklists, and report progress clearly. It also supports managing local task records and explicitly requested shared issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deleting tasks or purging completed records can permanently remove local task history.

Mitigation: Review the target records, preview pruning with a dry run, and confirm before deleting or using --purge.

Risk: Creating issues or Plane records can publish task details to shared systems.

Mitigation: Confirm the destination and contents with the user before creating or posting shared records.

## Reference(s):

- [TodoWrite on ClawHub](https://clawhub.ai/drumrobot/skills/todowrite)
- [Task CLI guide](claude-task.md)
- [Checklist synchronization guide](fix-plan-sync.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files, Shell commands]

**Output Format:** [Text and Markdown checklists, with task commands when appropriate]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local task records and, with user approval, shared issues]

## Skill Version(s):

0.9.4 (source: ClawHub release and CHANGELOG, released 2026-09-30)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
