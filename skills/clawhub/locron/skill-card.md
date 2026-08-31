## Description:

Safely create, preview, inspect, run, update, remove, import, export, explain, diagnose, and manage the local dashboard for schedules managed by the Locron local-first job scheduler.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitekiwi](https://clawhub.ai/user/whitekiwi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and power users use this skill to safely inspect, diagnose, and manage Locron jobs, runs, services, configuration, imports, exports, and local dashboard state while preserving dry-run and authorization boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduled commands and HTTP requests can have real side effects when a Locron job is applied or run.

Mitigation: Review dry-run JSON for normalized targets, schedules, enabled state, and policies, then require explicit user authorization before real execution or mutation.

Risk: Dashboard tokens, inline values, headers, bodies, imports, and exports can expose secrets or credential-like data.

Mitigation: Prefer status checks that do not reveal secrets and require explicit acknowledgement before token display or rotation, plaintext import, or plaintext export.

Risk: Service changes, dashboard registration changes, cancellations, enablement, disablement, and removals may not support dry-run.

Mitigation: Inspect the exact target immediately before acting, limit scope to the named target, and verify durable state after the authorized mutation completes.

## Reference(s):

- [Locron 0.5-0.8 safety model](references/safety.md)
- [Locron ClawHub skill page](https://clawhub.ai/whitekiwi/skills/locron)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise operational summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON command output when available and preserves warnings, unknowns, and authorization boundaries.]

## Skill Version(s):

0.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
