## Description:

Search Google Maps for local businesses and places, fetch full place details, read place reviews, and run a local-SEO geo-grid to track where a business ranks across an NxN lattice of points, as structured JSON. Four endpoints on the v2 engine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to find local businesses, retrieve place details and reviews, and measure local search rankings across a geographic grid. It can also pass a place ID to Company Enrich to retrieve published business contact details and owner information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and location information are sent to Scavio, and the optional enrichment workflow sends a place ID for business and owner details.

Mitigation: Review the information in each request and use the separate enrichment step only when its contact and owner details are needed.

## Reference(s):

- [Google Maps API documentation](https://scavio.dev/docs/google-maps?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-maps-api)
- [Company Enrich documentation](https://scavio.dev/docs/company-enrich?utm_source=agent-skills&utm_medium=skill&utm_campaign=google-maps-api)
- [ClawHub skill release](https://clawhub.ai/scavio-ai/skills/google-maps-api)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured JSON containing place search results, place details, reviews, and geo-grid ranking results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include business contact and owner details when the separate Company Enrich step is used.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
