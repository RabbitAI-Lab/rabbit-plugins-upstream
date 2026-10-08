## Description:

Compares public GoodRx pharmacy price snapshots for a user-specified prescription product and US location using Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

People comparing prescription costs use this skill to review posted pharmacy prices for a specified medication, form, strength, quantity, and US location without seeking medical advice or making a purchase.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Price lookups share searched medication, product details, location parameters, and an API key with Crawlora.

Mitigation: Use only when comfortable sharing these details, and do not transmit medical or prescription records.

Risk: Posted price snapshots may not reflect stock, final cost, or insurance coverage.

Mitigation: Show source and collection time, keep price categories separate, and confirm eligibility and final cost with the pharmacy.

Risk: A lower price might be mistaken for a clinical recommendation.

Mitigation: Keep the requested product fixed and refer medication or dosing decisions to a qualified clinician or pharmacist.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/prescription-price-research)
- [GoodRx price endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown pharmacy-price table with product options, sources, and timestamps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates price and eligibility categories; includes questions to confirm with pharmacies.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
