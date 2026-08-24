## Description:

Provides A-share market review, quantitative screening, backtesting, Tonghuashun iFinD data access, AI4Trade integration, and confirmation-gated multi-agent investment research through an MCP skill.

This skill is for research and development only.

## Publisher:

[frontier-ai-vl](https://clawhub.ai/user/frontier-ai-vl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to inspect A-share markets, screen candidate stocks, run lightweight research backtests, manage local watchlists and alerts, and request AI-assisted research. The skill is intended for research, simulation, and local record keeping, not brokerage execution or real trading orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI4Trade actions can change platform state, including following, publishing, accepting replies, exchanging points, or marking heartbeat messages.

Mitigation: Require explicit approval for each action and only proceed when the caller passes confirm=true for that specific AI4Trade operation.

Risk: External AI research can send prompts, stock codes, and market data to configured model or data services and may incur model-provider costs.

Mitigation: Run get_skill_status before research, require confirm_external_ai=true for each run, and tell users to independently verify all research outputs.

Risk: Market screening, backtests, technical indicators, and prediction signals can be incomplete or misleading if treated as investment advice.

Mitigation: Present outputs as research and simulation only, avoid claims of guaranteed returns, and require independent review before any financial decision.

Risk: Market data and integration credentials could be exposed if passed through prompts or redirected to untrusted services.

Mitigation: Keep tokens in the host environment or secret manager, use fixed service endpoints or loopback-only DSA access, and never pass secrets as tool arguments.

## Reference(s):

- [Usage Examples](references/usage-examples.md)
- [ClawHub Release Page](https://clawhub.ai/frontier-ai-vl/skills/stock-screener-pro)
- [Tonghuashun iFinD QuantAPI Endpoint](https://quantapi.51ifind.com)
- [AI4Trade API Endpoint](https://ai4trade.ai/api)

## Skill Output:

**Output Type(s):** [text, markdown, structured data, configuration, guidance]

**Output Format:** [MCP tool responses with text, markdown-style explanations, and JSON-compatible structured data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include market snapshots, screening results, backtest summaries, prediction signals, local portfolio or alert records, AI4Trade status/actions, and multi-agent research reports.]

## Skill Version(s):

3.5.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
