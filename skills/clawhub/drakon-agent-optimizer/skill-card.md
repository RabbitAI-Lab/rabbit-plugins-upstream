## Description:

CLI tool that audits Claude Code, OpenClaw, and Hermes Agent configuration files for misconfigurations, token waste, security issues, and stale authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jarvis-drakon](https://clawhub.ai/user/jarvis-drakon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to audit and optimize local Claude Code, OpenClaw, and Hermes Agent configurations, review JSON findings and plans, and apply selected fixes through a transactional workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The tool reads local OpenClaw and Claude Code configuration files, including auth profile metadata and workspace skills, hooks, and extensions.

Mitigation: Install only when that local access is acceptable for the environment, and review the documented file scope before running audits or scans.

Risk: Licensed fix and optimize modes can modify local OpenClaw configuration.

Mitigation: Use dry-run first, review proposed changes, and apply only the changes approved by the user.

Risk: Optional monitoring creates a daily cron job and posts summary counts to the vendor endpoint.

Mitigation: Enroll only when daily monitoring is desired, and use the documented disable command when monitoring should stop.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jarvis-drakon/skills/drakon-agent-optimizer)
- [Drakon Systems Agent Optimizer product page](https://drakonsystems.com/products/agent-optimizer)
- [npm package](https://www.npmjs.com/package/@drakon-systems/agent-optimizer)
- [Publisher GitHub profile](https://github.com/Drakon-Systems-Ltd)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit, plan, and apply commands emit JSON on stdout; mutating fixes require user approval and an applicable license.]

## Skill Version(s):

0.14.0 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
