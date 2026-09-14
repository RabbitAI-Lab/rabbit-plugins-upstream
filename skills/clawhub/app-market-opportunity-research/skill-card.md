## Description:

Research app-market opportunities using Crawlora app catalogs, historical charts, live store listings, release notes, reviews, and Google Trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Product, growth, and app-development teams use this skill to assess app niches, compare competitors, inspect chart movement, sample reviews, and form evidence-backed unmet-need hypotheses. It helps separate opportunity hypotheses from demonstrated demand, market size, and revenue forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends app-market research queries, review searches, Trends requests, and the Crawlora API key to Crawlora.

Mitigation: Use a dedicated Crawlora API key, keep it in the environment, and avoid putting unrelated secrets or private local data into query or POST bodies.

Risk: Chart ranks, review samples, Android install bands, and Google Trends scores can be mistaken for market size, revenue, active users, or absolute demand.

Mitigation: Preserve sampling bounds and freshness notes, compare only like-for-like chart definitions, and present opportunity claims as hypotheses with supporting and conflicting evidence.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Google Trends data FAQ](https://support.google.com/trends/answer/4365533?hl=en)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown opportunity brief with competitor matrices, chart trajectories, review themes, assumptions, and validation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded Crawlora API command examples and concise excerpts from app-store evidence.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
