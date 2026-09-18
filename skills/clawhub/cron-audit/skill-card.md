## Description:

cron-audit audits OpenClaw cron jobs for silent failure modes, including broken delivery routes, undelivered alerts, missing failure alerts, overdue schedules, and jobs that never ran.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cprite](https://clawhub.ai/user/cprite)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw operators use this skill to inspect scheduled jobs, troubleshoot cron jobs that appear silent, and review delivery and failure-alert configuration before re-enabling old jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The opt-in --heal mode can change live OpenClaw cron delivery and failure-alert settings.

Mitigation: Use --full or --json for read-only checks first, and only allow --heal after reviewing the route and alert configuration.

Risk: Automatic route repair may send a job to an agent default route that is a safe landing location but not the intended final thread.

Mitigation: Review healed jobs and re-point them to the right destination after repair.

## Reference(s):

- [cron-audit source repository](https://github.com/cprite/cron-audit)
- [cron-audit ClawHub page](https://clawhub.ai/cprite/skills/cron-audit)
- [OpenClaw project](https://github.com/openclaw/openclaw)
- [cron-routes.example.json](references/cron-routes.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, JSON findings, and shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; opt-in --heal can edit live OpenClaw cron jobs.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
