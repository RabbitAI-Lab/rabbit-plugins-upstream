## Description: <br>
Pay for things safely from your agent - gasless USDC on Base plus JIT single-use virtual cards via the Z-Zero MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dempty-glitch](https://clawhub.ai/user/dempty-glitch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent prepare payment flows through the Z-Zero MCP server while keeping card data out of model context. It is intended for gasless USDC payments on Base and just-in-time single-use virtual card checkout flows that require human confirmation before spending. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill delegates real money movement to an external MCP package, and the security evidence says the runtime flow can execute payments without a clearly enforced human-approval gate. <br>
Mitigation: Use low spending caps, confirm the exact final amount yourself, and require approval before allowing auto_pay_checkout or any payment tool to run. <br>
Risk: Using an unpinned npm package can change the payment runtime between installs. <br>
Mitigation: Prefer a pinned z-zero-mcp-server package version instead of @latest and review the installed package before deployment. <br>


## Reference(s): <br>
- [Z-Zero homepage](https://www.clawcard.store) <br>
- [Z-Zero agent dashboard](https://www.clawcard.store/dashboard/agents) <br>
- [z-zero-mcp-server on npm](https://www.npmjs.com/package/z-zero-mcp-server) <br>
- [Base mainnet transfer proof](https://basescan.org/tx/0xdfd1f2f824e1232c3e03c52485332570ff01fbb0340c5571f699ed1218735d7a) <br>
- [ClawHub skill listing](https://clawhub.ai/dempty-glitch/skills/z-zero-payments) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, text] <br>
**Output Format:** [Markdown with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires npx and Z_ZERO_API_KEY; payment actions should be reviewed with low spending caps and explicit final-amount confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
