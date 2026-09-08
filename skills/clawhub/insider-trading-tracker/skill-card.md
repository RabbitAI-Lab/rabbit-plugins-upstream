## Description:

Track SEC Form 4 insider buying and selling by ticker, market-wide activity, cluster buy signals, and 10b5-1 plan detection through the read-only SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and interpret read-only insider-trading filing data for market research, including ticker-level Form 4 activity, market-wide buying and selling, cluster buys, and scheduled-sale context. Outputs are informational research context, not personalized trading advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SentiSense API key and sends requests to the SentiSense API.

Mitigation: Install only if the user is comfortable sharing the SentiSense API key with that service and restrict network access to app.sentisense.ai.

Risk: Insider-trading filing data can be misread as a buy or sell recommendation.

Mitigation: Treat outputs as informational research context and avoid presenting them as personalized trading advice.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API](https://app.sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/insider-trading-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, API calls, guidance]

**Output Format:** [Markdown with REST endpoint examples and concise analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and network access to app.sentisense.ai; responses should distinguish informational context from trading advice.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
