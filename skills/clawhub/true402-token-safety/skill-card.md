## Description:

Checks tokens for honeypot, liquidity, and ownership risks before trading, with observed liquidity-removal history available on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true402](https://clawhub.ai/user/true402)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and developers use this skill to check a token before buying or approving it and to explain flagged risks. Agents can use the verdict as a pre-trade gate, but it does not guarantee future safety.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running unpinned npm commands in a trading workflow may execute unverified code.

Mitigation: Verify and pin the package before use, especially in automated trading or when valuable secrets are present.

Risk: Paid checks expose a wallet private key to the local execution environment.

Mitigation: Prefer free checks; if payment is needed, use only a dedicated low-balance wallet and keep the key out of logs and shared files.

Risk: A point-in-time verdict or partial removal history cannot establish that a token will remain safe.

Mitigation: Explain flagged reasons and coverage limits, and require human judgment before trading.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/true402/skills/true402-token-safety)
- [true402 homepage](https://true402.dev)
- [true402 API reference](https://true402.dev/docs/api)
- [true402 OpenAPI specification](https://true402.dev/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with a token-risk verdict and reasons]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdict may include a 0–100 score; Base liquidity-removal history is optional and may be incomplete.]

## Skill Version(s):

1.2.2 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
