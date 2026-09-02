## Description:

小果(微信:xg_quant)基金量化分析助手专注于基金量化分析工具，基于小果量化策略系统，提供基金历史行情数据、基金因子数据、基金策略回测、基金组合分析等核心功能，适用于基金投资者、资产配置研究员和量化策略开发者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[li152](https://clawhub.ai/user/li152)

### License/Terms of Use:

MIT-0

## Use Case:

External fund investors, asset-allocation researchers, and quantitative strategy developers use this skill to request ETF fund market data, factor data, strategy backtests, and portfolio analysis from the 小果量化 system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentialed API usage could expose account details or authorization codes, especially over non-HTTPS connections.

Mitigation: Use only trusted servers and accounts, prefer HTTPS, and avoid entering valuable credentials into untrusted endpoints.

Risk: The security scan reports broad network, code-submission, deletion, file-write, strategy-execution, community-publishing, and custom-code data-call capabilities.

Mitigation: Review and scan the skill before deployment, avoid running bundled scripts on sensitive directories, and require explicit human confirmation before high-impact actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/li152/skills/xg-fund-quant)
- [Publisher profile: li152](https://clawhub.ai/user/li152)
- [xg_quant_trader usage tutorial](https://gitcode.com/qq_50882340/xg_quant_trader)
- [Fund factor API reference](references/xg_factor.txt)
- [Fund strategy API reference](references/xg_factor_trader.txt)
- [TDX function reference](references/xg_tdx_func.txt)
- [Alpha factor reference](references/alpha.txt)
- [Factor table reference](references/因子表.txt)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with Python API examples and parameter references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include credentialed API call examples for ETF fund data, factor analysis, strategy backtesting, and portfolio analysis.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
