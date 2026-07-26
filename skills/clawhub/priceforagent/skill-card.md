## Description: <br>
Get real-time prices for crypto, stocks, and commodities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edibez](https://clawhub.ai/user/edibez) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent builders use this skill to check crypto, stock, and commodity prices through natural-language queries or direct asset lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Natural-language price queries may include sensitive portfolio holdings, trading plans, account details, or other personal information. <br>
Mitigation: Avoid sending sensitive personal or financial details in queries to the price API. <br>
Risk: The generated API key could be exposed through logs, shared prompts, or committed configuration. <br>
Mitigation: Keep the API key private and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/edibez/skills/priceforagent) <br>
- [Price for Agent API](https://p4ai.bitharga.com) <br>
- [OpenAPI Specification](https://p4ai.bitharga.com/v1/openapi.yaml) <br>
- [Function Schema](https://p4ai.bitharga.com/v1/function-schema) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with API request examples and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a generated API key for price requests; responses include asset, price, bid, ask, currency, market status, and timestamp when returned by the API.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
