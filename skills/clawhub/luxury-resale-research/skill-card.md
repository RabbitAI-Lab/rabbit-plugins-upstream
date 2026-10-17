## Description:

Research luxury-fashion and watch resale listings, sold evidence, condition, and seller signals across specialist marketplaces for sourcing and evidence comparison, not buying or appraisal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Resale researchers and shoppers compare public luxury-fashion and watch listings, sold evidence where available, condition descriptions, and seller signals across specialist marketplaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, listing URLs, and seller identifiers are sent to Crawlora with an API key when research is requested.

Mitigation: Use the skill only when comfortable sharing those query details with Crawlora; keep the API key private.

Risk: Public listing information may be mistaken for a verified sale, authentication, appraisal, or complete purchase cost.

Mitigation: Separate asking prices from sold evidence, identify source-stated signals, and leave unsupported fees, shipping, duties, or sale details unestimated.

Risk: The available routes also cover broader retail and editorial information outside a resale comparison.

Mitigation: Use those routes only when relevant to the requested research.

## Reference(s):

- [Luxury Resale Research release](https://clawhub.ai/crawlora-org/skills/luxury-resale-research)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown comparison table or JSON list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates active asks from sold evidence and labels unavailable fields.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
