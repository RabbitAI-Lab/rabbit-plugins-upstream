## Description:

Provides AI agents with read-only access to U.S. stock market data, sentiment, filings, institutional activity, options, analyst coverage, earnings, and market insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use the skill to retrieve and summarize stock prices, sentiment, filings, institutional activity, options, analyst data, earnings, and market insights through the SentiSense API. Results are informational and do not place trades or make purchases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags setup that executes an unpinned npm package and provisions an API key, while the skill describes its data calls as read-only. The scanner did not establish harmful intent, and its coverage is incomplete.

Mitigation: Before using the setup command, review and decide whether to trust the npm package and its key-provisioning behavior. If you do not want to execute the package, use an existing API key or the documented HTTPS provisioning path, and keep any key and keep link private.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API key page](https://app.sentisense.ai/get-api-key)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense)

## Skill Output:

**Output Type(s):** [text, JSON, guidance, API calls]

**Output Format:** [Read-only API requests and JSON data, summarized as text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Informational market data; results depend on API access tier, coverage, quotas, and rate limits.]

## Skill Version(s):

2.30.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
