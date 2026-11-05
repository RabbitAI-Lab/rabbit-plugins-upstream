## Description:

Retrieves read-only analyst coverage, price targets, rating changes, and call histories for tracked U.S. stocks, with optional comparisons to SentiSense sentiment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to answer questions about analyst coverage, price targets, rating changes, and analyst history, and to compare analyst views with SentiSense sentiment. Results are informational research, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live research queries are sent to SentiSense, and API requests consume quota.

Mitigation: Use ticker-only queries where possible and avoid sending personal or confidential information; limit repeat calls to those needed for the requested research.

Risk: Free-tier results may be incomplete previews, and analyst data refreshes about once daily.

Mitigation: Identify preview responses and check response timestamps before summarizing; describe the available data as informational context, not a recommendation.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/#full-sample-responses-with-a-free-key)
- [Get a SentiSense API key](https://app.sentisense.ai/get-api-key)
- [Analyst Ratings Tracker on ClawHub](https://clawhub.ai/thesentitrader/skills/analyst-ratings-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise Markdown research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Informational only; distinguish free preview data and include relevant dates and coverage counts. Not personalized investment advice.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
