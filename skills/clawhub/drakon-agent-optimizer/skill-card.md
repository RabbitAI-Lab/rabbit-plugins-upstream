## Description:

Audits Claude Code, OpenClaw, and Hermes Agent configurations for security issues, misconfigurations, stale authentication, and token waste, and offers guided optimizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use the skill to audit local agent configurations, review security and cost findings, and plan or apply approved OpenClaw fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auditing reads local agent configurations, authentication profile metadata, and workspace skill, hook, or extension files.

Mitigation: Install only if this local access is acceptable, and treat any quoted content in findings as untrusted data.

Risk: Applying fixes can change OpenClaw configuration.

Mitigation: Preview with dry-run or plan mode and apply only human-approved proposals; retain backups for rollback.

Risk: Optional monitoring sends daily summary data and installs a scheduled task.

Mitigation: Enroll only after reviewing the summary payload and accepting the scheduled transmissions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jarvis-drakon/skills/drakon-agent-optimizer)
- [Agent Optimizer product information](https://drakonsystems.com/products/agent-optimizer)
- [Agent Optimizer npm package](https://www.npmjs.com/package/@drakon-systems/agent-optimizer)

## Skill Output:

**Output Type(s):** [Analysis, Configuration guidance, Shell commands]

**Output Format:** [Text and structured JSON reports or plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings and risk-rated proposals can be reviewed before applying licensed fixes.]

## Skill Version(s):

0.16.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
