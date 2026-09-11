## Description:

Research app-market opportunities using Crawlora app catalogs, historical charts, live store listings, release notes, reviews, and Google Trends. Use for app niche assessments, competitor maps, chart-movement analysis, and evidence-backed unmet-need hypotheses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and market researchers use this skill to assess app niches, compare competitors, inspect chart movement and release activity, review customer feedback, and form evidence-backed unmet-need hypotheses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends app-market research terms, app IDs, review queries, Trends requests, and a Crawlora API key to Crawlora.

Mitigation: Use a Crawlora-scoped API key, keep it in the environment, and avoid placing unrelated secrets or sensitive data in request parameters or bodies.

Risk: App-store ranks, review samples, and Google Trends scores can be mistaken for market size, revenue, installs, or population-level prevalence.

Mitigation: Keep data freshness, sampling bounds, missing-data flags, source limits, assumptions, and conflicting evidence visible in opportunity briefs.

Risk: Shell commands generated around the helper can make external requests to the documented Crawlora API.

Mitigation: Review commands before execution and use only the skill's documented endpoint set for this app-market research workflow.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Google Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/app-market-opportunity-research)
- [ClawHub publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces opportunity briefs that should preserve data freshness, sampling bounds, unknowns, conflicting evidence, and assumptions.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
