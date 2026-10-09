## Description:

Audits Claude Code, OpenClaw, and Hermes Agent configurations for security issues, misconfigurations, stale authentication, and token waste, with optional guided fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to audit local agent configurations, review security and cost findings, and plan approved changes to OpenClaw settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audits read local agent configuration and workspace extensions, which may contain sensitive material.

Mitigation: Install only when this access is appropriate; treat scanned findings as untrusted data rather than instructions.

Risk: Applying a proposed fix may change OpenClaw configuration or require a restart.

Mitigation: Preview with dry-run, review each proposal and its risk, apply only approved changes, and retain backups for rollback.

Risk: Optional monitoring creates a daily scheduled task and sends audit summary counts to the vendor.

Mitigation: Enroll only after reviewing the disclosed payload and schedule; leave monitoring disabled otherwise.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jarvis-drakon/skills/drakon-agent-optimizer)
- [Agent Optimizer product information](https://drakonsystems.com/products/agent-optimizer)
- [Agent Optimizer npm package](https://www.npmjs.com/package/@drakon-systems/agent-optimizer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Human-readable findings and recommendations; CLI supports JSON audit and change plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Changes require user approval; licensed fixes can create backups and support rollback.]

## Skill Version(s):

0.16.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
