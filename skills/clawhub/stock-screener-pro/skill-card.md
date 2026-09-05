## Description:

A股行情、量化筛选、回测、因子挖掘、同花顺 iFinD、AI4Trade 与受限多智能体投研 MCP。

This skill is ready for commercial/non-commercial use.

## Publisher:

[frontier-ai-vl](https://clawhub.ai/user/frontier-ai-vl)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and agents use this skill for A-share market review, stock screening, technical snapshots, lightweight backtesting, factor research, local portfolio records, alerts, AI4Trade interactions, and bounded multi-agent investment research. It is for research and simulation workflows and does not connect to brokers or place real orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use market-data credentials and external model or data services, which may expose research prompts, stock symbols, or requested market data to configured providers.

Mitigation: Keep credentials in the host environment or secret manager, review provider configuration before use, and require confirm_external_ai=true for each external AI research run.

Risk: AI4Trade actions can change account or social state, including publishing signals or content, following accounts, heartbeat reads, and exchanging points.

Mitigation: Require explicit user approval and confirm=true for each AI4Trade state-changing action, and review the exact action parameters before allowing it.

Risk: Backtests, factor scores, and model outputs can be misleading because they may be affected by overfitting, data limits, sample selection, costs, slippage, or market changes.

Mitigation: Treat outputs as research evidence only, review stated data limitations, use independent validation periods, and do not interpret scores as buy or sell instructions.

Risk: Optional quant backends can install packages and download external research data when manually bootstrapped.

Mitigation: Run bootstrap scripts only after review, use the pinned QuantaAlpha commit and isolated virtual environments, and verify upstream license and data terms before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/frontier-ai-vl/skills/stock-screener-pro)
- [Usage examples](references/usage-examples.md)
- [QuantaAlpha repository](https://github.com/QuantaAlpha/QuantaAlpha.git)
- [QuantaAlpha Qlib CSI300 dataset](https://huggingface.co/datasets/QuantaAlpha/qlib_csi300/resolve/main)
- [Tonghuashun iFinD QuantAPI endpoint](https://quantapi.51ifind.com)
- [AI4Trade API endpoint](https://ai4trade.ai/api)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Structured tool responses and Markdown guidance with inline code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are research and simulation results; external AI research and AI4Trade state changes require explicit per-action confirmation.]

## Skill Version(s):

3.8.1 (source: server release evidence and LOCAL_PATCHES.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
