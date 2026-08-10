## Description:

股票研究专家研木的Skill - 可比公司估值(Comps), 含PE/PB/ROE/利润率雷达图对比.

This skill is ready for commercial/non-commercial use.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Financial analysts, investment research users, and agents use this skill to compare a target stock against selected comparable companies using valuation, profitability, growth, and balance-sheet metrics. It supports text or JSON output plus radar and bar chart files for downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes outbound Sina Finance quote requests for analyzed tickers.

Mitigation: Install and run it only in environments where those ticker lookups and network requests are acceptable.

Risk: Generated valuation analysis can be mistaken for investment advice.

Mitigation: Treat outputs as informational research support and require qualified human review before investment decisions.

Risk: The script writes generated chart images to the selected output directory.

Mitigation: Use an intended workspace output path and review generated files before sharing or committing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/yanmu-comps-model)
- [Sina Finance](https://finance.sina.com.cn)

## Skill Output:

**Output Type(s):** [text, json, shell commands, files, guidance]

**Output Format:** [Text report or JSON with generated PNG chart files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ticker, comparable-company tickers, market, output directory, and output format parameters.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
