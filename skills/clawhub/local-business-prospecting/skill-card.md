## Description:

Build and qualify local-business prospect lists by category and geography using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, Yelp, and public business websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to build deduplicated local-business prospect shortlists or CSV exports with contact fields, qualification evidence, source URLs, and retrieval status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prospecting queries, locations, target public URLs, and the Crawlora API key are sent to Crawlora.

Mitigation: Install and use the skill only when that data sharing is acceptable, keep the API key in an environment variable, and avoid entering sensitive private data.

Risk: The skill could be misused to collect private contacts or initiate outreach outside the user's request.

Mitigation: Use it for public business data, retain source pages for contact evidence, and perform outreach or CRM imports only when explicitly requested.

Risk: Business status, ratings, reviews, and location coverage may be incomplete or stale.

Mitigation: Refresh relevant candidates with live place detail, preserve unknown values as unknown, report shortfalls, and mark rows that were not refreshed.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/local-business-prospecting)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV, Shell commands, Configuration guidance, API calls]

**Output Format:** [Markdown tables or CSV, with optional shell commands and JSON API responses during collection]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prospect outputs should retain source URLs, retrieval timestamps, refresh status, qualification evidence, and exclusion reasons when applicable.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
