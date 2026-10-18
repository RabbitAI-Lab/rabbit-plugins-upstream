## Description:

Guides agents through read-only SentiSense data to summarize analyst coverage, ratings, price targets, rating changes, and comparisons with crowd sentiment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, researchers, and developers use this skill to review published analyst activity and price targets for US stocks, compare them with sentiment, and explain post-earnings reactions. Results are informational, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker queries and the API key are sent to SentiSense over HTTPS.

Mitigation: Use only if comfortable sharing those data with SentiSense; review the separate onboarding flow before requesting a temporary key.

Risk: Financial data or limited free-tier previews could be mistaken for a complete picture or trading advice.

Mitigation: Label preview slices, include dates and denominators, and present findings as informational research rather than recommendations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/analyst-ratings-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dated findings with source windows and preview limitations; no trades or account changes.]

## Skill Version(s):

1.1.6 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
