## Description:

Summarizes analyst coverage, ratings, price targets, rating changes, and sentiment comparisons for stocks tracked by SentiSense.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, researchers, and agents use this skill to review published analyst opinions and price targets for tracked US-listed stocks and ADRs, compare them with current sentiment, and summarize rating activity without placing trades or giving personalized advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker and research queries are sent to SentiSense with an API key.

Mitigation: Use the skill only if sharing these queries with SentiSense is acceptable, and protect the API key.

Risk: Market research may be mistaken for investment advice or a prediction.

Mitigation: Present results as dated informational research, not personalized buy or sell recommendations.

Risk: A separate onboarding flow can provision a temporary API key.

Mitigation: Approve that flow only after reviewing and trusting it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/analyst-ratings-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dated, source-attributed market research; free-tier responses may contain preview slices.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
