## Description:

Macy's Research retrieves product details, reviews, rating summaries, and typeahead suggestions for known Macy's product IDs through the Crawlora API, returning normalized JSON without scraping HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve Macy's product pricing, descriptions, variants, reviews, rating summaries, and typeahead suggestions when they already have a numeric productId or a partial query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated requests may go beyond the documented GET-only Macy's examples.

Mitigation: Use only the documented GET routes for product details, reviews, and suggestions; avoid arbitrary -X POST calls.

Risk: Unvalidated or non-numeric product IDs may broaden requests outside the intended Macy's product lookup flow.

Mitigation: Validate product IDs as numeric Macy's IDs before invoking the helper.

Risk: Crawlora API usage can consume account credits.

Mitigation: Monitor API credit use and scope the API key to this workflow where possible.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/macys-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses with Markdown usage guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and a known numeric Macy's productId for product detail or review retrieval; typeahead suggestions require a query string.]

## Skill Version(s):

1.0.13 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
