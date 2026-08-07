## Description:

Rug-check a Base token before trading with real buy/sell honeypot simulation, liquidity and ownership checks, and observed liquidity-removal history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true402](https://clawhub.ai/user/true402)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and trading agents use this skill to check Base ERC-20 tokens before buying, approving, or following a trade. It runs the true402 checker and returns a verdict with on-chain reasons that can be used as a pre-trade safety gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paid-check wallet key can be exposed through shared files, logs, process inspection, or CI output.

Mitigation: Prefer free no-wallet mode; when paid checks are needed, use a dedicated low-balance Base wallet and keep PAYER_PRIVATE_KEY out of shared files, global shell profiles, Dockerfiles, and logs.

Risk: A token-safety verdict is point-in-time and can miss later liquidity removal or other post-check changes.

Mitigation: Treat the verdict as one trading input, use --history for observed Base liquidity-removal context, and avoid autonomous purchases without human or policy review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/true402/skills/true402-token-safety)
- [Publisher Profile](https://clawhub.ai/user/true402)
- [true402 Homepage](https://true402.dev)
- [API Documentation](https://true402.dev/docs/api)
- [OpenAPI Specification](https://true402.dev/openapi.json)
- [Browser Token Check](https://true402.dev/check)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and token-safety verdicts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AVOID, CAUTION, or OK verdicts, numeric scores, exit-code guidance, and specific on-chain risk reasons.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
