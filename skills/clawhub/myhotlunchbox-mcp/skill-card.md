## Description:

Read and manage a My Hot Lunchbox school-lunch account from a shell with curl: sign in, list students, read the lunch calendar and cart, and check orders, deliveries, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and account holders use this skill to inspect and manage My Hot Lunchbox account data from shell sessions when the MCP server is unavailable or scripting is preferred.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell sessions can expose My Hot Lunchbox credentials or bearer tokens if secrets are pasted into command lines, logs, or history.

Mitigation: Read credentials from environment variables or secure prompts, avoid echoing tokens, and clear sensitive shell state after use.

Risk: Write operations can change orders, student records, subscriptions, coupons, gift cards, or payments, and some request bodies are documented as unverified against a live account.

Mitigation: Preview totals and payloads first, avoid speculative write calls, re-read resources after mutations, and prefer the MCP version when available for typed tools, dry runs, and confirmation gates.

Risk: Checkout can charge a real payment method, and retrying with a new idempotency key after an ambiguous response can risk duplicate charges.

Mitigation: Use initCheckout before payment, confirm the returned total, and reuse the same idempotency key when retrying an ambiguous checkout.

Risk: Repeated failed sign-in attempts can trigger CAPTCHA or remove server-side sign-in access for the account.

Mitigation: Stop after invalid_grant or a failed login response and verify credentials before attempting another sign-in.

## Reference(s):

- [My Hot Lunchbox endpoints](references/endpoints.md)
- [My Hot Lunchbox API host](https://ordernow.myhotlunchbox.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples and endpoint notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl commands, jq filters, environment variable setup, and cautions for credential, write, and payment operations.]

## Skill Version(s):

0.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
