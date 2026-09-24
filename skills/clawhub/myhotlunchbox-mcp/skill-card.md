## Description:

Read and manage a My Hot Lunchbox school-lunch account from a shell with curl: sign in, list students, read the lunch calendar and cart, and check orders, deliveries, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and My Hot Lunchbox account users can use this skill to retrieve account, student, calendar, cart, order, transaction, and report data from shell-based workflows when the MCP server is unavailable or not installed. It also documents write and checkout endpoints, which require careful manual review before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw shell commands can operate against a live My Hot Lunchbox account and may expose credentials or account data if copied into unsafe environments.

Mitigation: Load credentials from environment variables or secure prompts, avoid pasting secrets into command history, and inspect commands before execution.

Risk: Write, delete, subscription, coupon, and checkout endpoints can change account state or charge a payment method without built-in safeguards.

Mitigation: Treat these operations as manual-only, inspect every payload and price, require explicit confirmation, and prefer the MCP server when available because it provides confirm-gated writes and dry-run previews.

Risk: Unverified write request bodies can clear omitted fields or appear successful without proving the intended account change occurred.

Mitigation: Fetch the current model before editing, post complete payloads, and re-read the affected resource after a 200 response to confirm the result.

Risk: Repeated failed sign-in attempts can trigger CAPTCHA or block server-side sign-in for the account.

Mitigation: Stop after an invalid_grant response and verify credentials before retrying.

## Reference(s):

- [My Hot Lunchbox endpoints](references/endpoints.md)
- [My Hot Lunchbox order site](https://ordernow.myhotlunchbox.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to use curl and jq against live account APIs and to produce command snippets, request payloads, and operational cautions.]

## Skill Version(s):

1.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
