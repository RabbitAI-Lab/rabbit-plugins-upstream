## Description: <br>
Unusual options activity radar for US stocks and ETFs: end-of-day IV rank, implied volatility, options sentiment, put/call percentile, 25-delta skew, open-interest walls, and max pain, each ranked against the ticker's own trailing history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query read-only SentiSense options-market analytics for US stocks and ETFs, then explain unusual activity, IV rank, put/call percentiles, skew, open-interest walls, and max pain in educational terms. It is not for order entry, portfolio management, greeks-based hedging, or personalized investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated requests to SentiSense may consume service quota or hit rate limits. <br>
Mitigation: Keep the API key in an environment variable, stop or back off when quota and rate-limit responses are returned, and disclose preview or quota-limited results. <br>
Risk: Options analytics can be mistaken for personalized trading advice or real-time order-flow data. <br>
Mitigation: Frame outputs as educational, end-of-day market context and avoid buy, sell, forecast, sweep, or account-management recommendations. <br>
Risk: API credentials could be exposed if copied into prompts, URLs, or user-facing answers. <br>
Mitigation: Use the X-SentiSense-API-Key header from the SENTISENSE_API_KEY environment variable and do not print or embed the key in generated output. <br>


## Reference(s): <br>
- [SentiSense](https://sentisense.ai) <br>
- [SentiSense API Key](https://app.sentisense.ai/get-api-key) <br>
- [ClawHub Skill Listing](https://clawhub.ai/thesentitrader/skills/unusual-options-activity) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, guidance] <br>
**Output Format:** [Markdown with concise explanations, sourced API-derived values, and optional shell or Python snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only SentiSense API responses are summarized as educational market context, not trading advice.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
