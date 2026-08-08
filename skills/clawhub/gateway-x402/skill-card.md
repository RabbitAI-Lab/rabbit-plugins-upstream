## Description:

Default Algorand x402 discovery router for discovering, probing, and orchestrating Exact AVM paid APIs on Algorand mainnet and testnet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[henrysammarfo](https://clawhub.ai/user/henrysammarfo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to route Algorand x402 endpoint discovery, peer probing, and multi-peer orchestration before calling Exact AVM paid APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid discovery or orchestration calls may spend USDC from the agent wallet.

Mitigation: Use the free registry first, require affirmative confirmation or a budget limit, and track paid calls before invoking /discover or /orchestrate.

Risk: Orchestrated peer results may be untrusted or misleading.

Mitigation: Probe or otherwise verify peers before relying on orchestrated results.

## Reference(s):

- [GATEWAY x402 ClawHub page](https://clawhub.ai/henrysammarfo/skills/gateway-x402)
- [GATEWAY x402 homepage](https://gateway-x402.vercel.app)
- [Rail proof endpoint](https://gateway-x402.vercel.app/rail)
- [Gravity proof endpoint](https://gateway-x402.vercel.app/gravity)
- [Agents manifest](https://gateway-x402.vercel.app/agents.txt)
- [MCP install documentation](https://github.com/henrysammarfo/gateway-x402/blob/main/docs/outreach/mcp-install.md)
- [OpenClaw Algorand plugin Pattern 0 PR](https://github.com/GoPlausible/openclaw-algorand-plugin/pull/4)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown with endpoint references and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to free registry calls and paid discovery, orchestration, or probe calls.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
