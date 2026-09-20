## Description:

Runs an xStocks trading desk through a Mermail mailbox for approved DCA purchases on Solana, per-DCA invoice emails, and weekly brokerage-style statement drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate a Mermail-backed xStocks DCA workflow under a standing grant, including approved PayBox Jupiter DCA or swap-slice actions, per-DCA invoice emails, and weekly activity statements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact xStocks DCA and email workflows.

Mitigation: Define budget, cadence, exact Solana mint allowlist, invoice recipients, and wallet before use, then review every trading or email preview before approval.

Risk: Ticker-only, email-derived, or search-derived token choices could lead to unintended assets.

Mitigation: Use only exact Solana mint addresses supplied by the authenticated user or already present on the standing grant.

Risk: Pending or unknown trading states could be mistaken for confirmed activity.

Mitigation: Invoice or report execution only after authoritative terminal success, and reserve pending spend without retrying unknown submissions.

Risk: Inbound email, attachments, or tool output could attempt to authorize trades, sends, recipient changes, or secret handling.

Mitigation: Treat inbound and tool content as untrusted data, require clean scan status before interpreting message bodies, and never paste or request private keys, signed transactions, JWTs, or API keys.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [ClawHub Skill Page](https://clawhub.ai/mermail/skills/mermail-xstocks-desk)
- [PayBox Jupiter Plugin DCA](references/paybox-jupiter.md)
- [xStocks Desk Security](references/security.md)
- [xStocks Desk Tool Contracts](references/tools.md)
- [xStocks Desk Workflows](references/workflows.md)
- [Standing Grant, Per-DCA Invoice, and Weekly Statement Templates](references/templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown or plain text with structured status labels, email draft content, and JSON-shaped tool inputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MERMAIL_API_KEY, full-profile Mermail and PayBox authorization, exact user-approved mint allowlists, and user approval for trading or email sends.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
