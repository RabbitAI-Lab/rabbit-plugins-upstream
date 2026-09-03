## Description:

缠论买点扫描闭环工作流：扫描科创板和创业板缠论一、二、三类买点，滚动复用自选股分组，判断单日形态，并生成次日条件单与 HTML 报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[menglaw2308](https://clawhub.ai/user/menglaw2308)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run an A-share technical-analysis workflow after market close: scan candidate buy points, manage Tencent watchlist groups, calculate next-session conditional orders, and review an HTML trading-action report. The report is decision support and should be checked against current market data before any real order is placed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can use authenticated market and watchlist connectors to update Tencent watchlist groups and produce trading-action reports.

Mitigation: Install and run it only when the operator is comfortable granting those connector permissions, and review watchlist changes and generated reports before acting.

Risk: Market data, formulas, or generated conditional-order prices may be incorrect or stale.

Mitigation: Verify the input market data, formula assumptions, and generated HTML report before placing any real orders.

Risk: The output is financial decision support and may be mistaken for a guarantee or investment advice.

Mitigation: Treat the report as probabilistic technical-analysis support; do not rely on it as a promise of returns or a substitute for independent review.

## Reference(s):

- [A+B 合并主策略参数表](references/策略参数表.md)
- [ClawHub skill page](https://clawhub.ai/menglaw2308/skills/chanlun-scan-closed-loop)
- [ClawHub publisher profile](https://clawhub.ai/user/menglaw2308)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, Python configuration updates, shell commands, and generated HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided trading dates and stock pool data; generated reports should be manually reviewed before trading decisions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
