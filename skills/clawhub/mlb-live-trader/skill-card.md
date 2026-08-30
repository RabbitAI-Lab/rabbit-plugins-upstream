## Description:

Use when comparing live MLB win probabilities with executable prediction-market prices through Simmer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kvzsolt](https://clawhub.ai/user/kvzsolt)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and technically sophisticated prediction-market users use this skill to compare live MLB win probabilities with executable Simmer market prices, evaluate paper trades, and optionally place bounded live orders after explicit opt-in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live mode can submit real-money prediction-market orders that may lose their full purchase price.

Mitigation: Start in paper mode, read the disclaimer, initialize live state, review per-order and daily limits, and use --live only after explicit operator review.

Risk: Simmer API keys or wallet material could be exposed if stored in source files, config files, logs, or shell history.

Mitigation: Keep SIMMER_API_KEY and wallet-related secrets in an environment-managed secret store and do not write them to config.json or logs.

Risk: External sports feeds, market data, venue liquidity, fees, and order responses can lag, change, fail, or be misidentified.

Mitigation: Require fresh ESPN signals and executable quotes, preserve paper-first validation, supervise early live runs, and independently verify positions.

Risk: Multiple hosts or schedulers using one account may not share local budget and duplicate-order controls.

Mitigation: Use one scheduler per account and point every instance at the same absolute SIMMER_MLB_STATE_PATH on a lock-capable filesystem.

## Reference(s):

- [MLB Live Trader ClawHub page](https://clawhub.ai/kvzsolt/skills/mlb-live-trader)
- [DISCLAIMER.md](DISCLAIMER.md)
- [ESPN MLB scoreboard endpoint](https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard)
- [ESPN MLB summary endpoint](https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/summary)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, shell command examples, plain-text run output, and optional machine-readable JSON status lines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paper mode is the default; live mode requires SIMMER_API_KEY and explicit --live opt-in.]

## Skill Version(s):

2.2.1 (source: evidence release metadata and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
