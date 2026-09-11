## Description:

Read and manage a My Hot Lunchbox school-lunch account from a shell with curl: sign in, list students, read the lunch calendar and cart, and check orders, deliveries, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve My Hot Lunchbox account data and prepare shell commands for lunch calendars, carts, orders, reports, subscriptions, and payment-related account workflows when the MCP server is unavailable or scripting is preferred.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw write, delete, subscription, and payment endpoints can modify school-lunch account state or charge a saved card.

Mitigation: Manually review each command and require explicit user confirmation before any mutation or payment; prefer the MCP version for confirm-gated writes.

Risk: Credential and bearer-token handling in shell sessions can expose account access if values are pasted into command lines or kept in persistent profiles.

Mitigation: Read credentials from environment variables, avoid shell history, unset passwords after login, and avoid storing tokens in persistent shell configuration.

Risk: Read-modify-write order payloads can clear omitted fields or return a successful response without proving the intended change landed.

Mitigation: Fetch the current model, inspect the full payload before posting it back, and re-read the affected resource after the request.

Risk: Payment checkout can charge a real payment method, and retrying with a fresh idempotency key can risk a second charge.

Mitigation: Price the cart with initCheckout first, confirm the total before checkout, and reuse the same idempotency key when retrying an ambiguous checkout.

## Reference(s):

- [My Hot Lunchbox endpoint reference](artifact/references/endpoints.md)
- [My Hot Lunchbox API host](https://ordernow.myhotlunchbox.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl and jq command snippets, environment-variable setup, API endpoint paths, JSON request bodies, and cautionary handling notes.]

## Skill Version(s):

0.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
