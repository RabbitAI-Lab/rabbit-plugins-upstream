## Description:

Helps shoppers compare KnifeRevive listings and request San Francisco Bay Area knife sharpening, with live availability checks and customer-authorized checkout or booking handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[svetlyoh](https://clawhub.ai/user/svetlyoh)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and their agents use the skill to compare KnifeRevive products, check live pricing and policies, and prepare customer-approved purchases or Bay Area sharpening requests. Bookings and payments require separate confirmation.

### Deployment Geography for Use:

San Francisco Bay Area for sharpening; pickup and prepayment are limited to Contra Costa and Santa Clara counties. Listing fulfillment depends on live merchant terms.

## Known Risks and Mitigations:

Risk: A shopping or booking handoff could be mistaken for a completed purchase or confirmed appointment.

Mitigation: Disclose final terms and require customer approval; describe bookings as requests and payments as pending until the merchant confirms each state.

Risk: Wallet spending or private checkout links could expose funds or sensitive customer data.

Mitigation: Use only independently authorized, scoped wallet access for a verified invoice; keep private links and tokens confidential, and leave card checkout to the customer.

Risk: Availability, coverage, fees, and payment options can change.

Mitigation: Check live merchant capabilities and terms before recommending a service or preparing a handoff; offer the human booking route if agent booking is unavailable.

## Reference(s):

- [KnifeRevive Concierge on ClawHub](https://clawhub.ai/svetlyoh/skills/kniferevive-concierge)
- [API workflow](references/api.md)
- [Sharpening booking requests](references/booking.md)
- [Published marketplace listing checkout](references/listing-checkout.md)
- [Payments](references/payments.md)
- [Sharpening and physical handoff](references/sharpening.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with comparisons, quotes, and private booking or checkout links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Booking and payment status are reported separately; links and quotes do not establish a paid order or confirmed appointment.]

## Skill Version(s):

0.4.2 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
