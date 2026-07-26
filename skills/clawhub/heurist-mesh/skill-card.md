## Description: <br>
Real-time crypto token data, DeFi analytics, blockchain data, Twitter/X social intelligence, enhanced web search, and crypto project search in one skill. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wjw12](https://clawhub.ai/user/wjw12) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users can use this skill to guide agents through Heurist Mesh setup, payment configuration, schema discovery, and crypto analytics requests. It supports token, DeFi, wallet, Twitter/X, web-search, project, and research workflows through Heurist Mesh APIs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to access paid Heurist services. <br>
Mitigation: Require explicit user approval before paid requests and confirm available credits, price, agent, and tool before each call. <br>
Risk: The skill includes wallet private-key and crypto-signing flows for x402 payments. <br>
Mitigation: Prefer API-key credits when possible; if x402 is used, use a dedicated low-balance wallet and verify network, recipient, and amount before signing. <br>
Risk: Payment credentials stored in `.env` could be exposed if committed or shared. <br>
Mitigation: Keep `.env` out of source control and avoid printing or pasting secrets into chat, logs, or generated files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wjw12/skills/heurist-mesh) <br>
- [Heurist Mesh](https://mesh.heurist.ai) <br>
- [Heurist API documentation](https://docs.heurist.ai) <br>
- [Heurist API Key](references/heurist-api-key.md) <br>
- [x402 On-Chain Payment](references/x402-payment.md) <br>
- [Inflow Payment Platform](references/inflow-payment.md) <br>
- [Heurist Mesh schema endpoint](https://mesh.heurist.xyz/mesh_schema?agent_id=TokenResolverAgent&agent_id=CoinGeckoTokenInfoAgent) <br>
- [x402-enabled agents](https://mesh.heurist.xyz/x402/agents) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, API calls, Analysis] <br>
**Output Format:** [Markdown with inline bash, JSON, and TypeScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to call paid Heurist Mesh services after credentials and user approval are confirmed.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
