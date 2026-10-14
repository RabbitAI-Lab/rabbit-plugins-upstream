## Description:

Research app-market opportunities using Crawlora app catalogs, chart history, store listings, release notes, reviews, and Google Trends to develop evidence-backed niche assessments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and market researchers use the skill to compare competing apps, chart movements, updates, and customer feedback, then frame app-niche opportunities as testable hypotheses rather than demand or revenue forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App research queries and the Crawlora API key are sent to Crawlora.

Mitigation: Confirm this data sharing is acceptable before use; keep the API key out of logs, commits, and shared shell history.

Risk: An unintended country or language can make app and trend comparisons misleading.

Mitigation: Set country and language deliberately and report the selected locale with the findings.

Risk: Rankings, selected reviews, and relative Trends scores can be mistaken for market size or proven demand.

Mitigation: Compare like-for-like data, disclose sampling and freshness limits, and present opportunities as hypotheses requiring validation.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Google Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown opportunity brief with competitor comparisons, supporting and conflicting evidence, and validation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes data freshness, sample bounds, assumptions, and unknowns.]

## Skill Version(s):

1.0.10 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
