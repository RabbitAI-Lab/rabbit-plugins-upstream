## Description:

rozo-checkout lets agents pay Coinbase-hosted payment links, including OpenRouter top-ups, from supported USDT/USDC chains or Bitcoin Lightning without a Coinbase account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT

## Use Case:

External developers and agent operators use this skill to quote, create, confirm, and monitor payments for Coinbase or OpenRouter invoices from supported crypto wallets. It is intended for payment workflows where the user must review the merchant, amount, chain, token, memo, and destination before funds move.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help move real funds when a payment flow is confirmed.

Mitigation: Use the default keyless path when possible, and review the merchant, amount, chain, token, memo, and destination before confirming.

Risk: Optional hot-wallet signing can expose funds if a primary wallet or overfunded wallet is configured.

Mitigation: Enable --send only with a dedicated low-balance hot wallet; the documented send path also uses confirmations, local checks, and a per-payment cap.

Risk: Sending the wrong token, wrong network, wrong amount, or omitting a required memo can cause unrecoverable payment loss.

Mitigation: Follow the generated deposit block exactly once and verify chain, token, destination, memo, amount, and expiry before paying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shawnmuggle/skills/rozo-checkout)
- [Publisher profile](https://clawhub.ai/user/shawnmuggle)
- [README](README.md)
- [Quick start](docs/QUICKSTART.md)
- [Safety design](docs/safety.md)
- [How it works](docs/how-it-works.md)
- [Security audit notes](docs/security-audit-notes.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command scripts print one JSON object on stdout and may require explicit confirmation before funds move.]

## Skill Version(s):

0.1.11 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
