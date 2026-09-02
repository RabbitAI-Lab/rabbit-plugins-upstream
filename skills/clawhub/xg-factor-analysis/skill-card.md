## Description:

小果量化因子分析系统助手基于 Alphalens 和自定义分析框架，帮助 agents provide factor data cleaning, IC analysis, quantile returns, long-short portfolio analysis, turnover analysis, Fama-MacBeth regression, factor stability analysis, visualization, and composite scoring for quantitative factor research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[li152](https://clawhub.ai/user/li152)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, quantitative researchers, and external users use this skill to prepare market and factor data, run factor effectiveness analysis, generate charts and local reports, and obtain scoring guidance for factor research, model construction, strategy backtesting, and teaching workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated quantitative analysis files may overwrite local outputs when force recalculation is enabled.

Mitigation: Run batch factor workflows in a working copy or dedicated data directory and review output paths before enabling force recalculation.

Risk: Market-data and factor-analysis outputs can be misleading if users provide incomplete, misaligned, or unsuitable input data.

Mitigation: Validate factor and price data formats, date alignment, missing-data handling, and generated metrics before using the outputs for trading or investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/li152/skills/xg-factor-analysis)
- [Publisher profile](https://clawhub.ai/user/li152)
- [Alphalens overview example](artifact/references/alphalens/examples/overview.txt)
- [Alphalens performance module](artifact/references/alphalens/performance.py)
- [XG Alphalens reference implementation](artifact/references/xg_alphalens/xg_alphalens.py)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python code examples, shell commands, configuration notes, and analysis workflow descriptions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local generation of quantitative analysis reports, charts, and data files.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
