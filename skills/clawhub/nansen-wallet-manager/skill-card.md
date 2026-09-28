## Description:

Helps agents create, inspect, export, send from, and delete local or Privy-managed wallets using the Nansen CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to manage local or Privy-managed wallets, inspect wallet information, and prepare token transfers with the Nansen CLI.

### Deployment Geography for Use:

Global, subject to applicable geographic and sanctions restrictions.

## Known Risks and Mitigations:

Risk: Agent-initiated transfers or wallet deletion can cause irreversible loss of funds or access.

Mitigation: Require explicit human confirmation before each send or delete; preview sends with --dry-run and verify destination, amount, and chain.

Risk: Exported local-wallet private keys can be captured in logs, transcripts, or insecure files.

Mitigation: Require explicit human confirmation before export; avoid --reveal and keep any exported key file access restricted.

Risk: Wallet passwords and API or provider credentials may be exposed through insecure storage or broad agent access.

Mitigation: Use only credentials and wallets the operator authorizes for agent use; prefer a secure keychain or secret manager and avoid plaintext credential fallback.

## Reference(s):

- [Nansen Wallet Manager on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-wallet-manager)
- [Publisher profile on ClawHub](https://clawhub.ai/user/nansen-devops)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet actions may alter balances, delete wallets, or expose private keys; dry-run previews are available for sends.]

## Skill Version(s):

0.1.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
