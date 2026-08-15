## Description:

Stock terminal for AI agents. Turns chat into a futuristic financial terminal: typed commands like "open NVDA", "screen smart-money", "daily brief", or natural questions like "what's hot today?" return composite synthesized reports across price, sentiment, insider trades, congressional disclosures, institutional flows, analyst ratings, AI insights, and embedded news. Use for stock terminal, financial terminal for AI, daily market brief, open a ticker, screen stocks by smart money, what is hot today, one-command stock research. Read-only. No trading, no purchases, no write operations, no wallet access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn natural-language stock research requests into read-only financial terminal responses that synthesize market data, sentiment, smart-money flows, analyst signals, AI insights, and embedded news.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an API key for read-only SentiSense market-data calls.

Mitigation: Provide only a SentiSense API key intended for market-data reads, keep it in the host environment, and avoid placing it in chat or generated artifacts.

Risk: Optional news-title and social embed enrichment can touch external URLs when enabled.

Mitigation: Use the hardened fetcher described by the skill, or prefer slug-title fallback and sanitized cards in privacy-sensitive environments.

Risk: Financial terminal responses could be mistaken for personalized investment advice.

Mitigation: Keep responses educational and data-grounded, preserve the read-only posture, and avoid personal buy, sell, or trading recommendations.

## Reference(s):

- [SentiSense Homepage](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-terminal)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with inline code, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only financial research responses; requires SENTISENSE_API_KEY for authenticated data calls.]

## Skill Version(s):

1.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
