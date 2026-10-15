## Description:

Build pet-care or dog-training shortlists from public Rover listings and profiles accessed through Crawlora, preserving price units, location fit, review context, and unresolved availability and qualification questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and their assistants use this skill to compare local sitters, walkers, or dog trainers by advertised services, starting rates, experience claims, and public review excerpts, then identify questions to confirm before choosing a provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search criteria sent to Crawlora may expose sensitive location or pet-care details, and the API requires a key.

Mitigation: Use a Crawlora key only if comfortable with that data flow; minimize home, medical, and account details in searches and comparisons.

Risk: Public listing prices, qualifications, reviews, and availability may be incomplete or unverified.

Mitigation: Attribute provider claims, keep price units and unknown fees explicit, and confirm availability, credentials, and care requirements directly before deciding.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/pet-care-provider-shortlisting)
- [Crawlora Rover endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown provider shortlist and requirement matrix]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes attributed listing evidence, price units, unresolved criteria, and availability questions; does not book providers.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
