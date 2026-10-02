## Description:

Guides agents in creating, inspecting, exporting, sending from, and deleting local or Privy-backed wallets with the Nansen CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage local or Privy-backed wallets, check balances, and prepare or send tokens through the Nansen CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Token sends, especially full-balance sends with --max, can move real funds.

Mitigation: Require explicit human approval for each send and prefer --dry-run to inspect the transaction first.

Risk: Deleting wallets can remove access to funds.

Mitigation: Require explicit human approval before deleting a wallet.

Risk: Exporting local private keys with --reveal exposes secrets in agent transcripts or terminal output.

Mitigation: Require explicit human approval; prefer redacted exports or restricted file-based exports over --reveal.

## Reference(s):

- [Nansen Wallet Manager on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-wallet-manager)
- [Nansen CLI browser-login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet commands may return balances, transaction details, or, on explicit local-key export, sensitive private keys.]

## Skill Version(s):

0.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
