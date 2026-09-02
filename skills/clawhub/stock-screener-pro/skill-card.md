## Description:

Provides A-share market review, quantitative screening, technical snapshots, lightweight backtesting, Tonghuashun iFinD data access, AI4Trade integration, and restricted multi-agent investment research through an MCP tool surface.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frontier-ai-vl](https://clawhub.ai/user/frontier-ai-vl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to inspect A-share market conditions, screen candidate securities, run research-only backtests and factor checks, maintain local watchlists and alerts, and request constrained AI-assisted investment research. The skill is framed for research, simulation, and local record keeping rather than broker execution or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market data, model outputs, factor benchmarks, and backtests may be incomplete, stale, or misleading if treated as trading instructions.

Mitigation: Treat all outputs as research material, review data limits and assumptions, compare against independent sources, and avoid presenting results as investment advice or guaranteed returns.

Risk: AI4Trade actions with confirmation can publish content or change AI4Trade platform state.

Mitigation: Review each requested AI4Trade action before setting confirm=true, and keep AI4Trade credentials in the host environment or secret manager rather than in prompts or tool arguments.

Risk: External AI and market services may receive research prompts, stock codes, and market-data requests.

Mitigation: Use confirm_external_ai only after explicit approval for the specific research run, and verify service configuration with get_skill_status before sending sensitive research context.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/frontier-ai-vl/skills/stock-screener-pro)
- [Usage Examples](references/usage-examples.md)
- [Tonghuashun iFinD QuantAPI](https://quantapi.51ifind.com)
- [AI4Trade API](https://ai4trade.ai/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON tool responses with occasional inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are research-oriented and may include market indicators, candidate lists, backtest summaries, status checks, local record changes, or external-service research results.]

## Skill Version(s):

3.7.0 (source: server release evidence and LOCAL_PATCHES.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
