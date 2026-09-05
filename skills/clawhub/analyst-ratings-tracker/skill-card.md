## Description:

Tracks Wall Street analyst coverage, price targets, rating changes, per-analyst call history, Street-versus-crowd comparisons, and post-earnings analyst reactions through the read-only SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, investors, and agent developers use this skill to retrieve read-only analyst ratings, price-target consensus, coverage, market-wide upgrades and downgrades, analyst history, and sentiment comparison for US stocks. It is for informational research context, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stock-query requests are sent to SentiSense with the user's API key.

Mitigation: Install only if that data sharing is acceptable, and use SENTISENSE_API_KEY environment-variable authentication when avoiding local CLI credential storage is preferred.

Risk: Analyst ratings and sentiment output could be mistaken for investment advice.

Mitigation: Treat the output as research context and keep responses informational rather than personalized buy, sell, or portfolio guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/analyst-ratings-tracker)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API application](https://app.sentisense.ai)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with optional shell commands, REST API examples, and JSON output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SentiSense API requests authenticated with SENTISENSE_API_KEY; output may reflect free-tier preview limits and rate limits.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
