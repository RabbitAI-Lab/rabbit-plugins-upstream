## Description:

Search Yelp businesses in a metro, pull one business in full with hours, amenities and health inspections, and page through review bodies with owner responses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business teams use this skill to search Yelp businesses, retrieve detailed business profiles, and page through reviews for lead generation, reputation monitoring, local SEO, and competitor research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Yelp search terms, locations, business identifiers or URLs, and review filters are sent to Scavio under the user's API key.

Mitigation: Avoid sending confidential lead lists, sensitive addresses, or proprietary competitive research queries unless that use is acceptable for the organization.

Risk: Repeated paging or duplicate review requests can consume paid API credits.

Mitigation: Budget before paging, start review paging at page 2 after a business lookup, and stop when has_next_page is false.

Risk: Location-less searches can return data for the proxy exit location and produce inconsistent local results.

Mitigation: Provide an explicit location or a full Yelp search URL before relying on search output.

## Reference(s):

- [Scavio Yelp Search documentation](https://scavio.dev/docs/yelp-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=yelp-business-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=yelp-business-data)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/yelp-business-data)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline code examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Yelp endpoints cost 2 credits each.]

## Skill Version(s):

1.0.2 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
