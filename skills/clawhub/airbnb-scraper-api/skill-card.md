## Description:

Search Airbnb stays with the full discount ledger, pull one listing with its complete amenity list and rating breakdown, and page through real review bodies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to search Airbnb stays, inspect listing details, and page through reviews for travel planning, short-term-rental market research, comp sets, and host analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls consume Scavio credits and send Airbnb search, listing, or review requests through Scavio using the user's API key.

Mitigation: Confirm the request scope before calling endpoints, use explicit pagination limits, and avoid unnecessary retries.

Risk: Review text and host profile fields may contain personal data about real people.

Mitigation: Summarize personal data when possible, avoid profiling individuals, and share only data needed for the user's task.

Risk: Search prices can be misleading when dates or currency are omitted because Airbnb may default or A/B test the result window and pricing.

Mitigation: Send explicit check_in, check_out, and currency values, and do not present prices as date-specific when dates_are_defaulted is true.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/airbnb-scraper-api)
- [Scavio Airbnb Search Documentation](https://scavio.dev/docs/airbnb-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline code examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. API requests use POST JSON bodies and each Airbnb endpoint call consumes 1 Scavio credit.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
