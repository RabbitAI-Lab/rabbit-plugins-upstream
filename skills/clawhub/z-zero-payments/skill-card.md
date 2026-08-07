## Description: <br>
Pay for things safely from your agent — gasless USDC on Base plus JIT single-use virtual cards via the Z-Zero MCP server. Card data never enters the model context, and no payment executes without explicit human approval. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dempty-glitch](https://clawhub.ai/user/dempty-glitch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent assist with real purchases through the Z-Zero MCP server while keeping payment credentials out of model context and requiring explicit human approval before checkout. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can assist with real purchases and money movement. <br>
Mitigation: Install only when that capability is intended, show the final total to the operator, and wait for explicit approval before checkout. <br>
Risk: The Z-Zero API key grants access to payment tooling. <br>
Mitigation: Keep the API key protected and provide it through the configured Z_ZERO_API_KEY environment variable. <br>
Risk: The release depends on an external MCP server package. <br>
Mitigation: Review the MCP server and package source before deployment, as recommended by the server security guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dempty-glitch/skills/z-zero-payments) <br>
- [Z-Zero homepage](https://z-zero.xyz) <br>
- [Z-Zero agent dashboard](https://z-zero.xyz/dashboard/agents) <br>
- [z-zero-mcp-server npm package](https://www.npmjs.com/package/z-zero-mcp-server) <br>
- [Base mainnet payment proof](https://basescan.org/tx/0xdfd1f2f824e1232c3e03c52485332570ff01fbb0340c5571f699ed1218735d7a) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown instructions with JSON configuration examples and command references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npx and Z_ZERO_API_KEY; payment actions require explicit human approval.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
