## Description:

Discover and compare suppliers behind brands using Crawlora's ImportYeti company reports and public business websites for supplier shortlists, observed sourcing relationships, shipment-activity comparisons, and questions to qualify potential manufacturers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sourcing teams, and developers use this skill to build supplier shortlists from ImportYeti company reports, public business websites, and Crawlora search and extraction endpoints. It helps compare observed sourcing relationships and shipment activity while preserving open qualification questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the user's API key, supplier names, search queries, request bodies, and public URLs submitted through the skill.

Mitigation: Keep the API key in the environment rather than hardcoding it, and avoid sending confidential sourcing plans or private URLs unless sharing them with Crawlora is acceptable.

Risk: Shipment records and extracted public-page data can be incomplete or ambiguous, so results may overstate sourcing relationships or supplier qualifications.

Mitigation: Treat shipment records as observations, preserve source URLs and collection time, compare only compatible coverage windows, and label MOQ, lead time, certifications, capacity, and availability as unknown unless directly supported.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ImportYeti coverage notes](https://www.importyeti.com/our-data)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown supplier shortlist with linked evidence and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes observed supplier, country or address, customer relationship, product evidence, shipment metric and date scope, official website, fit rationale, and open qualification questions.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
