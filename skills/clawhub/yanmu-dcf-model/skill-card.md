## Description:

Builds DCF valuation models with five-year free cash flow projections, Gordon-growth terminal value discounting, and WACC/growth sensitivity heatmaps for supported equity tickers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Equity analysts, finance learners, and agents supporting investment research use this skill to run DCF valuation scenarios for supported A-share, Hong Kong, and U.S. tickers, compare implied value with current market price, and produce sensitivity analysis artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may query Sina Finance for live ticker prices during execution.

Mitigation: Install and run it only where outbound quote lookup is acceptable, and validate current price data before relying on results.

Risk: The skill can write sensitivity heatmap images into the selected output directory.

Mitigation: Use a controlled output directory and review generated files before sharing or retaining them.

Risk: DCF outputs depend on embedded financial assumptions and supported-company data coverage.

Mitigation: Treat results as investment research support and review assumptions, inputs, and sensitivity ranges before using the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/yanmu-dcf-model)
- [Sina Finance](https://finance.sina.com.cn)

## Skill Output:

**Output Type(s):** [text, json, shell commands, files, guidance]

**Output Format:** [Plain text DCF report or structured JSON, with an optional PNG sensitivity heatmap file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ticker and market inputs, accepts optional WACC, terminal growth, output directory, and output format settings, and may fetch live quote data during execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
