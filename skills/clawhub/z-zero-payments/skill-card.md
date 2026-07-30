## Description: <br>
Pay for things safely from your agent - gasless USDC on Base plus JIT single-use virtual cards via the Z-Zero MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dempty-glitch](https://clawhub.ai/user/dempty-glitch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent assist with purchases through Z-Zero payment rails while keeping card details out of model context and requiring explicit human approval before payment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables an agent to assist with real payments, which can move funds or commit purchases. <br>
Mitigation: Require explicit human approval for the exact final total before every purchase and abort when approval is missing. <br>
Risk: Payment credentials or card details could be exposed if the workflow is bypassed. <br>
Mitigation: Keep the Z_ZERO_API_KEY protected, use the MCP flow as documented, and do not request or resolve raw card details in model context. <br>
Risk: Unexpected spend can occur if budgets, merchant totals, or checkout status are misunderstood. <br>
Mitigation: Set spending caps where available, verify the final total including shipping, and report the returned payment status accurately. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dempty-glitch/skills/z-zero-payments) <br>
- [Z-Zero homepage](https://z-zero.xyz) <br>
- [Z-Zero agent dashboard](https://z-zero.xyz/dashboard/agents) <br>
- [z-zero-mcp-server npm package](https://www.npmjs.com/package/z-zero-mcp-server) <br>
- [Base mainnet gasless USDC transfer proof](https://basescan.org/tx/0xdfd1f2f824e1232c3e03c52485332570ff01fbb0340c5571f699ed1218735d7a) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with inline JSON and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npx and Z_ZERO_API_KEY; produces payment workflow guidance and MCP configuration instructions rather than card data.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
