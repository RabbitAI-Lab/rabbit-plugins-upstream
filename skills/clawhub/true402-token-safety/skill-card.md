## Description:

Checks tokens for honeypot and rug-pull risks using buy/sell simulation, liquidity and ownership checks, and observed Base liquidity-removal history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true402](https://clawhub.ai/user/true402)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and agent developers use this skill to assess a token before buying or approving it, and to report the check's verdict and supporting reasons. Base is the default chain; Ethereum and BSC checks are also supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A token check is a point-in-time assessment and does not guarantee future safety; historical coverage may be partial.

Mitigation: Relay the reasons and coverage limits, and do not present an OK verdict or absent removal history as a guarantee.

Risk: Paid checks give the CLI access to a payment wallet's private key.

Mitigation: Use free checks first; if needed, use a dedicated, low-balance Base wallet and keep the key out of files and logs.

Risk: Token and address queries are sent to true402.dev.

Mitigation: Avoid submitting token or address queries that must remain private.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/true402/skills/true402-token-safety)
- [true402 homepage](https://true402.dev)
- [true402 API reference](https://true402.dev/docs/api)
- [true402 OpenAPI specification](https://true402.dev/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with a token-risk verdict, score, reasons, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports AVOID, CAUTION, or OK; optional liquidity-removal history is available for Base only.]

## Skill Version(s):

1.2.3 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
