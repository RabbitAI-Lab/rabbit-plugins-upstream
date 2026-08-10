## Description:

Rozo Checkout Skill helps agents pay OpenRouter Coinbase Payment Links with BTC Lightning or USDT/USDC on supported chains through a one-time bridge order.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to route OpenRouter Coinbase Payment Link payments with supported non-Base-USDC coins. The normal path gives users a deposit block for their own wallet; optional hot-wallet sending is available only when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional hot-wallet mode can load local or environment wallet keys and broadcast irreversible transfers.

Mitigation: Prefer the default keyless flow where the user pays from their own wallet; use hot-wallet sending only with explicit user intent and a low-balance wallet.

Risk: Private keys or passphrases can be exposed if placed in prompts, command lines, commits, or valuable project .env files.

Mitigation: Do not ask users to paste keys into the agent conversation; prefer encrypted keystores or user-managed wallet flows and keep any local key material out of tracked files.

Risk: Wrong token, wrong network, missing Stellar memo, or duplicate payment to a one-time order can cause unrecoverable loss.

Mitigation: Use the generated deposit block exactly, verify token, chain, amount, address, memo, and expiry before funding, and do not retype payment addresses by hand.

Risk: Retrying after funds are detected can create a second payment or complicate reconciliation.

Mitigation: Preserve the link id, Rozo payment id, and transaction hashes, poll status, and escalate for reconciliation instead of creating or funding a new order.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shawnmuggle/skills/rozo-checkout)
- [README](README.md)
- [Quick start](docs/QUICKSTART.md)
- [How it works](docs/how-it-works.md)
- [Safety design](docs/safety.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command outputs are single JSON objects; optional hot-wallet mode can broadcast irreversible crypto transfers after explicit confirmation.]

## Skill Version(s):

0.1.6 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
