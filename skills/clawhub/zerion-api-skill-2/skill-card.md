## Description: <br>
Query blockchain wallet data, token prices, and transaction history using the Zerion API via its MCP connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vshamanov](https://clawhub.ai/user/vshamanov) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, developers, and analysts use this skill to ask an agent for Zerion-backed wallet, DeFi, NFT, token-price, PnL, transaction, and dashboard data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Zerion API keys, and the security review flags guidance that can place keys inside prompts sent to another model service. <br>
Mitigation: Use only revocable, low-privilege Zerion API keys; pass credentials through a dedicated connector or secure secret field; avoid prompts, request bodies, files, logs, or generated artifacts that expose the key. <br>


## Reference(s): <br>
- [Wallet Endpoints Reference](references/wallet-endpoints.md) <br>
- [Fungible & NFT Endpoints Reference](references/fungible-nft-endpoints.md) <br>
- [Zerion MCP Server](https://developers.zerion.io/mcp) <br>
- [Zerion API Dashboard](https://dashboard.zerion.io/) <br>
- [ClawHub Skill Release](https://clawhub.ai/vshamanov/skills/zerion-api-skill-2) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with JSON, JavaScript, endpoint, and MCP usage examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Zerion MCP or REST query parameters, parsed response guidance, and dashboard artifact code.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
