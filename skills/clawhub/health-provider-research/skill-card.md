## Description:

Find and compare public Healthgrades directory records for physicians, hospitals, pharmacies, urgent care, and group practices through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents researching US healthcare options can assemble source-attributed provider and facility shortlists by specialty, location, and directory attributes. Confirm insurance coverage, availability, and costs directly with providers or insurers.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Directory ratings, awards, filters, and profiles may be mistaken for verified clinical quality or medical advice.

Mitigation: Attribute directory claims to their sources and dates; avoid diagnosis, treatment recommendations, and unsupported quality rankings.

Risk: Insurance listings and appointment filters may not reflect current network status, availability, or out-of-pocket costs.

Mitigation: Mark these details as unconfirmed and direct users to the provider or insurer for verification.

Risk: Provider searches could disclose unnecessary personal medical details to Crawlora.

Mitigation: Use only the minimum search details needed and avoid submitting patient or insurance information unless the user explicitly requests it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/health-provider-research)
- [Healthgrades endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown provider or facility shortlist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes directory source URLs, collection times, relevant attributes, and questions needing direct confirmation; not a clinical recommendation.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
