## Description:

Summarizes sampled Reddit discussion about a public company or ticker, with optional same-window Yahoo Finance price context, without treating sentiment as a trading signal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and researchers use this skill to review sampled public Reddit discussion about a verified security and compare themes with dated price context when useful. The brief distinguishes discussion from evidence and does not give trading advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker, company, and subreddit searches are sent to Crawlora using an API key.

Mitigation: Avoid confidential watchlists, private investment plans, and sensitive research terms in queries.

Risk: Sampled Reddit posts can misrepresent broader investor views or repeat unverified claims.

Mitigation: Report sampling limits and source links, verify factual claims, and do not present discussion as a forecast or trading recommendation.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/reddit-stock-sentiment-research)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown research brief with a theme table and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sample counts, coverage limits, and optional dated price context; not investment advice.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
