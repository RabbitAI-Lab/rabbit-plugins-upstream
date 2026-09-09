## Description:

SignalRadar monitors Polymarket prediction markets for probability changes and sends alerts when configured thresholds are crossed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vahnxu](https://clawhub.ai/user/vahnxu)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to track selected Polymarket markets, inspect current monitor state, discover relevant markets, and receive threshold-based alerts through configured delivery channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Background monitoring can create a recurring scheduler entry that keeps running after the session ends.

Mitigation: Leave schedule.auto_enable unset or false unless background checks are wanted, and remove persistence with the skill's schedule disable command.

Risk: Webhook delivery can send watched market questions and probability changes to a user-configured third-party endpoint.

Mitigation: Use only trusted HTTPS webhook endpoints and keep webhook URLs private because they act as bearer credentials.

Risk: Stored OpenClaw routing or scheduled delivery state can persist locally.

Mitigation: Use schedule clear-route to remove stored OpenClaw routing and review the local SignalRadar data directory when uninstalling.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vahnxu/skills/signalradar)
- [SignalRadar Configuration Reference](artifact/references/config.md)
- [SignalRadar Runtime Protocol Reference](artifact/references/protocol.md)
- [SignalRadar Operations Reference](artifact/references/operations.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local configuration, watchlist, baseline, event log, and scheduler state through the skill CLI when the user authorizes those actions.]

## Skill Version(s):

1.5.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
