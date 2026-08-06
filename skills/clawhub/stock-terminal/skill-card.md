## Description: <br>
Stock terminal for AI agents. Turns chat into a futuristic financial terminal: typed commands like "open NVDA", "screen smart-money", "daily brief", or natural questions like "what's hot today?" return composite synthesized reports across price, sentiment, insider trades, congressional disclosures, institutional flows, analyst ratings, AI insights, and embedded news. Use for stock terminal, financial terminal for AI, daily market brief, open a ticker, screen stocks by smart money, what is hot today, one-command stock research. Read-only. No trading, no purchases, no write operations, no wallet access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesentitrader](https://clawhub.ai/user/thesentitrader) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and market-research agents use this skill to turn natural-language stock questions and short commands into read-only financial-terminal reports. It supports educational market research across prices, sentiment, smart-money flows, analyst ratings, AI insights, and news without trading or write access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SentiSense API key and can spend API quota on market-data lookups. <br>
Mitigation: Install only where the host is allowed to use SENTISENSE_API_KEY, keep the key in host configuration, and monitor quota use. <br>
Risk: Generic prompts such as "what's hot today" or "what's the news" may route to this financial terminal in a multi-skill agent. <br>
Mitigation: Configure the host to require finance or market context before invoking stock-terminal for generic news or trend requests. <br>
Risk: Market summaries can be mistaken for investment advice. <br>
Mitigation: Preserve the skill's read-only and educational framing, and avoid personal buy, sell, or trading recommendations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-terminal) <br>
- [SentiSense website](https://sentisense.ai) <br>
- [SentiSense API reference](https://sentisense.ai/skill.md) <br>
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with terminal-style reports, inline commands, API examples, and implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only outputs; requires SENTISENSE_API_KEY for SentiSense market-data calls; no trading, purchasing, write operations, or wallet access.] <br>

## Skill Version(s): <br>
1.5.1 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
