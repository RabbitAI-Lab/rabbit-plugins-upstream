## Description:

Audits Claude Code, OpenClaw, and Hermes Agent configurations for security issues, misconfigurations, stale authentication, and opportunities to reduce token use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to review local agent configurations, inspect security and cost findings, and plan approved configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI reads local agent configuration, which can include sensitive settings.

Mitigation: Verify the npm package and publisher before installing, and run it only where that access is appropriate.

Risk: Fix and optimization commands can change local agent configuration.

Mitigation: Review dry-run plans, approve only intended changes, and retain backups for rollback.

Risk: Optional monitoring sends daily summary counts and check names to the vendor.

Mitigation: Enroll only if desired and preview the monitoring payload before enabling it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jarvis-drakon/skills/drakon-agent-optimizer)
- [Agent Optimizer product page](https://drakonsystems.com/products/agent-optimizer)
- [Agent Optimizer npm package](https://www.npmjs.com/package/@drakon-systems/agent-optimizer)

## Skill Output:

**Output Type(s):** [Analysis, Configuration instructions, Shell commands]

**Output Format:** [JSON findings and plans, summarized as text or Markdown for the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings and proposals include risk details; approved changes can include rollback guidance.]

## Skill Version(s):

0.15.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
