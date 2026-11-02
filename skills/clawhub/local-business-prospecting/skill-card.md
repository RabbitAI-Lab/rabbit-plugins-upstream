## Description:

Build and qualify local-business prospect lists by category and geography using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, Yelp, and public business websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to research and qualify local businesses by category and geography, then receive a deduplicated shortlist or CSV with contact details and source evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search criteria and target website URLs are sent to Crawlora, and requests consume API credits.

Mitigation: Keep the API key private and bound discovery and enrichment to the requested research scope.

Risk: Business contact details could be used for outreach beyond the research task.

Mitigation: Collect only publicly published business contacts, retain their source pages, and do not send outreach or import results into a CRM unless requested.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Skill release page](https://clawhub.ai/crawlora-org/skills/local-business-prospecting)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Files, Guidance]

**Output Format:** [Markdown table or CSV with business details, qualification evidence, source URLs, and retrieval status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deduplicated business shortlist; reports shortfalls and preserves source evidence.]

## Skill Version(s):

1.0.14 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
