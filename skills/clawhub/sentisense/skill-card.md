## Description: <br>
SentiSense is a read-only US stock market data API for AI agents covering real-time prices, news and social sentiment, the SentiSense Score, insider Form 4 trades, congressional STOCK Act disclosures, institutional 13F holdings and flows, options positioning, analyst ratings, earnings, and AI-generated market insights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI agents use this skill to query SentiSense's read-only US equities data for market research, dashboards, watchlists, sentiment monitoring, and stock analysis. It is intended for informational workflows, not trading execution or investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent receives access to a SentiSense API key and can query SentiSense financial data. <br>
Mitigation: Install only when that access is intended, store SENTISENSE_API_KEY in the agent environment, and rotate or revoke the key if exposure is suspected. <br>
Risk: Financial data, sentiment, and AI-generated market insights may be mistaken for investment advice. <br>
Mitigation: Treat results as informational only; do not use this skill to provide personalized recommendations, solicit transactions, or execute trades. <br>
Risk: Free and paid API tiers have quota, rate, and preview limitations that can produce partial or limited responses. <br>
Mitigation: Handle quota and preview responses explicitly, disclose partial data in downstream summaries, and avoid assuming a preview response is complete. <br>


## Reference(s): <br>
- [SentiSense API documentation](https://sentisense.ai/docs/api/) <br>
- [SentiSense website](https://sentisense.ai) <br>
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with endpoint guidance and curl, Python, or JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; outputs are informational financial data and analysis, not investment advice.] <br>

## Skill Version(s): <br>
2.8.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
