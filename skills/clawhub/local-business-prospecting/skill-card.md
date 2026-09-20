## Description:

Build and qualify local-business prospect lists by category and geography using Crawlora's Google Maps dataset, live Google Maps, Apple Maps, Yelp, and public business websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research local businesses, qualify candidates against explicit criteria, and produce a deduplicated prospect shortlist or CSV with contact and source evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends prospecting queries and selected public business URLs to Crawlora's service.

Mitigation: Keep the API key in the environment, install only if this service use is acceptable, and avoid placing secrets in prompts, command arguments, or generated prospect lists.

Risk: Prospect lists may include stale, incomplete, or unknown business status data.

Mitigation: Review generated prospect lists before outreach or CRM use, preserve source URLs and retrieval times, refresh high-value candidates, and report shortfalls instead of padding weak matches.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/local-business-prospecting)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown table or CSV with inline shell commands when API calls are needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include business names, provider IDs, addresses, websites, public phone and email, ratings, review counts, qualification evidence, source URLs, retrieval timestamps, refresh status, and exclusion reasons.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
