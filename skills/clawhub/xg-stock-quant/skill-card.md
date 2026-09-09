## Description:

小果股票量化分析助手 helps agents support stock quantitative analysis by querying historical market data, minute bars, technical factors, financial data, index data, strategy backtests, and portfolio analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[li152](https://clawhub.ai/user/li152)

### License/Terms of Use:

MIT-0

## Use Case:

External investors, quantitative researchers, and strategy developers use this skill to obtain stock data, calculate factors, run strategy backtests, and analyze portfolios through the 小果 quant workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials and code may be sent to a remote HTTP service.

Mitigation: Use only a trusted server and publisher, and avoid sending real credentials over plaintext HTTP.

Risk: Strategy operations may create or delete persistent records.

Mitigation: Require explicit confirmation before any create or delete strategy operation.

Risk: Bundled scripts may affect local factor data or analysis files.

Mitigation: Run scripts in an isolated workspace and keep backups of any factor data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/li152/skills/xg-stock-quant)
- [Publisher profile](https://clawhub.ai/user/li152)
- [xg_quant_trader tutorial](https://gitcode.com/qq_50882340/xg_quant_trader)
- [alpha reference](artifact/references/alpha.txt)
- [xg_factor reference](artifact/references/xg_factor.txt)
- [xg_factor_trader reference](artifact/references/xg_factor_trader.txt)
- [xg_tdx_func reference](artifact/references/xg_tdx_func.txt)
- [因子表 reference](artifact/references/因子表.txt)
- [因子计算测试 reference](artifact/references/因子计算测试.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API parameters for stock data, factors, backtests, and portfolio analysis.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
