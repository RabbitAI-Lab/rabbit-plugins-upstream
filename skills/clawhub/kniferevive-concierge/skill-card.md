## Description:

Helps shoppers compare KnifeRevive's SF Bay Area sharpening services and Annex technology listings, then prepare authorized bookings or secure checkout handoffs when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[svetlyoh](https://clawhub.ai/user/svetlyoh)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and their agents use this skill to compare KnifeRevive sharpening services in the San Francisco Bay Area or technology listings, check current terms and availability, and prepare a customer-approved purchase or booking handoff.

### Deployment Geography for Use:

San Francisco Bay Area, California, United States, for sharpening services; technology listings online subject to merchant availability and fulfillment terms.

## Known Risks and Mitigations:

Risk: A quote or listing may not reflect final prices, availability, delivery terms, or booking status.

Mitigation: Check live merchant terms and the final itemized total before approval; confirm payment and appointment status separately.

Risk: A payment, wallet transfer, or appointment could proceed without the shopper's informed consent.

Mitigation: Require explicit transaction authorization and the merchant's first-party approval flow; use only an independently authorized wallet or secure checkout handoff.

Risk: Shopper contact, courier, or private checkout details could be exposed.

Mitigation: Collect only necessary fulfillment details through the merchant review page when possible, and keep private links and session tokens out of shared messages.

## Reference(s):

- [KnifeRevive Concierge ClawHub listing](https://clawhub.ai/svetlyoh/skills/kniferevive-concierge)
- [API workflow](artifact/references/api.md)
- [Sharpening and physical handoff](artifact/references/sharpening.md)
- [Payments](artifact/references/payments.md)
- [Installation and agent prompts](artifact/references/installation.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown]

**Output Format:** [Text or Markdown summaries, comparisons, quotes, and checkout handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payment and booking status require separate merchant verification.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
