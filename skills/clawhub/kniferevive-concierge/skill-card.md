## Description:

Helps shoppers compare KnifeRevive listings and request San Francisco Bay Area knife sharpening, with live coverage and pricing checks and customer-controlled checkout or explicitly authorized Lightning payment when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[svetlyoh](https://clawhub.ai/user/svetlyoh)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Shoppers use this skill to find and compare KnifeRevive products or request knife sharpening, review prices and handoff options, and reach a secure merchant checkout or booking form. An existing authorized host wallet may pay a verified Lightning invoice when that option is enabled.

### Deployment Geography for Use:

Online listing discovery; sharpening in the San Francisco Bay Area, California, United States, with prepaid and pickup options limited to eligible Contra Costa and Santa Clara ZIP codes.

## Known Risks and Mitigations:

Risk: A wallet payment could exceed the shopper's intended authorization or pay an unverified invoice.

Mitigation: Require an independently verified wallet grant and confirm the merchant, invoice, amount, and routing-fee limit before a single payment; otherwise use the customer-controlled checkout.

Risk: Sharing private checkout or booking links could expose customer or order information.

Mitigation: Have the customer review links privately on the first-party merchant site, and keep booking and session tokens out of public messages and logs.

Risk: Outdated prices or unconfirmed booking and payment states could mislead shoppers.

Mitigation: Check live coverage, fees, and policies; show an itemized quote and report payment and appointment confirmation separately.

## Reference(s):

- [KnifeRevive Concierge on ClawHub](https://clawhub.ai/svetlyoh/skills/kniferevive-concierge)
- [KnifeRevive storefront](https://kniferevive.com/shop/)
- [API workflow](references/api.md)
- [Sharpening booking requests](references/booking.md)
- [Published marketplace listing checkout](references/listing-checkout.md)
- [Payments](references/payments.md)
- [Sharpening service guide](references/sharpening.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Checkout links]

**Output Format:** [Conversational text or Markdown with itemized pricing, booking choices, and private merchant links when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices, coverage, payment availability, and booking status require live merchant verification.]

## Skill Version(s):

0.5.14 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
