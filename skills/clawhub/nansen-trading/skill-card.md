## Description:

Execute DEX swaps on Solana or Base (including cross-chain bridges) and Hyperliquid perpetual trades. Use when buying or selling a token, getting a swap quote, executing a trade, or opening/closing/managing a perp position.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and developers can use this skill to request quotes, execute swaps and bridges on Solana or Base, and manage Hyperliquid perpetual positions through the Nansen CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documentation says the wallet password is persisted in a local plaintext environment file.

Mitigation: Review the credential storage setup before installation, protect access to the local credential file, and use a secure secret store where available.

Risk: Transaction confirmation can be skipped, and non-interactive execution may proceed without a prompt; on-chain trades are irreversible.

Mitigation: Preview actions with --dry-run and inspect the wallet, network, assets, amounts, and order details before signing. Avoid --yes or NANSEN_YES=1 unless bypassing the prompt is intentional.

## Reference(s):

- [Nansen CLI documentation and source repository](https://github.com/nansen-ai/nansen-cli)
- [Nansen CLI package on npm](https://www.npmjs.com/package/nansen-cli)
- [Browser login platform scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Nansen CLI commands and text responses, with Markdown guidance when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include quotes, transaction or order details, positions, account information, and bridge status.]

## Skill Version(s):

0.1.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
