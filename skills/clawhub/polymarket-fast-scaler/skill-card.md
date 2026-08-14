## Description:

Polymarket FastScaler helps automate BTC 5-minute Polymarket trading with a magnitude-gated momentum signal and conviction-ladder position sizing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading operators use this skill to paper-test or run a BTC 5-minute Polymarket strategy that sizes positions from a gated 1-minute BTC momentum signal. The skill can place live orders and should be validated independently before any real-money use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automate real-money Polymarket trades.

Mitigation: Run paper mode first, keep daily and per-market budget caps tight, and enable live trading only after independent validation.

Risk: The strategy is unvalidated despite a conflicting validation phrase in the documentation.

Mitigation: Treat the strategy as an unvalidated reference template and do not rely on the retracted performance claim.

Risk: Configuration can be changed beyond the stated BTC 5-minute scope.

Mitigation: Keep the default BTC and 5-minute settings unless other assets, windows, or thresholds have been separately tested.

Risk: API keys and wallet credentials can authorize trading activity.

Mitigation: Protect the Simmer API key and any wallet private key, avoid committing secrets, and use managed-wallet defaults where appropriate.

Risk: Fast markets may resolve before scheduled stop-loss or take-profit monitoring can act.

Mitigation: Use conservative position sizes because sub-15-minute markets rely primarily on exposure limits rather than exit monitoring.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/simmer/skills/polymarket-fast-scaler)
- [Skill Instructions](artifact/SKILL.md)
- [Risk Disclaimer](artifact/DISCLAIMER.md)
- [Paper Validation Results](artifact/paper-validation-results.md)
- [Release Notes](artifact/NEXT.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with Python commands, JSON configuration, and CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paper mode is the default; live mode can execute Polymarket trades when credentials and live flags are supplied.]

## Skill Version(s):

1.2.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
