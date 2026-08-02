## Description: <br>
Search live UK marketplace prices and products from any agent, returning normalized product names, prices in GBP, condition, marketplace, and direct purchase URLs for physical products. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fusionx212](https://clawhub.ai/user/fusionx212) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to add live UK physical-product search, price comparison, budget filtering, marketplace selection, and direct purchase-link retrieval to agents. <br>

### Deployment Geography for Use: <br>
United Kingdom <br>

## Known Risks and Mitigations: <br>
Risk: Product searches and filters are sent to fetch-price.com. <br>
Mitigation: Avoid sending personal, confidential, or sensitive details in search queries. <br>
Risk: Returned purchase URLs may include affiliate tracking. <br>
Mitigation: Tell users when links may be affiliate links and have them review destination URLs before buying. <br>
Risk: Paid usage may require an API key. <br>
Mitigation: Use a dedicated FETCH_PRICE_API_KEY with appropriate spending and access controls. <br>
Risk: The skill is limited to live UK physical-product listings and does not support digital goods, services, non-UK marketplaces, or historical price research. <br>
Mitigation: Route unsupported requests elsewhere or clearly explain the limitation to the user. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/fusionx212/skills/sdk) <br>
- [Publisher profile](https://clawhub.ai/user/fusionx212) <br>
- [fetch-price MCP documentation](https://fetch-price.com/docs/mcp) <br>
- [fetch-price pricing](https://fetch-price.com/pricing) <br>
- [fetch-price query API](https://api.fetch-price.com/api/query) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Code, Shell commands, Configuration guidance] <br>
**Output Format:** [Normalized JSON product results with optional Markdown, code, shell command, and configuration guidance for SDK or MCP use] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results include product name, price, currency, condition, marketplace/network, direct purchase URL, and metadata where available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, pyproject.toml, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
