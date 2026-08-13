## Description:

Real-time supervisor and control interface for the DRADIS prediction-market trading engine across Polymarket International, Polymarket US, and Kalshi, with DRADIS_API_KEY authentication support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mbordash](https://clawhub.ai/user/mbordash)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to monitor a DRADIS prediction-market trading engine, inspect positions, telemetry, logs, latency, squadrons, and LLM advisor activity, and apply carefully confirmed configuration changes. It is intended for DRADIS instances the user controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed configuration patches or LLM-action approvals can affect live trading behavior and real money.

Mitigation: Require explicit human confirmation before any write, validate fields with the config schema, and read back changed values before reporting success.

Risk: A leaked or overprivileged DRADIS_API_KEY could expose a trading engine to unauthorized monitoring or configuration changes.

Mitigation: Use a dedicated least-privilege API key and enable DRADIS_READ_ONLY when only monitoring is needed.

Risk: Running against an untrusted or third-party DRADIS instance could expose account, position, strategy, or market data.

Mitigation: Install only for DRADIS instances the user controls and treat logs, positions, telemetry, and configuration values as sensitive trading information.

## Reference(s):

- [DRADIS project homepage](https://github.com/mbordash/DRADIS)
- [ClawHub skill page](https://clawhub.ai/mbordash/skills/dradis-tactical-command)
- [Publisher profile](https://clawhub.ai/user/mbordash)

## Skill Output:

**Output Type(s):** [text, markdown, API Calls, configuration, guidance]

**Output Format:** [Markdown and structured API request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include DRADIS status summaries, position and telemetry analysis, logs, configuration patch proposals, and post-change verification results.]

## Skill Version(s):

1.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
