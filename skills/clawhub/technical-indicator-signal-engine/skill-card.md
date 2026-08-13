## Description:

Generates buy, sell, or hold technical-analysis signals from OHLCV market data by combining EMA/ADX trend checks, Bollinger Band mean-reversion checks, and OBV-based volume-price confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[night-king-lt](https://clawhub.ai/user/night-king-lt)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to analyze supplied OHLCV price data and produce technical buy, sell, or hold signals for equities, ETFs, or crypto assets. Outputs are technical-analysis indicators and are not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake technical-analysis trading signals for investment advice.

Mitigation: Label outputs as technical-analysis indicators only and require users to make independent decisions based on their own risk tolerance or licensed professional advice.

Risk: Running the bundled demo can make outbound requests to the OKX public market-data API.

Mitigation: Run live-data examples only in network-approved environments, or provide local OHLCV data directly to the SignalEngine.

Risk: Incorrect OHLCV column mapping can produce misleading signals.

Mitigation: Verify that open, high, low, close, and volume columns are correctly mapped before generating signals.

## Reference(s):

- [Indicator Calculation Specification](references/indicator_spec.md)
- [Server-Resolved Source Repository](https://github.com/night-king-lt/technical-indicator-signal-engine)
- [ClawHub Skill Listing](https://clawhub.ai/night-king-lt/skills/technical-indicator-signal-engine)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown and Python signal outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces per-symbol signal series where 1 means buy, -1 means sell, and 0 means hold.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and README.md); release metadata version 0.1.0

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
