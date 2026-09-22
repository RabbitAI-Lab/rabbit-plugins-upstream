## Description:

Helps agents harden OpenClaw cron and background workers with POSIX-focused reliability guardrails for quoting, deterministic working directories and environments, pipeline behavior, and silent-on-success operation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phenomenoner](https://clawhub.ai/user/phenomenoner)

### License/Terms of Use:

MIT

## Use Case:

Developers and automation maintainers use this skill to make OpenClaw cron and background workers more reliable, low-noise, and safe by default. It is suited to execution-wrapper hardening rather than application logic debugging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unattended cron payloads can make unclear, noisy, or destructive changes if the generated job scope is not reviewed.

Mitigation: Review actual cron payloads for clear scope, documented environment variables, rollback behavior, and no destructive actions without explicit approval.

Risk: Cron output may expose secrets or create unnecessary alerts when debug logging is copied into unattended jobs.

Mitigation: Redact secrets by default and keep successful runs silent, using only short actionable failure messages.

## Reference(s):

- [Cron Agent Contract](references/cron-agent-contract.md)
- [Cron exec pitfalls -> safer replacements](references/pitfalls.md)
- [ClawHub skill page](https://clawhub.ai/phenomenoner/skills/cron-worker-guardrails)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces concise hardening checklists and safe execution patterns for unattended jobs.]

## Skill Version(s):

1.0.5 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
