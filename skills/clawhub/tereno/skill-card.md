## Description:

Provides Base token and contract security checks, prediction market oracle audits, and shared verification guidance for agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tereno-xyz](https://clawhub.ai/user/tereno-xyz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous agents use Tereno before Base token or contract interactions, prediction market bets, and escrow decisions to review security evidence and surface risks for human or policy review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional local `npx -y tereno-mcp` setup can run an unpinned npm package, creating supply-chain risk and potentially exposing credentials or local files.

Mitigation: Avoid the local setup, or use a reviewed fixed package version and limit its access to credentials and local files.

## Reference(s):

- [Tereno service](https://www.tereno.xyz)
- [Tereno MCP endpoint](https://www.tereno.xyz/api/mcp)
- [ClawHub skill page](https://clawhub.ai/tereno-xyz/skills/tereno)
- [Capabilities, pricing, and MCP tools](references/capabilities-and-pricing.md)
- [Binance Agentic Wallet x402 workflow](references/baw-x402-workflow.md)
- [Cooperative cache and bounty guide](references/cooperation-economy.md)
- [ERC-8183 escrow and ERC-7579 guards](references/escrow-and-erc7579.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Machine-readable JSON verdicts with evidence, reason codes, limitations, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts may include an on-chain validity block and a reusable artifact reference.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
