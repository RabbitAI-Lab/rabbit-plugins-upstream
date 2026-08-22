## Description:

US stock market data API for AI agents: news and social sentiment, the SentiSense Score, insider Form 4 trades, congressional STOCK Act disclosures, institutional 13F holdings and flows, options positioning, analyst ratings, the earnings calendar, AI-generated market insights, and stock prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI agents use this skill to retrieve read-only U.S. equity market data, sentiment, filings, options, analyst, earnings, and pricing signals from the SentiSense API. The skill supports research workflows and dashboard-style market analysis, not trade execution or investment recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key, and optional CLI authentication can store the key in a local configuration file.

Mitigation: Prefer direct REST calls with SENTISENSE_API_KEY in the environment, avoid storing keys on shared machines, and rotate or revoke exposed keys.

Risk: Optional npx, npm, pip, CLI, or SDK use runs third-party local code.

Mitigation: Use direct REST calls when possible; if local packages are used, review source code first and prefer the pinned CLI version shown in the skill.

Risk: Market data and AI-generated analysis may be mistaken for live trading guidance or investment advice.

Mitigation: Present outputs as informational only, respect documented data freshness such as delayed prices, and avoid using the skill for trade execution or personalized recommendations.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Documentation](https://sentisense.ai/docs/api/)
- [SentiSense API Key Management](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [Python SDK](https://github.com/SentiSenseApp/sentisense)
- [Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with inline HTTP, curl, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only API usage; responses may include JSON market data and preview wrappers depending on endpoint and account tier.]

## Skill Version(s):

2.12.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
