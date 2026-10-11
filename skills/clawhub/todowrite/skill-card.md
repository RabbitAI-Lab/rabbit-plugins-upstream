## Description:

Routes TODO checklists to session tasks, persistent files, or shared issues and guides task reporting and synchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users use this skill to route tasks to the appropriate tracking medium, maintain checklists, and report progress consistently.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The completion-report rule may create an external Plane issue without separate approval when no shareable resource URL exists.

Mitigation: Disable or amend that rule before using authenticated tools unless automatic Plane issue creation is acceptable.

Risk: The task CLI can permanently delete task records through delete or prune --purge.

Mitigation: Review targets and use prune --dry-run or the default archive mode before cleanup; avoid purge unless permanent deletion is intended.

## Reference(s):

- [TodoWrite on ClawHub](https://clawhub.ai/drumrobot/skills/todowrite)
- [Task CLI guide](claude-task.md)
- [Task and checklist synchronization guide](fix-plan-sync.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with checklist examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update persistent task records.]

## Skill Version(s):

0.10.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
