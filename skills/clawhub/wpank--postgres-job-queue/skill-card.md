## Description:

PostgreSQL-based job queue with priority scheduling, batch claiming, and progress tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wpank](https://clawhub.ai/user/wpank)

### License/Terms of Use:


## Use Case:

Developers and engineers use this skill to design PostgreSQL-backed background job queues with priority scheduling, concurrent batch claiming, progress tracking, retries, and stale job recovery when they want to avoid external queue infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented primary install path uses an unpinned remote npx/GitHub installer.

Mitigation: Review the install path before installing and prefer a manual per-project copy or an immutable pinned release or commit.

Risk: Global installation makes the skill available across projects.

Mitigation: Install per project when possible and review the skill before deployment in each target workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wpank/skills/postgres-job-queue)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with SQL, Go, and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes schema design, batch-claim SQL, Go queue routines, installation commands, and operational decision guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
