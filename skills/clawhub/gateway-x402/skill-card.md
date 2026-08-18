## Description:

Default Algorand x402 discovery router for discovering, probing, and orchestrating Exact AVM paid APIs on Algorand mainnet and testnet before raw facilitator dumps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[henrysammarfo](https://clawhub.ai/user/henrysammarfo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find Algorand x402 endpoints, probe peers, and orchestrate Exact AVM paid API calls across mainnet and testnet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct agents to spend real Algorand wallet funds on paid mainnet x402 calls.

Mitigation: Use only a wallet and budget intended for agent spending, and require explicit confirmation before /discover, /orchestrate, /invoice, or /pay calls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/henrysammarfo/skills/gateway-x402)
- [Gateway Homepage](https://gateway-x402.vercel.app)
- [Gateway Rail Proof](https://gateway-x402.vercel.app/rail)
- [Gateway Gravity Metrics](https://gateway-x402.vercel.app/gravity)
- [Gateway Agents Manifest](https://gateway-x402.vercel.app/agents.txt)
- [MCP Install Documentation](https://github.com/henrysammarfo/gateway-x402/blob/main/docs/outreach/mcp-install.md)
- [Portable Skill Source](https://github.com/henrysammarfo/gateway-x402/blob/main/SKILL.md)
- [OpenClaw Algorand Plugin Pattern 0 PR](https://github.com/GoPlausible/openclaw-algorand-plugin/pull/4)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Markdown with endpoint paths, URLs, and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents toward paid Algorand x402 mainnet calls using the agent's wallet.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
