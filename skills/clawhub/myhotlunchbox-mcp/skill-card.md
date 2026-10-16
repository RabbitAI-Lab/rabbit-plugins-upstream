## Description:

Guides shell-based access to a My Hot Lunchbox account to view school-lunch information and manage orders and account settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and developers with a My Hot Lunchbox account use this skill to check students, lunch calendars, carts, transactions, and subscriptions from a shell when the MCP server is unavailable. It also describes account and order changes that require careful review and explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell access to a real account can expose credentials and student or payment-related information.

Mitigation: Keep credentials out of command history, limit access to account data, and stop rather than retrying a failed sign-in.

Risk: Writes can change or clear orders, student profiles, subscriptions, coupons, or gift cards, and the documented write payloads have not been tested on a live account.

Mitigation: Review the full payload, require explicit confirmation before each mutation, and read the resource again afterward; prefer the MCP wrapper's confirmation flow when available.

Risk: Checkout can charge a real payment method, including on an accidental repeat attempt.

Mitigation: Price the cart and confirm the total before checkout; reuse the same idempotency key when retrying an ambiguous payment.

## Reference(s):

- [My Hot Lunchbox endpoint reference](references/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Instructions for authenticated account reads and potentially consequential writes; no enforceable confirmation in shell commands.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
