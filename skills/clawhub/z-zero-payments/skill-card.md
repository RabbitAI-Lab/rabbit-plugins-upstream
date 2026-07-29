## Description: <br>
Pay for things safely from your agent using gasless USDC on Base and JIT single-use virtual cards via the Z-Zero MCP server, with card data kept out of model context and explicit human approval required before payment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dempty-glitch](https://clawhub.ai/user/dempty-glitch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent complete approved purchases with Z-Zero payments while keeping card details out of model context. It supports gasless USDC on Base and single-use virtual-card checkout flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This skill gives an agent real payment capability. <br>
Mitigation: Install it only for agents authorized to make purchases, verify the final merchant and total, and require explicit human approval before payment. <br>
Risk: A compromised or exposed Z-Zero key could allow unwanted access from an untrusted agent environment. <br>
Mitigation: Keep Z_ZERO_API_KEY protected and revoke or rotate the Z-Zero key if the machine or agent environment is no longer trusted. <br>
Risk: A purchase can exceed the operator's intended spend if the final total changes during checkout. <br>
Mitigation: Set clear spending caps and abort if the final merchant or total, including shipping, differs from what the operator approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dempty-glitch/skills/z-zero-payments) <br>
- [Z-Zero homepage](https://z-zero.xyz) <br>
- [Z-Zero agent dashboard](https://z-zero.xyz/dashboard/agents) <br>
- [z-zero-mcp-server on npm](https://www.npmjs.com/package/z-zero-mcp-server) <br>
- [Base mainnet transfer proof](https://basescan.org/tx/0xdfd1f2f824e1232c3e03c52485332570ff01fbb0340c5571f699ed1218735d7a) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and payment status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npx and Z_ZERO_API_KEY; payments require explicit human approval.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
