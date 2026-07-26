## Description: <br>
Generate modular, data-backed AM or PM market reports across global assets, including daily briefs, cross-asset dashboards, trend tables, top movers, and a best-idea wrap-up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[boilerrat](https://clawhub.ai/user/boilerrat) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and market-monitoring users can use this skill to create configurable AM or PM market briefs across equities, rates, FX, commodities, and crypto. It helps assemble concise summaries, trend tables, top-mover blocks, and a best-idea wrap-up from requested regions and tickers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may use third-party financial data services for requested tickers and market screens. <br>
Mitigation: Install and run it only when those public data sources are acceptable for the intended workflow, and disclose the requested tickers or screens accordingly. <br>
Risk: Market data, top-mover endpoints, and technical trend labels can be delayed, unavailable, rate-limited, or changed by providers. <br>
Mitigation: Treat generated briefs as analytical drafts, verify important figures against authoritative sources, and review pattern labels before using them in decisions. <br>
Risk: Financial summaries or best-idea sections could be mistaken for certain trading instructions. <br>
Mitigation: Keep language conceptual, include risks and invalidation, and avoid placing trades or presenting pattern labels as guarantees. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/boilerrat/skills/modular-market-brief) <br>
- [Yahoo Finance screener endpoint](https://query1.finance.yahoo.com/v1/finance/screener/predefined/saved) <br>
- [TMX Money Canadian markets](https://money.tmx.com/en/canadian-markets) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with optional JSON or markdown tables from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use optional public financial data sources and local Python helper scripts when structured market data is requested.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
