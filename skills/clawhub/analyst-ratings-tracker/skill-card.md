## Description:

Tracks Wall Street analyst coverage, price targets, rating changes, per-analyst call history, post-earnings reactions, and comparisons with SentiSense sentiment for supported U.S. stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and developers use this skill to fetch read-only analyst ratings, price targets, rating changes, analyst call history, and SentiSense sentiment context for equity research questions. It is for educational market context, not trading, portfolio management, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the SentiSense API key to SentiSense and can consume API quota.

Mitigation: Keep SENTISENSE_API_KEY in the environment, send it only to app.sentisense.ai, and monitor quota and rate-limit responses.

Risk: Financial research outputs could be mistaken for personalized investment advice.

Mitigation: Present outputs as educational market context, avoid buy or sell recommendations, and separate dated facts from interpretation.

Risk: Free-tier preview responses can truncate firm lists or histories.

Mitigation: Label preview responses, report available denominators and total counts, and avoid treating displayed rows as the full dataset.

Risk: Analyst data may be delayed or refreshed on a drifting daily schedule.

Mitigation: Use returned timestamps such as updatedAt, actionDate, and publishedDate, and avoid implying real-time coverage.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/analyst-ratings-tracker)
- [SentiSense Homepage](https://sentisense.ai)
- [SentiSense API Host](https://app.sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Markdown, Shell commands]

**Output Format:** [Markdown with REST endpoint examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SentiSense API usage; requires SENTISENSE_API_KEY and network access to app.sentisense.ai.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
