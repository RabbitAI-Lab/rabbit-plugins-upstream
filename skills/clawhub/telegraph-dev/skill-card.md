## Description: <br>
Telegraph Protocol lets agents route verified AI inference, signal lookup, content-authenticity checks, and paid x402 USDC inference calls through a configured Telegraph MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xwick](https://clawhub.ai/user/0xwick) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to access Telegraph-routed inference for weather, authenticity checks, language tasks, image generation, embeddings, and autonomous signal monitoring. It is intended for environments where the Telegraph MCP server is configured and the user accepts wallet-backed x402 payment behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can route agent requests through Telegraph services and may trigger wallet-backed USDC payments. <br>
Mitigation: Install only when Telegraph-routed inference is intended, fund a burner wallet with a small balance, and require approval before paid calls when the agent setup supports it. <br>
Risk: A private key is needed by the local MCP server for signed x402 payment authorizations. <br>
Mitigation: Avoid main wallet keys and keep the key scoped to the local MCP server environment. <br>


## Reference(s): <br>
- [Telegraph Protocol documentation](https://docs.telegraphprotocol.com) <br>
- [Telegraph MCP repository](https://github.com/telegraphprotocol/telegraph-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Configuration guidance] <br>
**Output Format:** [Markdown responses with MCP tool calls and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May initiate paid x402 USDC requests through the configured Telegraph MCP server; requires mcpServers.telegraph and a funded burner wallet.] <br>

## Skill Version(s): <br>
1.1.0 (source: server evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
