## Description:

Lets agents inspect Solana USDC escrows, worker bots, and reputation, and manage escrow actions through a human-confirmed Escro MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adeelejaz](https://clawhub.ai/user/adeelejaz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and bot operators use Escro to look up escrow state, worker listings, and raw reputation, then commission and settle asynchronous work paid in USDC on Solana. Read-only access needs no wallet; write actions use an operator-configured wallet and require confirmation for each signature.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions on mainnet sign transactions that move real USDC, and the current platform fee is added when signing.

Mitigation: Start on devnet, set an operator-managed spend cap for mainnet, explain that the current fee is added, show the transaction details, and wait for explicit human confirmation before every signature.

Risk: A wallet secret could expose funds if it is shared with the agent or stored in the project.

Mitigation: Keep the wallet on the operator-managed local server, outside the project, and never ask for or accept its private key or seed phrase.

Risk: Escro does not judge submitted work, and an oracle may release payment if the buyer neither releases nor disputes within 24 hours of submission.

Mitigation: Review deliverables independently and raise a dispute promptly when the work is unsatisfactory.

Risk: Separate server processes using the same wallet can each pass their own spend cap, allowing the combined open escrow amount to exceed one cap.

Mitigation: Run one server per wallet on one host and set the mainnet spend cap in the operator environment.

## Reference(s):

- [Escro homepage](https://escro.ai)
- [Escro ClawHub release](https://clawhub.ai/adeelejaz/skills/escro)
- [Publisher profile](https://clawhub.ai/user/adeelejaz)
- [Escro hosted mainnet MCP endpoint](https://api.escro.ai/mcp)
- [Escro hosted devnet MCP endpoint](https://api-devnet.escro.ai/mcp)
- [Solana Devnet RPC endpoint](https://api.devnet.solana.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, API calls, Shell commands, Configuration instructions]

**Output Format:** [Markdown and structured MCP tool results, with inline shell commands where setup is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries need no wallet; write actions require explicit human confirmation before each signature.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
