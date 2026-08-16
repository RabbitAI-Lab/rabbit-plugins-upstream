## Description:

ROZO Intents Pay & Bridge helps agents create and track Rozo cross-chain USDC/USDT payment intents, check wallet balances, parse crypto payment QR data, and guide confirmations across supported Ethereum, Arbitrum, Base, BNB Chain, Polygon, Solana, and Stellar flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

External users and developers use this skill to send or bridge crypto payments, inspect USDC/USDT wallet balances, parse crypto payment QR codes or addresses, and check Rozo payment status while preserving explicit confirmation for payment flows by default.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crypto transfers are irreversible and may be sent to the wrong recipient, chain, token, memo, or amount.

Mitigation: Before funding, manually verify the recipient address, chain, token, memo, amount, and fee against a trusted source.

Risk: The skill includes an opt-in mode that can execute small payments without a fresh per-payment confirmation.

Mitigation: Keep confirmation thresholds at 0 unless intentionally enabling no-confirmation small payments.

Risk: Wallet addresses, payment amounts, chain choices, memos, and payment IDs are transmitted to Rozo public rate-limited APIs.

Mitigation: Use the skill only when the user explicitly wants Rozo to process the payment, balance, QR, or status request.

## Reference(s):

- [ROZO Intents Pay & Bridge on ClawHub](https://clawhub.ai/shawnmuggle/skills/rozo-intents-skills)
- [Rozo](https://rozo.ai)
- [Rozo API Reference](artifact/references/api-reference.md)
- [Supported Tokens and Chains](artifact/references/supported-chains.md)
- [Wallet Address Detection Rules](artifact/references/wallet-detection.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands and structured payment, balance, QR, and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and calls Rozo public rate-limited APIs; payment confirmation thresholds ship disabled at 0/0 unless the user changes version.json.]

## Skill Version(s):

1.0.9 (source: server release metadata, SKILL.md frontmatter, version.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
