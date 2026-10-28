## Description:

Screens startup launches, public traction signals, verified revenue profiles, and crowdfunding campaigns using Product Hunt, TrustMRR, and Kickstarter through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Founders, analysts, and acquisition researchers use this skill to compare public product launches, revenue profiles, and crowdfunding campaigns while preserving dates and source context. It supports initial screening, not private diligence or investment guarantees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, slugs, and campaign identifiers are sent to Crawlora with an API key.

Mitigation: Use a Crawlora-scoped key and keep private diligence material out of search queries.

Risk: Public revenue and campaign figures may be incomplete or change after collection.

Mitigation: Preserve source URLs and dates, and do not treat these snapshots as investment advice or proof of product delivery.

## Reference(s):

- [Startup Launch Research release](https://clawhub.ai/crawlora-org/skills/startup-launch-research)
- [Endpoint reference](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Dated Markdown research brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source URLs and collection timestamps; public, point-in-time signals.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
