## Description: <br>
Inspect and simulate Clicks Protocol settlement routing for AI agents on Base. Use read-only MCP calls for settlement state, split previews, optional yield routing, and attribution stats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[protogenosone](https://clawhub.ai/user/protogenosone) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent builders use this skill to inspect Clicks Protocol settlement state, preview USDC split routing, review yield and referral status, and plan post-payment treasury policy before any signed on-chain action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is finance-adjacent and queries live protocol information through a remote MCP endpoint. <br>
Mitigation: Treat results as read-only status or simulation output, and confirm live state separately before any transaction decision. <br>
Risk: Related SDK or local MCP write flows can involve USDC-moving transactions when separately connected to a signer. <br>
Mitigation: Keep signing outside this skill and require explicit human review of chain, contract, method, asset, amount, recipient, fees, and expected state change before submission. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/protogenosone/skills/clicks-protocol) <br>
- [Clicks Protocol Website](https://clicksprotocol.xyz) <br>
- [Contract Reference](references/contracts.md) <br>
- [SDK Package](https://www.npmjs.com/package/@clicks-protocol/sdk) <br>
- [MCP Server Package](https://www.npmjs.com/package/@clicks-protocol/mcp-server) <br>
- [OpenAPI Specification](https://clicksprotocol.xyz/api/openapi.json) <br>
- [Agent Metadata](https://clicksprotocol.xyz/.well-known/agent.json) <br>
- [ERC-8004 Registration](https://clicksprotocol.xyz/.well-known/agent-registration.json) <br>
- [LLMs Reference](https://clicksprotocol.xyz/llms.txt) <br>
- [Attestor Schema V1](https://clicksprotocol.xyz/strategy/ATTESTOR-SCHEMA-V1.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-like MCP responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; uses read-only remote MCP calls and does not handle private keys or sign transactions.] <br>

## Skill Version(s): <br>
1.2.7 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
