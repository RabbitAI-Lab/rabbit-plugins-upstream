## Description:

Trading analysis framework for XAU/USD, forex, gold, and crypto chart analysis that supports multi-timeframe structure, liquidity concepts, entry checklists, trade reviews, market bias, data checks, and memory schemas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading-analysis agents use this skill to structure market-analysis conversations, fetch supporting market, calendar, and correlation data, produce candidate entry plans, run pre-trade checklists, and review trades while leaving final decisions to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist trading history, generated journals, reports, and private strategy context in local trading-memory files.

Mitigation: Use it only in trusted workspaces, review stored files before sharing, and avoid placing sensitive strategy notes on shared machines.

Risk: The skill can read plaintext API-key material from local trading memory and make outbound market or scraping API requests.

Mitigation: Use scoped keys, prefer environment-based secret handling where available, and review configured endpoints before running data-fetching scripts.

Risk: The continuous XAU monitor can create background-style logging and repeated network activity.

Mitigation: Use one-shot or manual workflows unless continuous monitoring is intentional, and stop scheduled or monitor processes after use.

Risk: The security summary reports an HTTPS helper that disables certificate checks.

Mitigation: Fix TLS verification before relying on fetched data or using the skill in security-sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/trading-analyst)
- [ClawHub publisher profile](https://clawhub.ai/user/pmuhammadagus-byte)
- [Twelve Data time series API](https://api.twelvedata.com/time_series)
- [Firecrawl scrape API](https://api.firecrawl.dev/v1/scrape)
- [CFTC COT data](https://www.cftc.gov/dea/newcot/deafut.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis, checklist guidance, JSON reports, local memory files, and shell command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TWELVE_DATA_API_KEY and FIRECRAWL_API_KEY for full data-layer behavior; curl is declared as a required binary.]

## Skill Version(s):

1.0.1 (source: server release metadata and artifact _meta.json; source SKILL.md frontmatter reports 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
