## Description:

Research app-market opportunities with Crawlora app catalogs, chart history, store listings, release notes, reviews, and Google Trends to develop evidence-backed opportunity hypotheses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Product teams, founders, and market researchers use this skill to compare competing apps, chart movements, release activity, and customer reviews, then frame app-niche opportunities and next validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research requests, app IDs, review queries, and the Crawlora API key are sent to Crawlora.

Mitigation: Keep the API key in the environment and review request parameters before researching sensitive or confidential product ideas.

Risk: Chart ranks, review samples, and normalized Trends scores can overstate market demand when interpreted as downloads, revenue, or population-wide sentiment.

Mitigation: Keep comparisons like-for-like, disclose data freshness and sample limits, and distinguish opportunity hypotheses from validated demand.

## Reference(s):

- [App-market endpoint reference](reference/endpoints.md)
- [Google Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/app-market-opportunity-research)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown opportunity brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes competitor comparisons, supporting and conflicting evidence, data freshness, sampling bounds, and next validation steps.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
