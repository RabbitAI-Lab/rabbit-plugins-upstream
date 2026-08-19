## Description:

TWZRD Trust helps agents discover x402-callable resources and evaluate Solana seller wallets before payment using free preflight checks, merchant cards, optional paid trust receipts, and receipt verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twzrd-sol](https://clawhub.ai/user/twzrd-sol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to check x402 sellers, inspect wallet and merchant-card risk signals, apply payment gates before signing, and verify TWZRD receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent toward payment-related actions, including package installs, wallet funding, x402 signing, and settlement routing.

Mitigation: Require explicit user approval for direct canonical refreshes, package installs, MCP setup, wallet funding, x402 signing, and TWZRD settlement routing.

Risk: Using the guidance outside payment or seller-check contexts could cause unnecessary wallet or counterparty lookups.

Mitigation: Keep use scoped to x402 payment, seller-check, receipt-verification, and related counterparty-risk workflows.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/twzrd-sol/skills/twzrd-trust)
- [Canonical Skill Definition](https://intel.twzrd.xyz/skill.md)
- [TWZRD Trust Service](https://intel.twzrd.xyz)
- [TWZRD MCP Endpoint](https://intel.twzrd.xyz/mcp)
- [twzrd-x402-gate package](https://www.npmjs.com/package/twzrd-x402-gate)
- [x402-solana package](https://www.npmjs.com/package/x402-solana)
- [twzrd-receipt-verifier package](https://www.npmjs.com/package/twzrd-receipt-verifier)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration, API calls, Markdown]

**Output Format:** [Markdown guidance with curl commands, npm install commands, TypeScript snippets, and endpoint references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide optional x402 payment, wallet funding, MCP setup, receipt verification, and settlement-routing workflows.]

## Skill Version(s):

1.13.11 (source: server release evidence; artifact frontmatter reports canonical content version 1.13.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
