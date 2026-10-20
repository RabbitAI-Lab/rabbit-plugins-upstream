## Description:

Helps agents audit and optimize local OpenClaw, Claude Code, and Hermes Agent configurations for misconfigurations, security issues, stale authentication, and token waste.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect agent configuration, review audit findings and proposed optimizations, and apply approved OpenClaw fixes with rollback support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A globally installed third-party CLI reads local agent configuration, including authentication profiles.

Mitigation: Install only if this access is acceptable; review findings without sharing credentials or configuration contents.

Risk: Applying proposed fixes can change OpenClaw configuration.

Mitigation: Use dry-run modes first and approve only the intended proposals before applying changes.

Risk: Optional monitoring installs a daily cron job and posts audit summary data to Drakon Systems.

Mitigation: Enroll only if you accept the scheduled reports; leave monitoring disabled otherwise.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/drakon-agent-optimizer)
- [Agent Optimizer product information](https://drakonsystems.com/products/agent-optimizer)
- [Agent Optimizer npm package](https://www.npmjs.com/package/@drakon-systems/agent-optimizer)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with CLI commands and JSON audit or plan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings and proposed changes can be reviewed before applying them.]

## Skill Version(s):

0.16.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
