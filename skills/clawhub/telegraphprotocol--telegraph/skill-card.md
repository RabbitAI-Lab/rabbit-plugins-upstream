## Description: <br>
Use Telegraph Protocol for verified AI inference across weather and climate data, authenticity checks, LLM completions, image generation, embeddings, AI text detection, autonomous signal monitoring, and x402 USDC-paid inference through the Telegraph MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[telegraphprotocol](https://clawhub.ai/user/telegraphprotocol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to route selected inference, authenticity, weather, signal-monitoring, and payment-enabled AI tasks through the Telegraph MCP server. It is intended for users who explicitly want Telegraph-routed providers or x402 USDC micropayments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User prompts, images, video, or text can be routed to changing third-party AI providers. <br>
Mitigation: Use Telegraph only for data appropriate for those provider paths, inspect the live miner catalog before sensitive requests, and avoid submitting private data unless the current route is trusted. <br>
Risk: Paid inference can spend wallet funds through automatic x402 calls with limited per-call user control. <br>
Mitigation: Configure a burner wallet with a very small balance and avoid using a main wallet or high-value key. <br>


## Reference(s): <br>
- [Telegraph Protocol Documentation](https://docs.telegraphprotocol.com) <br>
- [Telegraph MCP Homepage](https://github.com/telegraphprotocol/telegraph-mcp) <br>
- [ClawHub Skill Page](https://clawhub.ai/telegraphprotocol/skills/telegraph) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with MCP tool names, JSON configuration snippets, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe external MCP tool calls and paid inference routes; actual provider set can change with the live Telegraph miner catalog.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
