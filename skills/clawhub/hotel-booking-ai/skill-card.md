## Description:

Hotel search, comparison, and booking with live room rates and real-time availability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tourmind](https://clawhub.ai/user/tourmind)

### License/Terms of Use:

MIT

## Use Case:

External users and travel agents use this skill to search hotels, compare verified live room rates, inspect cancellation terms, create bookings, manage orders, and start supported payments through TourMind APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes an update workflow that can modify installed skill files from a remote release source.

Mitigation: Review the release source and installed changes before approving any update, and do not approve an update unless the release source is independently trusted.

Risk: Order, cancellation, and payment operations require a user_key and can affect real bookings.

Mitigation: Use public search without a key when possible, provide the key only for order operations, and never expose the key in outputs.

Risk: Cancellation and payment choices may create fees, refunds, or payment-processing charges.

Mitigation: Confirm the exact booking, cancellation terms, fee or refund consequences, and selected payment method before proceeding.

## Reference(s):

- [Parameter Guide](references/parameter_guide.md)
- [TourMind Skill API](https://api.tourmind.com)
- [ClawHub Skill Page](https://clawhub.ai/tourmind/skills/hotel-booking-ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown hotel recommendations, booking confirmations, policy summaries, and payment guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local hotel images, live rate tables, exact API error text, and read-only hotel detail links when returned by TourMind.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; artifact SKILL.md declares 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
