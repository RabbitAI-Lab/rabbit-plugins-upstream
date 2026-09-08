## Description:

Produces an auditable 30-day US equities research brief from SentiSense market mood, story-cluster, insight, market-summary, and earnings API data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and market researchers use this skill to catch up on the prior month in US equities with dated, sourced market-mood, story-cluster, signal, and earnings context. It is intended for research and education, not investment advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends a required API key to SentiSense over HTTPS for read-only market data calls.

Mitigation: Provide SENTISENSE_API_KEY through the runtime environment, avoid logging it, and keep use scoped to app.sentisense.ai.

Risk: Market briefs could be mistaken for investment advice or could overstate what the fetched data supports.

Mitigation: Keep claims tied to fetched responses, include coverage windows and the fixed financial disclaimer, and avoid recommendations to buy or sell securities.

Risk: Generated briefs include SentiSense attribution, external links, and provider-specific formatting.

Mitigation: Review those output requirements before deployment when provider branding or external links are restricted.

Risk: Rate limits, quota limits, preview caps, or incomplete endpoint responses can leave parts of the month uncovered.

Mitigation: Honor Retry-After on per-minute limits, stop retrying on quota exhaustion, and state missing or preview-limited layers in the coverage line.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/last-30-days-in-markets)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense website](https://sentisense.ai)
- [SentiSense skill API reference](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Guidance]

**Output Format:** [Markdown research brief with dated event lines, tables, coverage notes, attribution, and financial disclaimer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and read-only HTTPS access to app.sentisense.ai; performs no trades, purchases, wallet access, or account modifications.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
