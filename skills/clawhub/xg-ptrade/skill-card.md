## Description:

小果量化交易Ptrade全能助手 supports Ptrade quantitative-strategy work, including backtest setup, Python strategy code generation, trading-log analysis, live-trading signal guidance, performance attribution, and risk assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[li152](https://clawhub.ai/user/li152)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and quantitative-trading practitioners use this skill to create and adapt Ptrade Python strategies, configure backtests, inspect trading logs and performance metrics, and prepare risk controls before simulation or live deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or bundled Ptrade strategies can place live trades once enabled in Ptrade, including full-position order paths.

Mitigation: Run strategies in backtest or simulation first, manually review every generated order path, and require explicit human approval before live execution.

Risk: The artifact includes margin and futures trading examples that can increase financial exposure.

Mitigation: Remove or disable margin, futures, reverse-repo, and other leveraged trading APIs unless the user explicitly needs them and is authorized to use them.

Risk: Backtest behavior may diverge from live execution because commissions, slippage, trading halts, price limits, and broker data latency affect orders.

Mitigation: Configure realistic costs and liquidity limits, filter halted/ST/delisting securities, and compare simulated behavior with paper trading before deployment.

## Reference(s):

- [Ptrade API Quickstart](artifact/references/ptrade_api_quickstart.md)
- [Strategy Notes](artifact/references/strategy_notes.md)
- [Ptrade API Documentation](artifact/references/ptrade API文档.pdf)
- [ClawHub Skill Page](https://clawhub.ai/li152/skills/xg-ptrade)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with Python strategy code blocks and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Ptrade strategy templates, backtest settings, trading-log interpretation, performance analysis, and risk-review notes.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata; artifact frontmatter reports 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
