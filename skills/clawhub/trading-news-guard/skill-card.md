## Description:

Provides trading agents with news blackout awareness for high-impact events such as NFP, CPI, FOMC, and ECB so they can decide whether to skip or delay trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading-agent operators use this skill as a reference for checking high-impact economic events before trade entry and for applying fail-closed blackout behavior when news status is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact describes both local/no-network behavior and API-based status checks, creating ambiguity in a financially sensitive trading workflow.

Mitigation: Confirm and document the intended data source before use, then implement a tested check that fails closed when event status cannot be verified.

Risk: The release does not include working code, a defined data source, or a verifiable command.

Mitigation: Do not connect it to automated trading until the missing implementation is replaced with reviewed code, tests, and explicit blackout-window behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/trading-news-guard)
- [Publisher profile](https://clawhub.ai/user/northcap-group)

## Skill Output:

**Output Type(s):** [guidance, configuration, code, JSON]

**Output Format:** [Markdown guidance with JSON examples and Python pseudocode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only artifact; no working command or data source is included.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
