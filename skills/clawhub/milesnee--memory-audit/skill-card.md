## Description:

Audits and helps repair agent memory systems using DDIA reliability checks and DDD bounded-context analysis when memory is stale, bloated, inconsistent, or due for a periodic health check.

This skill is ready for commercial/non-commercial use.

## Publisher:

[milesnee](https://clawhub.ai/user/milesnee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to baseline, diagnose, prioritize, and validate repairs to OpenClaw-style agent memory workspaces. It focuses on stale state, oversized core files, missing front matter, duplicate or weak search behavior, lifecycle gaps, and bounded-context coupling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect and change persistent agent memory and behavior files.

Mitigation: Install it only in workspaces where memory audit and repair are intentional, run diagnosis first, review planned changes before edits, and keep version control or backups available.

Risk: Example commands use fixed /tmp report paths, which can collide or expose audit details in shared environments.

Mitigation: Use workspace-specific report paths and avoid shared fixed /tmp locations when running reports.

Risk: Cron jobs, trace logging, and behavior-rule updates can create persistent operational changes.

Mitigation: Enable those changes only after explicit approval and after confirming they are desired for the target workspace.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/milesnee/skills/memory-audit)
- [Audit Checklist](references/audit-checklist.md)
- [DDIA + DDD Memory System Mapping](references/ddia-ddd-mapping.md)
- [Audit Report Template](assets/audit-report-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON baseline files, shell commands, and code or configuration change guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces baseline JSON and audit or validation Markdown; proposed repairs should be reviewed before edits are applied to persistent memory or behavior files.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
