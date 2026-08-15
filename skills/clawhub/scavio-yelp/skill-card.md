## Description:

Search Yelp businesses in a metro, pull one business in full with hours, amenities and health inspections, and page through review bodies with owner responses. 3 endpoints, 2 credits each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to query Scavio's Yelp endpoints for local business search, business detail records, and review pages when building lead lists, reputation monitoring, or competitor research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Yelp queries are sent to Scavio and API calls consume credits.

Mitigation: Keep SCAVIO_API_KEY private, budget pagination before making calls, and monitor credits_used and credits_remaining in responses.

Risk: Review paging or missing location values can produce duplicate charges, billed empty responses, or geographically inconsistent results.

Mitigation: Start review pagination at page 2 after /yelp/business, stop when has_next_page is false, and include a location or full Yelp URL for searches.

Risk: Yelp filters and recommendation behavior can make returned data incomplete or different from the user's requested filter.

Mitigation: Verify applied filters in returned results, report not_recommended_review_count where relevant, and avoid claiming completeness for omitted popular items or hidden reviews.

## Reference(s):

- [Scavio Yelp documentation](https://scavio.dev/docs/yelp-search)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-yelp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, API Calls, Configuration]

**Output Format:** [Markdown guidance with JSON API examples and Python, JavaScript, and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses are structured JSON envelopes with credit usage fields.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
