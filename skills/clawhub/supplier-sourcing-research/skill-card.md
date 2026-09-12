## Description:

Discover and compare suppliers behind brands using Crawlora's ImportYeti company reports and public business websites. Use for supplier shortlists, observed sourcing relationships, shipment-activity comparisons, and questions to qualify potential manufacturers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sourcing teams, and developers use this skill to build supplier shortlists from observed shipment relationships, public company reports, and business websites. It supports comparison and qualification planning, not conclusions about manufacturing quality, capacity, or willingness to sell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper sends the user's Crawlora API key and research queries to Crawlora.

Mitigation: Keep the API key in the environment, review query and request-body contents before running the helper, and install only if that data sharing is acceptable.

Risk: Search locale defaults may not match non-US or non-English sourcing contexts.

Mitigation: Pass explicit country and language parameters when local market context matters.

Risk: Shipment records and scraped public pages can be incomplete, ambiguous, or stale.

Mitigation: Treat shipment records as observations, preserve raw dates and source URLs, report unknown qualification fields, and verify supplier identity before relying on results.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ImportYeti coverage notes](https://www.importyeti.com/our-data)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with cited supplier evidence and optional shell commands returning JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve source URLs, shipment metric scope, raw ambiguous dates, and open qualification questions.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
