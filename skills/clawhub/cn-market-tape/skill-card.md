## Description:

Use when the user asks for A-share intraday or after-close market tape, theme strength rankings, sector or board money-flow rankings, limit-up pools, institutional survey heat, or a combined read of these signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tsetsugekka](https://clawhub.ai/user/tsetsugekka)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market-analysis agents use this skill to assemble Chinese A-share tape reads from requested modules such as theme strength, board money flow, limit-up pools, intraday flow charts, and institutional survey heat. The skill is for market research and explicitly does not provide investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public external data can refresh local theme data used in financial rankings without strict source pinning.

Mitigation: Review the configured public source before installation, preserve source and timestamp reporting in outputs, and validate refreshed assets before relying on rankings.

Risk: Different market-data sources, timestamps, or statistical windows can produce misleading combined reads.

Mitigation: Keep module outputs labeled with source, data time, unit, and snapshot status, and avoid subtracting or merging values when source or window compatibility is not established.

Risk: The skill can read market or watchlist context through MX tools and cache public market data locally.

Mitigation: Install only when MX access and public-cache behavior are acceptable, and follow the artifact guidance to avoid storing account data, credentials, raw responses, or full watchlists in the repository.

## Reference(s):

- [Intraday Flow Chart SOP](references/intraday-flow-chart-sop.md)
- [Market Tape Source Routing](references/market-tape-source-routing.md)
- [Theme Mainline Lifecycle Lens](references/theme-mainline-lifecycle.md)
- [ClawHub Skill Page](https://clawhub.ai/tsetsugekka/skills/cn-market-tape)
- [Server-Resolved GitHub Provenance](https://github.com/tsetsugekka/codex-market-skills/tree/main/skills/cn-market-tape)
- [Public Theme Data Source](https://daytrading.monster/themes)
- [Theme Lifecycle Reference Article](https://finance.sina.com.cn/wm/2026-06-03/doc-iniaecsk0758056.shtml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese-language Markdown tables, status lines, concise analysis, optional shell commands, optional JSON, and optional CSV file paths from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should identify data time, source, unit, snapshot status, fallback status, and limitations; market-research outputs are not investment advice.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
