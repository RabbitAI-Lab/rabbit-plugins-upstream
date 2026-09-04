## Description:

An MCP stock research toolkit for A-share quotes, quantitative screening, simulated backtesting, factor research, Tonghuashun iFinD, AI4Trade, and constrained multi-agent investment research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frontier-ai-vl](https://clawhub.ai/user/frontier-ai-vl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and analysts use this skill to gather A-share market context, screen stocks, run simulated backtests and factor studies, maintain local watchlists or alerts, and run explicitly confirmed AI-assisted investment research without broker order execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI4Trade operations can change account state or publish public-facing signals and content when AI4TRADE_TOKEN is configured.

Mitigation: Keep AI4TRADE_TOKEN unset unless those features are needed, and review every exact confirm=true action before allowing it.

Risk: Optional bootstrap scripts download and run third-party quant backends and research data.

Mitigation: Run optional bootstrap scripts only after accepting the extra third-party code, pinned versions, data downloads, and upstream terms.

Risk: Market, backtest, factor, and AI-assisted research outputs may be incorrect, stale, overfit, or misleading.

Mitigation: Treat outputs as research and simulation only, and independently review data coverage, assumptions, costs, capacity, and sample-out stability before relying on results.

Risk: External AI research may send prompts, symbols, and required market data to configured model or data services and may incur model costs.

Mitigation: Require explicit confirm_external_ai=true for each external AI run and use only approved model and data service configurations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/frontier-ai-vl/skills/stock-screener-pro)
- [Usage Examples](references/usage-examples.md)
- [Tonghuashun iFinD QuantAPI](https://quantapi.51ifind.com)
- [AI4Trade API](https://ai4trade.ai/api)
- [QuantaAlpha Repository](https://github.com/QuantaAlpha/QuantaAlpha.git)
- [QuantaAlpha Qlib CSI300 Dataset](https://huggingface.co/datasets/QuantaAlpha/qlib_csi300/resolve/main)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured JSON-like tool responses with occasional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Financial outputs are research and simulation only; AI, account-state, publishing, and optional backend setup actions require explicit confirmation.]

## Skill Version(s):

3.8.0 (source: server release metadata and LOCAL_PATCHES.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
