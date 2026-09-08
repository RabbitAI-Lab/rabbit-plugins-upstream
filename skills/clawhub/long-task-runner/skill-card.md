## Description:

Run slow local commands and queues with disk-backed state, bounded logs, timeouts, cancellation, safe recovery, and artifact checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dhzyw](https://clawhub.ai/user/dhzyw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to run long local jobs, monitor bounded status and logs, coordinate resource locks, cancel or safely resume approved work, and verify artifacts before final review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trusted job specs can launch local child commands that read inherited environment variables and write with normal local permissions.

Mitigation: Inspect job JSON and command arguments before execution, use only trusted workloads, and run jobs from an appropriate working directory with least necessary local access.

Risk: Secrets placed directly in job JSON or command-line URLs may be persisted in frozen specs, state, or logs.

Mitigation: Keep credentials out of job JSON and URLs; use existing environment or tool credential mechanisms and read bounded logs only when needed.

Risk: External or paid jobs can be duplicated if retried or resumed without a confirmed idempotency boundary.

Mitigation: Treat external submissions as non-replayable, track only already-submitted remote job IDs with read-only watchers, and require human review before any new submission.

## Reference(s):

- [Long Task Runner ClawHub Page](https://clawhub.ai/dhzyw/skills/long-task-runner)
- [Skill Instructions](SKILL.md)
- [README](README.md)
- [Job Specification](references/job-spec.md)
- [Scenario Guidance](references/scenarios.md)
- [Host Waiting Boundaries](references/host-waiting.md)
- [Optional Compression Guidance](references/optional-compression.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with JSON configuration and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces bounded status snapshots, failure identifiers, and log excerpts for agent review.]

## Skill Version(s):

1.0.0 (source: release metadata and runner.py VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
