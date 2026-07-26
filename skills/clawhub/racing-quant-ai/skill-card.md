## Description: <br>
赛马量化AI选股系统，集成量化策略选股和个股智能推荐分析，从量化策略数据库筛选符合需求的策略，获取持仓个股，再进行深度分析，最终给出投资参考。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenxyzcyxpp](https://clawhub.ai/user/chenxyzcyxpp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to match A-share quant strategy signals to holdings, run structured stock and portfolio analysis, and produce investment-reference reports with data-source notes and disclaimers. It also includes workflows for position sizing, strategy drawdown review, and gated trading-instruction generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence flags plaintext database credentials and access to remote strategy databases. <br>
Mitigation: Install only for trusted publishers, rotate or remove exposed database credentials before use, and limit database permissions. <br>
Risk: The security evidence flags live trading and production/admin workflows as too powerful for a stock-analysis skill. <br>
Mitigation: Separate analysis from brokerage and admin capabilities, and require explicit human confirmation plus dry-run previews before any trading or server action. <br>
Risk: Financial analysis may become misleading when market-data sources fail or return stale data. <br>
Mitigation: Require reports to cite actual data sources, disclose data retrieval failures, and keep investment-risk disclaimers in user-facing analysis. <br>


## Reference(s): <br>
- [信号-标的匹配框架](references/signal-asset-matching-framework.md) <br>
- [概念股/主题驱动产业链分析工作流](references/concept-stock-analysis-workflow.md) <br>
- [Multi-Stock Deep Analysis Workflow](references/multi-stock-analysis-workflow.md) <br>
- [Portfolio Deep Analysis Workflow](references/portfolio-analysis-workflow.md) <br>
- [策略仓位优化回测框架](references/position-sizing-optimization.md) <br>
- [策略历史回撤分析方法论](references/strategy-drawdown-analysis.md) <br>
- [策略持仓 → QMT 交易执行流水线](references/trading-execution-pipeline.md) <br>
- [Fintech Web 应用代码结构](references/fintech-codebase-structure.md) <br>
- [用户自研量化仓库 tsauto_run 策略储备清单](references/tsauto_run-strategy-inventory.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports, JSON trading instructions, code snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Financial-analysis outputs should identify actual data sources, disclose failed data retrieval, include risk notes, and preserve investment disclaimers.] <br>

## Skill Version(s): <br>
1.10.1 (source: server release metadata; artifact SKILL.md lists 1.10.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
