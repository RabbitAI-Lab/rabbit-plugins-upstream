## Description: <br>
Free Bitcoin AI: live BTC price, halving 2028, Fear & Greed, predictions. Lightning: welove@blink.sv <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[welove111](https://clawhub.ai/user/welove111) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent builders use this skill to retrieve Bitcoin market data, halving information, market signals, predictions, and donation details through the BTCvision MCP/A2A endpoint. Review the bundled search-intelligence toolkit before installation if only Bitcoin market functionality is intended. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release bundles an unrelated OSINT and security-search toolkit alongside the Bitcoin oracle. <br>
Mitigation: Review the artifact contents before installation and remove or avoid the search-intelligence-skill folder if only Bitcoin market data is intended. <br>
Risk: The bundled search toolkit can support security-search and OSINT workflows that may affect third-party targets or personal data. <br>
Mitigation: Use search and OSINT capabilities only for authorized targets, and do not submit secrets or personal data. <br>
Risk: The skill can surface donation prompts and Lightning invoice details during agent conversations. <br>
Mitigation: Require explicit user confirmation before any wallet registration, payment, or donation-related action. <br>
Risk: Bitcoin predictions and market-signal summaries may be incomplete, stale, or unsuitable for financial decisions. <br>
Mitigation: Present market outputs as informational context and require independent review before financial action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/welove111/skills/btcvision-oracle) <br>
- [BTCvision homepage](https://btc-vision.org) <br>
- [BTCvision MCP endpoint](https://btc-vision.org/.netlify/functions/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown or plain text responses with optional MCP tool results and generated Lightning invoice details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live market data, market-signal summaries, Bitcoin prediction text, donation information, and search-result context from the bundled search toolkit.] <br>

## Skill Version(s): <br>
2.2.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
