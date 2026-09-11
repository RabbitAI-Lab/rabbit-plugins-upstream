## Description:

X-ray any Polymarket wallet for skill level, entry quality, bot detection, and edge analysis using public Polymarket activity data.

This skill is for research and development only.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and prediction-market analysts use this skill to inspect public Polymarket wallet activity, compare trader profiles, and study behavioral signals such as entry quality, bot-like timing, hedging, and drawdown risk. It should support research and decision review, not automatic copytrading or financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review marks the release suspicious because the wallet analyzer is described as public-data only while the package also requests SIMMER_API_KEY and includes authenticated account-status behavior.

Mitigation: Review the skill before installation, run it in an isolated environment, and export SIMMER_API_KEY only when intentionally using the Simmer account-status helper.

Risk: Wallet metrics and generated recommendations can be mistaken for copytrading instructions or financial advice.

Mitigation: Use the output for research and independent review only; do not automate trades or allocate capital based solely on the skill's recommendation field.

Risk: Historical wallet performance, entry quality, and arbitrage indicators may not generalize to future market conditions.

Mitigation: Treat results as retrospective analysis, validate assumptions separately, and use paper or dry-run workflows before any real-money use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/polymarket-wallet-xray)
- [Simmer API Reference](https://docs.simmer.markets/api/overview)
- [Polymarket CLOB API](https://clob.polymarket.com)
- [Polymarket Gamma markets keyset endpoint](https://gamma-api.polymarket.com/markets/keyset)
- [Original wallet analysis framework](https://x.com/thejayden/status/2020891572389224878)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [CLI text or JSON metrics, with markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wallet profitability, entry-quality, bot-detection, arbitrage, risk-profile, and recommendation fields.]

## Skill Version(s):

1.1.5 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
