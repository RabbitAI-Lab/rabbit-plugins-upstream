## Description:

AI-powered sports betting simulations with Monte Carlo analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cannedoxygen](https://clawhub.ai/user/cannedoxygen)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse games, retrieve daily picks and track records, and run EdgeBets sports simulations for NBA, NFL, MLB, and MLS betting analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid simulations can spend USDC from a configured Solana wallet without clear per-transaction confirmation in the documented flow.

Mitigation: Require explicit confirmation of amount, recipient, network, game, and simulation parameters before each paid simulation.

Risk: The skill requires a Solana private key or wallet capable of signing transactions.

Mitigation: Use a dedicated low-balance wallet, avoid primary wallet private keys, and pin the exact package version before installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/cannedoxygen/skills/sdk)
- [EdgeBets Website](https://edgebets.fun)
- [EdgeBets API Documentation](https://api.edgebets.fun/api/v1/x402)
- [EdgeBets OpenAPI Spec](https://api.edgebets.fun/api/v1/x402/openapi.json)
- [edgebets-sdk npm Package](https://www.npmjs.com/package/edgebets-sdk)
- [x402 Protocol](https://x402.org)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with TypeScript or shell command snippets and structured simulation summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require a configured Solana wallet and can trigger paid USDC simulations when the agent executes SDK actions.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
