## Description:

Move a running service to another server: inventory, rehearsal, cutover runbook with measured downtime, rollback paths, and observation before the old copy is retired.

This skill is ready for commercial/non-commercial use.

## Publisher:

[holgergruenhagen](https://clawhub.ai/user/holgergruenhagen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and service operators use this skill to plan and rehearse moving one running service, its data, and scheduled jobs to another server. It prepares a measured cutover and rollback runbook while keeping production changes under the owner's step-by-step control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An environment inventory command may expose credential values in some cases.

Mitigation: Review the command before use and do not share or paste its output until it is corrected or confirmed to contain no secrets.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Analysis, Shell commands, Configuration instructions]

**Output Format:** [Markdown with checklists, tables, runbooks, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tailored to one owner-named service and its old and new servers; includes read-only checks, approval-gated active steps, measured downtime, and rollback paths.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
