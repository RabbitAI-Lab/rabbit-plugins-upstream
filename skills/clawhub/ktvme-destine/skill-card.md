## Description:

Helps an agent guide KTV room booking through store lookup, room availability selection, login, order creation, payment presentation, and payment-status polling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jacklovecat](https://clawhub.ai/user/jacklovecat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and booking agents use this skill to find KTV stores, compare available room time slots, create bookings, present payment details, and monitor payment status. It is intended for real booking flows backed by the Kmi KTV service CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a KTV account to create, monitor, and cancel real bookings.

Mitigation: Require user confirmation of store, room, time, price, and cancellation intent before order-changing actions.

Risk: The flow uses OTP login and depends on the external @ktvme/km-bot CLI.

Mitigation: Only install and run the CLI from trusted sources, and keep OTP entry inside the intended login flow.

Risk: Payment and order polling details may be written to local /tmp files.

Mitigation: Review and remove temporary polling result files after the booking flow completes.

## Reference(s):

- [API Overview and Common Constraints](artifact/reference/api-overview.md)
- [Store API](artifact/reference/api-store.md)
- [Room Availability API](artifact/reference/api-room.md)
- [Order API](artifact/reference/api-order.md)
- [Session and Login API](artifact/reference/api-session.md)
- [CLI Install and Verification](artifact/reference/cli-install.md)
- [Login Subflow](artifact/reference/subflow-login.md)
- [Payment Subflow](artifact/reference/subflow-pay.md)
- [Error Handling Guide](artifact/reference/error-handling.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON API parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local payment polling results under /tmp for an order id.]

## Skill Version(s):

0.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
