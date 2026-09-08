## Description:

Search Etsy listings, pull one listing with its variations and reviews, open a shop's profile and catalogue, and page through a shop's reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce researchers use this skill to query Etsy listing, shop, and review data through Scavio for market research, competitor analysis, and price comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Etsy search terms, listing IDs, shop names, and the Scavio API key to Scavio.

Mitigation: Keep the API key outside source control, disclose Scavio as the data processor, and only send user-approved queries.

Risk: API calls spend Scavio credits, including calls that return empty results.

Mitigation: Keep usage user-directed, confirm broad or repeated requests before running them, and monitor credit balance.

Risk: Buyer review text is user-generated content about real people.

Mitigation: Summarize reviews and avoid building individual profiles or fabricating review details.

## Reference(s):

- [Scavio Etsy API documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=etsy-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=etsy-product-data)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/etsy-product-data)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON API response examples and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns structured Etsy data from Scavio API calls.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
