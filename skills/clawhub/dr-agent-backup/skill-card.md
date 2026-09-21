## Description:

Repair or set up six-hour real workspace backups with immediate failure notification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daniel-refahi-ikara](https://clawhub.ai/user/daniel-refahi-ikara)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to set up, audit, repair, or restore deterministic backups for a Daniel-owned agent workspace. It focuses on preserving durable memory and configuration through scheduled git commits, pushes, health checks, and failure notification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring backup jobs can commit and push selected workspace files to a remote repository.

Mitigation: Confirm the intended remote, branch, credential method, allowlist, and exclude list before enabling the scheduler.

Risk: Backup credentials or sensitive runtime files could be exposed if included in tracked paths.

Mitigation: Store credentials outside git and verify that env files, local auth profiles, caches, databases, logs, media dumps, and generated transcripts remain excluded.

Risk: A failed backup commit, push, scheduler, or notification route can silently weaken restore continuity.

Mitigation: Use a deterministic scheduler, non-zero runner exits on failure, immediate failure notification, and periodic health checks for stale or missing backups.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/daniel-refahi-ikara/skills/dr-agent-backup)
- [Publisher profile](https://clawhub.ai/user/daniel-refahi-ikara)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with checklists and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is intended for agent execution and review before enabling scheduled backups or notifications.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
