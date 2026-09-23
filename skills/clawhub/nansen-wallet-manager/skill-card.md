## Description:

Wallet management - create (local or Privy server-side), list, show, export, send, delete. Use when creating wallets, checking balances, or sending tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to guide agents through Nansen CLI wallet operations, including wallet creation, balance checks, token transfers, export, deletion, and secure password handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through high-impact wallet actions, including fund transfers, sending an entire balance, wallet deletion, and private-key export.

Mitigation: Use it only where the agent is authorized to manage real crypto wallets, and require explicit human approval before any send, --max, delete, or private-key export action.

Risk: Plaintext private keys can be exposed through --reveal in terminal scrollback, logs, or agent transcripts.

Mitigation: Avoid --reveal in agent sessions; prefer safer file-based export only when absolutely necessary and protect exported files.

Risk: Local wallet creation requires a human-provided password and may fall back to an insecure credentials file when OS keychain storage is unavailable.

Mitigation: Have the human provide the password directly, avoid storing it in conversation or logs, and migrate to secure storage with `nansen wallet secure` when fallback credentials are used.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nansen-devops/skills/nansen-wallet-manager)
- [Publisher profile](https://clawhub.ai/user/nansen-devops)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires NANSEN_API_KEY and the nansen CLI; Privy wallet creation also requires PRIVY_APP_ID and PRIVY_APP_SECRET.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
