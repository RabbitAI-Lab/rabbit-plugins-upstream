## Description:

小果量化交易平台助手 helps agents use the XG Quant Platform for market data retrieval, factor and financial analysis, strategy backtesting, simulated trading, and strategy management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[li152](https://clawhub.ai/user/li152)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and quantitative trading users use this skill to generate Python client usage guidance and examples for retrieving market data, analyzing factor and financial data, backtesting strategies, and managing simulated or community strategies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends account credentials to a remote API endpoint.

Mitigation: Install only when the XG Quant server and Python client are trusted, and use a protected HTTPS or private-network endpoint.

Risk: Strategy publishing, deletion, and bulk deletion can change or remove user-managed strategy state.

Mitigation: Require explicit user confirmation before state-changing calls, especially delete-all operations.

Risk: Custom function based data requests can introduce additional execution or data-handling risk.

Mitigation: Review custom function requests and restrict them to trusted code, inputs, and destinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/li152/skills/xg-quant-pt)
- [XG Quant Backtrader Data usage tutorial](https://gitcode.com/qq_50882340/xg_quant_backtrader_data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include examples for remote API calls that require account credentials and explicit confirmation for state-changing strategy operations.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
