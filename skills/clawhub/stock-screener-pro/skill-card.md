## Description:

Stock Screener provides A-share market data, quantitative screening, backtesting, Tonghuashun iFinD, AI4Trade, and restricted multi-agent investment research through MCP.

This skill is for research and development only.

## Publisher:

[frontier-ai-vl](https://clawhub.ai/user/frontier-ai-vl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external analysts use this skill to review A-share market conditions, screen candidates, inspect technical indicators, run lightweight historical tests, manage local watchlists and alerts, and request confirmed AI-assisted research. It is limited to research, simulation, and local records, with no broker connection or real order placement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API tokens or market-data credentials could be exposed if placed in prompts, tool arguments, or shared logs.

Mitigation: Keep THS and AI4Trade tokens in the host environment or secret manager, and do not provide credentials through tool parameters or chat text.

Risk: AI4Trade actions can change platform state or publish simulated signals after confirmation.

Mitigation: Review each action, symbol, quantity, content, and target account before calling the tool with confirm=true.

Risk: External AI research may send prompts, tickers, and market-data requests to configured model or data services and may incur provider costs.

Mitigation: Require explicit approval for each external research run with confirm_external_ai=true, and disclose the scope of data sent before execution.

Risk: Market data, model outputs, screening results, and backtests can be incomplete, stale, or misleading.

Mitigation: Treat outputs as research material, independently verify facts and prices, compare risk metrics, and avoid presenting results as investment advice or future return guarantees.

Risk: Lightweight technical templates and backtests do not model all real-market constraints such as full fees, slippage, halts, limit-up execution, order-book depth, or survivorship effects.

Mitigation: Surface data-limit notes with results and require additional validation before using any rule or candidate list in an investment process.

## Reference(s):

- [Usage Examples](artifact/references/usage-examples.md)
- [ClawHub Skill Page](https://clawhub.ai/frontier-ai-vl/skills/stock-screener-pro)
- [Publisher Profile](https://clawhub.ai/user/frontier-ai-vl)
- [Tonghuashun iFinD QuantAPI Endpoint](https://quantapi.51ifind.com)
- [AI4Trade API Endpoint](https://ai4trade.ai/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Structured MCP tool responses, Markdown research summaries, and inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research and simulation outputs; AI4Trade state changes and external AI research require explicit per-action confirmation.]

## Skill Version(s):

3.6.0 (source: server release metadata and artifact/server.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
