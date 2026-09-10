## Description:

Query Pre-IPO Observer snapshots across Jarsy, Hyperliquid, PreStocks, Polymarket, and Hiive to screen companies, inspect source freshness, compare platform-specific signals, and summarize dated published research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hackstoic](https://clawhub.ai/user/hackstoic)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to research pre-IPO company snapshots across five platforms, check source freshness, and summarize registered public research reports. It supports screening and evidence gathering only; it does not trade, refresh origin sites, or generate investment recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Natural-language research answers include a Jarsy referral/access link.

Mitigation: Treat the referral line as separate from source citations, disclose it plainly, and use --json for machine-readable output without added narrative.

Risk: An alternate PREIPO_API_BASE_URL can redirect research queries to a different compatible Observer host.

Mitigation: Leave PREIPO_API_BASE_URL unset unless the alternate API host is intentionally trusted.

Risk: Snapshot data, manual imports, prediction topics, and static reports can be stale or incomplete.

Mitigation: Preserve source timestamps, stale flags, platform notices, pagination state, and report cutoff dates; do not present missing data as zero or as risk clearance.

Risk: Market, valuation, token, contract, and prediction-probability fields use different units and meanings across platforms.

Mitigation: Keep platform results grouped, preserve units and currencies, and avoid combined rankings, summed company values, investment advice, or return promises.

## Reference(s):

- [Public API and portable client](references/api.md)
- [Jarsy: legacy public API](references/jarsy.md)
- [Hyperliquid contracts](references/hyperliquid.md)
- [PreStocks products and notices](references/prestocks.md)
- [Polymarket: company topic market outcomes](references/polymarket.md)
- [Hiive50 manual snapshot](references/hiive.md)
- [Reading published company research](references/reports.md)
- [Pre-IPO Observer](https://preipo.polyos.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Natural-language research summaries with source links and timestamps, plus optional JSON command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public GET queries; natural-language answers include a separate Jarsy referral/access line, while --json returns machine-readable output without added narrative.]

## Skill Version(s):

1.1.0 (source: server evidence release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
