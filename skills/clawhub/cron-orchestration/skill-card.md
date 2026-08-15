## Description:

Defines cron scheduling and mutual-exclusion rules that separate coordinator, team broadcast, and side-collection duties while using five-minute intervals and lock files to prevent concurrent runs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[managernet](https://clawhub.ai/user/managernet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to standardize recurring agent task scheduling, serial execution, notification handoff, lock-file coordination, and repository-visible outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automates recurring agent execution, broad vault reads, external fetches, notifications, and automatic git pushes.

Mitigation: Review before installing in any live vault or repository, and deploy only where those recurring actions and repository writes are intended.

Risk: The evidence identifies unresolved dependency gating, lock cleanup, and overlap with legacy scripts.

Mitigation: Fix or contain dependency waits, lock cleanup, and old-script overlap before using the skill in a live workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/managernet/skills/cron-orchestration)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands]

**Output Format:** [Markdown with scheduling rules, tables, and command references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational constraints for task ordering, lock files, notifications, context isolation, and git push behavior.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
