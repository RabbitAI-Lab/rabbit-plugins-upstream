## Description:

A QMT quantitative trading assistant that helps generate, review, and troubleshoot Python strategy code for backtesting and live trading across stocks, futures, options, ETFs, convertible bonds, and margin trading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[li152](https://clawhub.ai/user/li152)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and quantitative trading practitioners use this skill to produce QMT strategy code, inspect common QMT coding issues, query platform APIs, and adapt templates for simulation or live trading workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated QMT strategies may contain live-order, cancellation, or repayment operations that can affect funded accounts.

Mitigation: Review all passorder, order, cancel, and repayment code manually before execution and test in simulation before using a funded account.

Risk: Strategy examples may expose or encourage hardcoded account values or sensitive trading credentials.

Mitigation: Move account identifiers and credentials into secure local configuration and avoid sharing them in prompts or generated code.

Risk: The skill lacks sufficient safeguards around financial actions and account data.

Mitigation: Install only when live QMT trading-code assistance is intended and require human approval before any generated code is connected to a trading account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/li152/skills/xg-qmt)
- [小果全能大QMT量化助手](references/小果全能大QMT量化助手.txt)
- [综合下单函数](references/23综合下单函数.txt)
- [交易下单函数](references/9交易下单函数.txt)
- [常见问题](references/63常见问题.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Python code blocks and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include QMT live-order examples, backtest templates, diagnostics, and API usage notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
