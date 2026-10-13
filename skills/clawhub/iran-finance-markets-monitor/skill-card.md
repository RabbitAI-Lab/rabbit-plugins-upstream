## Description:

Collects and validates Iranian currency, gold, and cryptocurrency prices and produces source-attributed market snapshots and neutral Persian reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ehsanghaffar](https://clawhub.ai/user/ehsanghaffar)

### License/Terms of Use:

MIT-0

## Use Case:

Market analysts, developers, and other users can collect Iranian FX, gold, and crypto prices and prepare an auditable Persian market report without personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live collection contacts external finance and news sites and may write local JSON snapshots.

Mitigation: Use --stdout-only when local files are unnecessary and review the source sites and output location before running.

Risk: Unpinned dependencies or unavailable and changing data sources can affect reliability.

Mitigation: Use a virtual environment, pin dependency versions for deployment, and report missing or invalid values instead of inventing prices.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ehsanghaffar/skills/iran-finance-markets-monitor)
- [Server-resolved source repository](https://github.com/ehsanghaffar/skills/tree/main/skills/iran-finance-markets-monitor)
- [Market data sources and validation notes](references/market-data-sources.md)
- [TGJU market data](https://www.tgju.org/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Persian market report or structured JSON snapshot]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source attribution, Tehran timestamps, and explicit gaps or source failures; optional local JSON snapshot.]

## Skill Version(s):

0.1.1 (source: ClawHub release; bundled skill frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
