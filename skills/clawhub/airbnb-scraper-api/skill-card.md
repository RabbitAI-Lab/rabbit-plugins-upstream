## Description:

Search Airbnb stays with the full discount ledger, pull one listing with its complete amenity list and rating breakdown, and page through real review bodies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to search Airbnb stays, inspect listing details, retrieve rating breakdowns, and page through guest reviews for travel planning, short-term rental comparison, market research, and host analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Airbnb locations, dates, filters, listing IDs, and review lookup requests to Scavio using the configured API key.

Mitigation: Use the skill only when sharing those travel/search inputs with Scavio is acceptable for the user and organization.

Risk: Each endpoint call consumes paid API credits, including empty result pages and review pagination.

Mitigation: Set explicit page, cursor, limit, and offset bounds before bulk searches or review collection.

Risk: Dateless searches may use defaulted dates and A/B-tested prices that should not be treated as answers for a user's specific travel window.

Mitigation: Send explicit check-in and check-out dates for price-sensitive requests and avoid quoting prices when the response indicates defaulted dates.

Risk: Review text and host profiles may contain personal data about real people.

Mitigation: Summarize personal data and avoid building profiles of individual guests, reviewers, or hosts.

## Reference(s):

- [Scavio Airbnb Search Documentation](https://scavio.dev/docs/airbnb-search)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/airbnb-scraper-api)
- [ClawHub Publisher Profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON-oriented API examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for calling Scavio Airbnb search, listing, and reviews endpoints; endpoint responses are structured JSON.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
