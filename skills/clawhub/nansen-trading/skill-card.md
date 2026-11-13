## Description:

Execute DEX swaps on Solana or Base (including cross-chain bridges) and Hyperliquid perpetual trades. Use when buying or selling a token, getting a swap quote, executing a trade, or opening/closing/managing a perp position.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request token swaps and bridges on Solana or Base, and to open, manage, or close Hyperliquid perpetual positions. It provides CLI guidance and trade plans for the requested action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked the skill suspicious because it reportedly instructs users to save a wallet password in a plaintext .env file; the scan was partial.

Mitigation: Consider the suspicious verdict and incomplete scan before installing. Avoid installing unless you are comfortable with the exposure and can protect the credential.

## Reference(s):

- [Nansen CLI documentation and source](https://github.com/nansen-ai/nansen-cli)
- [nansen-cli package](https://www.npmjs.com/package/nansen-cli)
- [Browser login platform scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [CLI commands with textual quotes, trade plans, and status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trade execution can broadcast irreversible on-chain transactions.]

## Skill Version(s):

0.1.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
