## Description:

Builds and qualifies local-business prospect lists by category and geography using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, Yelp, and public business websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and business-development teams use this skill to research, deduplicate, and qualify local-business prospects, with public contact details and source evidence for review before outreach or CRM import.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora API requests expose prospecting queries and public business-site URLs to a third-party provider; an exposed API key could permit unauthorized use.

Mitigation: Use an authorized Crawlora API key, keep it out of logs, and limit queries and site scraping to the requested task.

Risk: Lead lists can contain stale, inaccurate, or unsuitable contact and qualification information.

Mitigation: Retain source evidence and retrieval dates; review accuracy and applicable outreach requirements before contacting prospects or importing records into a CRM.

## Reference(s):

- [Crawlora endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/local-business-prospecting)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV]

**Output Format:** [Markdown table or CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Business contacts, qualification evidence, source URLs, retrieval dates, and refresh status; may report shortfalls or unverified records.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
