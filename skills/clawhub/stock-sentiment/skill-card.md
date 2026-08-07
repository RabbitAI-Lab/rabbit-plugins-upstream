## Description: <br>
Sentiment and smart-money positioning for US stocks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve SentiSense stock sentiment, market mood, smart-money positioning, analyst activity, earnings context, and sentiment-tagged news for US equities. Outputs should be used as educational market context, not personalized investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent needs access to a SentiSense API key to make authenticated requests. <br>
Mitigation: Store the key in SENTISENSE_API_KEY, send it only in the X-SentiSense-API-Key header, and do not place it in query strings or user-facing output. <br>
Risk: Stock sentiment, smart-money, and AI insight outputs may be mistaken for personalized financial advice. <br>
Mitigation: Frame outputs as educational market context and avoid buy, sell, order-entry, portfolio-management, or personalized recommendation language. <br>
Risk: Batch sentiment and insight values can be confused with real-time market data. <br>
Mitigation: Label batch-derived values with their freshness or generatedAt time and keep them distinct from real-time quote or chart data. <br>
Risk: API quota or rate limits can interrupt workflows. <br>
Mitigation: Respect 429 Retry-After responses and surface preview or truncation states rather than retrying aggressively or serving stale values. <br>


## Reference(s): <br>
- [SentiSense API Schema](https://sentisense.ai/skill.md) <br>
- [SentiSense Homepage](https://sentisense.ai) <br>
- [SentiSense API Key Setup](https://app.sentisense.ai/get-api-key) <br>
- [ClawHub Skill Listing](https://clawhub.ai/thesentitrader/skills/stock-sentiment) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Shell commands, Code, Guidance] <br>
**Output Format:** [Markdown summaries with optional JSON snippets, shell commands, and Python helper output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for authenticated read-only requests to app.sentisense.ai.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
