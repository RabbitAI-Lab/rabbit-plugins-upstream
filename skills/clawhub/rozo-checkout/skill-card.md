## Description:

Pay an OpenRouter Coinbase Payment Link with Stellar, Solana, BNB Chain, Ethereum, Polygon, Base (USDT/USDC) or Bitcoin Lightning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to pay OpenRouter Coinbase Payment Links with supported crypto assets that the Coinbase link does not accept directly. It can guide a user through keyless wallet payment, or optionally use a configured low-balance hot wallet for EVM and Solana sends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional hot-wallet path can use local private keys to send irreversible cryptocurrency payments.

Mitigation: Prefer the default keyless path where the user pays from their own wallet; use --send only with a dedicated low-balance hot wallet.

Risk: Wrong chain, token, amount, memo, or destination can cause unrecoverable payment loss.

Mitigation: Review the exact chain, token, amount, destination, memo or Lightning invoice, and expiry before final confirmation.

Risk: Credential exposure in a general-purpose agent environment can put valuable wallet keys at risk.

Mitigation: Avoid raw private keys in .env when possible, prefer encrypted key files for EVM, and never expose high-value wallet keys to the agent environment.

Risk: A funded or ambiguous order could be paid twice if retried incorrectly.

Mitigation: Follow the money-detected rule, preserve linkId, rozoPaymentId, and transaction hashes, and escalate for reconciliation instead of retrying payment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shawnmuggle/skills/rozo-checkout)
- [Publisher profile](https://clawhub.ai/user/shawnmuggle)
- [README](README.md)
- [Quick start](docs/QUICKSTART.md)
- [How it works](docs/how-it-works.md)
- [Safety design](docs/safety.md)
- [Security-audit notes](docs/security-audit-notes.md)
- [Agent summary](llms.txt)
- [Web agent documentation](https://checkout.rozo.ai/agent.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payment scripts print one JSON object on stdout; the skill should preserve payment identifiers and transaction hashes when reporting status.]

## Skill Version(s):

0.1.10 (source: ClawHub release metadata; artifact frontmatter metadata.version is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
