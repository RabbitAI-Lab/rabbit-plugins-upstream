## Description:

Builds a single self-contained HTML stock market dashboard from read-only SentiSense market-data API calls, including market mood, sentiment, options, watchlist, flows, stories, analyst moves, and earnings context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and market researchers use this skill to generate a local morning market briefing dashboard from SentiSense data. The dashboard is intended for research and informational review, not trading, account management, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dashboard may be mistaken for personalized investment advice or a trading recommendation.

Mitigation: State that outputs are research and educational information only, include the required investment disclaimer, and avoid buy, sell, target, prediction, or top-pick language.

Risk: The generated HTML can become stale because data is fetched once and baked into a local file.

Mitigation: Show the generation timestamp, label field-level freshness, and describe the file as a snapshot rather than a live view.

Risk: The SentiSense API key could be exposed if it is written into the generated dashboard.

Mitigation: Use the API key only for read-only requests during generation and do not embed secrets in the HTML output.

Risk: Market-data fields can be misread when score scales, missing values, delayed prices, or partial filing coverage are not labeled.

Mitigation: Apply the documented SentiSense score scale, distinguish missing values from zero readings, label delayed or batch data, and report partial 13F coverage without inferring motive or magnitude.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-market-dashboard)
- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Code, Files, Configuration]

**Output Format:** [Markdown guidance and generated self-contained HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; generated dashboards are offline snapshots with data baked in at generation time.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
