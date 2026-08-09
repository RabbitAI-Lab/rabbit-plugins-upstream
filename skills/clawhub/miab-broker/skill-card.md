## Description:

Operates the Message-in-a-Bottle (MIAB) LIFO callback stack for async inter-agent delegation, callback routing, wake registration, returns, resolution, and reaping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albzhu](https://clawhub.ai/user/albzhu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to coordinate local multi-agent task delegation without polling. It provides command guidance and scripts for creating, forwarding, returning, resolving, listing, and reaping file-backed callback envelopes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the release suspicious because the package contains an under-documented Discord notifier that can send callback history outside the machine despite no-network claims.

Mitigation: Review before installing, and do not run or schedule the closed-bottle notifier unless the Discord target, account, channel, and redaction needs have been explicitly reviewed.

Risk: Callback task, summary, result, and resume fields are written to local state and can be copied into dispatch messages.

Mitigation: Do not place secrets in callback fields; reference non-sensitive locations only when needed.

Risk: The broker is intended for a trusted single-user agent setup and does not authenticate agent identity claims.

Mitigation: Use it only with trusted local agents and keep CLAW_HOME private with restrictive permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/albzhu/skills/miab-broker)
- [Publisher profile](https://clawhub.ai/user/albzhu)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output from bundled scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local callback state under CLAW_HOME and may emit dispatch messages for agent wake routing.]

## Skill Version(s):

1.3.0 (source: server release metadata and changelog, released 2026-08-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
