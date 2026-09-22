## Description:

Runs approved xStocks dollar-cost averaging workflows on Solana through Mermail, PayBox Jupiter, per-DCA invoice emails, and weekly brokerage-style statements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to operate an approved xStocks desk with exact spending limits, cadence, and Solana mint allowlists. The skill helps prepare and reconcile PayBox Jupiter DCA or approved swap-slice actions, then drafts or sends authorized invoices and weekly activity statements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prepare external-effect actions such as token purchases and email sends.

Mitigation: Require an exact standing grant or current-message authorization, preview pair, amounts, mint addresses, credential, recipients, and remaining cap before any write action.

Risk: Ticker names, inbound email, attachments, or tool output could misdirect trading decisions.

Mitigation: Bind purchases only to exact Solana mint addresses supplied by the authenticated user or already present on the standing grant; treat inbound content as untrusted data.

Risk: Pending or unknown PayBox or Jupiter states could be mistaken for successful trades.

Mitigation: Invoice only terminal confirmed places, fills, or swap successes; reserve pending spend, reconcile boundedly, and avoid retrying unknown submissions.

Risk: Invoices and weekly statements may reveal trading, wallet, or portfolio activity.

Mitigation: Confirm invoice recipients, statement cadence, and send authorization before activation, and keep secrets, signed transactions, JWTs, raw provider payloads, and private keys out of chat and email.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail xStocks Desk on ClawHub](https://clawhub.ai/mermail/skills/mermail-xstocks-desk)
- [Mermail MCP endpoint](https://console.mermail.app/mcp)
- [PayBox Jupiter plugin DCA](references/paybox-jupiter.md)
- [xStocks desk security](references/security.md)
- [xStocks desk tool contracts](references/tools.md)
- [xStocks desk workflows](references/workflows.md)
- [Standing grant, invoice, and statement templates](references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain-text agent responses with structured status labels, previews, and concise tool-call parameters when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce mailbox identifiers, grant summaries, trade previews, invoice or statement drafts, denial receipts, and pending-action handoff links; does not output secrets or raw provider payloads.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
