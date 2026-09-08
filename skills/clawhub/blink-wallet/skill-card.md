## Description:

Bitcoin Lightning wallet for agents — balances, invoices, payments, BTC/USD swaps, QR codes, price conversion, transaction history, and L402 auto-pay client via the Blink API. All output is JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pretyflaco](https://clawhub.ai/user/pretyflaco)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to automate Blink Bitcoin Lightning wallet operations, including balance checks, invoice creation, payments, swaps, QR generation, transaction review, and L402 paid-resource access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access wallet credentials and spend real funds through Blink, Lightning, L402, swap, and Spark commands.

Mitigation: Use least-privileged API keys, avoid Write scope unless sending is required, test on staging first, check balance and fees, dry-run swaps and L402 payments, and require explicit confirmation before spending.

Risk: SPARK_MNEMONIC grants full self-custodial spend authority when Spark commands are used.

Mitigation: Provide SPARK_MNEMONIC only in runtimes intended to spend from that wallet; never log or display it; rely on the skill behavior that reads it from the environment and aborts if seed validation is unavailable.

Risk: L402 tokens, transaction data, and payment outputs can be sensitive and may be cached locally.

Mitigation: Treat token and transaction output as sensitive, use --no-store on shared systems, clear the L402 store when needed, and configure strict L402 budgets and domain allowlists.

Risk: L402 flows contact third-party service URLs and the security summary notes that unchecked requests need review.

Mitigation: Restrict allowed domains, dry-run discovery before payment, review the target URL and satoshi amount, and keep network access limited to the disclosed Blink, LNURL, L402, and Spark endpoints required for the task.

## Reference(s):

- [Blink Wallet ClawHub page](https://clawhub.ai/pretyflaco/skills/blink-wallet)
- [Blink skills homepage](https://github.com/blinkbitcoin/blink-skills)
- [Blink API and auth](references/blink-api-and-auth.md)
- [Invoice lifecycle](references/invoice-lifecycle.md)
- [Payment operations](references/payment-operations.md)
- [Swap operations](references/swap-operations.md)
- [Non-custodial Spark accounts](references/non-custodial.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; invoked scripts return JSON and may write QR PNGs or local wallet/L402 state files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet command outputs are structured JSON; payment, subscription, L402, and Spark operations may depend on configured credentials, budgets, allowlists, and runtime environment.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
