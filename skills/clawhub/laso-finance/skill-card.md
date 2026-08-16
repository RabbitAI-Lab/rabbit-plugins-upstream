## Description:

Order prepaid cards, gift cards, and send money to USD/EUR/GBP debit cards or US bank accounts using USDC on Base or Solana via the x402 protocol. Use when a user or agent needs to spend cryptocurrency, pay for an online checkout, buy a prepaid card, order a gift card, send money to a debit card or bank account, check a card or account balance, pay a paywalled x402 endpoint, or resolve a 402 Payment Required response.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huntermonk](https://clawhub.ai/user/huntermonk)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent spend USDC through Laso Finance for prepaid cards, gift cards, debit-card payouts, bank payments, balance checks, and x402 paywall settlement.

### Deployment Geography for Use:

Global, subject to product-specific payment rail limits for U.S. prepaid cards, U.S. push-to-card, Eurozone EUR payouts, and U.K. GBP payouts.

## Known Risks and Mitigations:

Risk: Stored Laso credentials may allow an agent to reuse account access for future financial activity.

Mitigation: Treat Laso credentials like banking credentials, keep them out of repositories and shared logs, and store them only in the intended credentials path with restricted permissions.

Risk: The skill can support purchases, transfers, withdrawals, banking changes, webhook registration, and credential persistence.

Mitigation: Require clear user approval before any purchase, transfer, withdrawal, banking change, webhook registration, or credential persistence.

Risk: Payment, account, and card workflows can expose sensitive financial details in prompts, logs, or generated files.

Mitigation: Avoid writing secrets or card details to project files, memory files, transcripts, or reusable instructions, and redact sensitive values from logs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huntermonk/skills/laso-finance)
- [Laso Finance](https://laso.finance)
- [Laso Finance Skill Source](https://laso.finance/SKILL.md)
- [Laso Finance Docs Version Beacon](https://laso.finance/.well-known/docs-version.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, HTTP requests, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include credential-handling steps, payment flow decisions, and API endpoint call sequences.]

## Skill Version(s):

1.0.0 (source: evidence.release.version; artifact metadata.version is 1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
