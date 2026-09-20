## Description:

Monitors, validates, summarizes, and reports Iranian financial markets, including FX, gold, coin, USDT/Toman, selected crypto prices, Fear & Greed, TGJU, Nobitex, Wallex, Bitpin, and Persian market reports, while preserving partial-data provenance and explicit source failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ehsanghaffar](https://clawhub.ai/user/ehsanghaffar)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to collect live Iranian market and crypto snapshots, generate Persian-language reports, and preserve source-level failures instead of inventing missing prices. It is for neutral market monitoring and explanation, not personalized investment advice or trading signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The live watcher contacts public market and news sites and depends on changing page structures or third-party API availability.

Mitigation: Run with --stdout-only first, review errors and warnings, and treat partial snapshots as incomplete instead of filling missing prices manually.

Risk: The watcher may write dated JSON snapshots to a local output directory.

Mitigation: Use --stdout-only for inspection or configure --output-dir intentionally before routine collection.

Risk: Dependency versions and network behavior may vary across environments.

Mitigation: Use a locked or pinned Python environment before scheduled or repeated use.

Risk: Market outputs could be mistaken for investment advice.

Mitigation: Keep summaries neutral, retain source attribution, and avoid personalized recommendations, guaranteed predictions, or buy/sell signals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ehsanghaffar/skills/iran-finance-markets-monitor)
- [Server-resolved GitHub provenance](https://github.com/ehsanghaffar/skills/tree/main/skills/iran-finance-markets-monitor)
- [Market data sources reference](references/market-data-sources.md)
- [TGJU market data](https://www.tgju.org/)
- [TGJU crypto news](https://www.tgju.org/news/category/93966/)
- [Cointelegraph RSS fallback](https://cointelegraph.com/rss)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, shell commands, Persian report text, and JSON market snapshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write dated local JSON snapshots unless run with --stdout-only; reports preserve null values, warnings, errors, and source attribution.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter metadata lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
