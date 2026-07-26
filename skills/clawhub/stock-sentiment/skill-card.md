## Description: <br>
Sentiment and smart-money positioning for US stocks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and finance-focused agents use this skill to retrieve SentiSense sentiment, market mood, smart-money positioning, analyst activity, AI insights, and sentiment-tagged news for US equities. Outputs should be synthesized as educational market context, not personalized buy or sell advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SentiSense API key and outbound requests to app.sentisense.ai. <br>
Mitigation: Store the key in SENTISENSE_API_KEY, keep it out of prompts and shared logs, and allow only the documented SentiSense endpoint when network egress is controlled. <br>
Risk: Market sentiment and smart-money outputs could be mistaken for personalized financial advice. <br>
Mitigation: Frame responses as educational market context and avoid buy, sell, portfolio, or order-entry recommendations. <br>
Risk: Some sentiment, news, and AI insight surfaces are batch metrics rather than real-time values. <br>
Mitigation: Label batch freshness when available and keep real-time quote data distinct from batch sentiment signals. <br>


## Reference(s): <br>
- [SentiSense](https://sentisense.ai) <br>
- [SentiSense Skill API Reference](https://sentisense.ai/skill.md) <br>
- [SentiSense API Key](https://app.sentisense.ai/get-api-key) <br>
- [Stock Sentiment on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-sentiment) <br>
- [Publisher Profile](https://clawhub.ai/user/thesentitrader) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown with sourced market context, optional JSON from API calls, and inline shell or Python commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and outbound HTTPS access to app.sentisense.ai; responses are read-only market data and should preserve batch freshness labels when available.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
