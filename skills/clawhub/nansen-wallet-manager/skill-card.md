## Description:

Wallet management: create local or Privy server-side wallets, list and show wallets, export local keys, send tokens, and delete wallets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide an agent through Nansen CLI wallet operations, including wallet creation, balance inspection, token transfers, key export for local wallets, and wallet deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide token transfers, wallet deletion, full-balance sends, key export for local wallets, and use of sensitive wallet credentials.

Mitigation: Require explicit user confirmation for send, export, delete, and --max operations, and prefer dry-run previews before broadcasting transactions.

Risk: Local wallet creation requires a user-provided password, and insecure storage may be used when an OS keychain is unavailable.

Mitigation: Ask the human user for the wallet password, do not store it in files, logs, or conversation history, and migrate to secure storage with nansen wallet secure when needed.

Risk: Privy wallet operations depend on application credentials that grant access to server-side wallet management.

Mitigation: Keep PRIVY_APP_ID and PRIVY_APP_SECRET in a secret manager and expose them only to trusted runtime environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nansen-devops/skills/nansen-wallet-manager)
- [Publisher profile](https://clawhub.ai/user/nansen-devops)
- [nansen-cli package](nansen-cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the nansen CLI and NANSEN_API_KEY; Privy wallet creation additionally requires PRIVY_APP_ID and PRIVY_APP_SECRET.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
