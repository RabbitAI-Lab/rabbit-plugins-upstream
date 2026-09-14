## Description:

Run local single-asset historical research with EMA, SMA, or RSI long/cash rules and produce basic JSON, CSV, Markdown, and chart artifacts.

This skill is for research and development only.

## Publisher:

[jiakleis](https://clawhub.ai/user/jiakleis)

### License/Terms of Use:

AGPL-3.0-only

## Use Case:

Developers, researchers, and educators use this skill to run local daily historical backtests for simple single-asset EMA, SMA, or RSI long/cash strategies from user-provided CSV data. It helps standardize a strategy, generate signals, compare against Buy & Hold, and produce auditable local result artifacts for research review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Historical backtest outputs may be mistaken for investment advice or future performance claims.

Mitigation: Treat outputs as historical research only and confirm data provenance, adjustment basis, transaction assumptions, and timing before interpreting results.

Risk: Poor CSV quality, missing fields, corporate-action handling, or timezone assumptions can distort generated signals and metrics.

Mitigation: Validate the input CSV against the data contract and document the data source, adjustment basis, gaps, currency, and timezone.

Risk: Generated run artifacts may contain local market data, strategy assumptions, or research results that should not be shared broadly.

Mitigation: Review the local runs directory before sharing or committing outputs.

Risk: Chart generation depends on the separately installed Pillow package.

Mitigation: Install the skill in an isolated virtual environment and pin Pillow according to local dependency policy.

## Reference(s):

- [Server-resolved source repository](https://github.com/jiakleis/zeyang-strategy-lab)
- [ClawHub skill page](https://clawhub.ai/jiakleis/skills/zeyang-strategy-lab)
- [Free Data Contract](references/data-contract.md)
- [Free Indicators and Signals](references/indicator-and-signal-free.md)
- [Metrics and Robustness](references/metrics-and-robustness.md)
- [Free Strategy Contract](references/strategy-contract-free.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands plus generated local JSON, CSV, Markdown, and PNG chart artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided local daily CSV; writes results under a local runs directory.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
