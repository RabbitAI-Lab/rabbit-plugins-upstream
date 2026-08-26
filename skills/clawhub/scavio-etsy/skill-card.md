## Description:

Search Etsy listings, pull one listing with its variations and reviews, open a shop's profile and catalogue, and page through a shop's reviews. 5 endpoints, 2 credits each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce researchers use this skill to query public Etsy listing, shop, and review data through Scavio for product discovery, market research, competitor analysis, and price comparison.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Etsy lookup requests are sent to Scavio using SCAVIO_API_KEY, and each request consumes credits.

Mitigation: Use the skill only for public Etsy data intended for querying through Scavio, keep the API key in a secret store or environment variable, and confirm the request before spending credits.

Risk: Returned review text is written by real buyers and may contain personal or subjective content.

Mitigation: Summarize review content and avoid building profiles of individual reviewers.

## Reference(s):

- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=etsy-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=etsy-product-data)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-etsy)
- [Publisher profile](https://clawhub.ai/user/scavio-ai)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, text]

**Output Format:** [Markdown with JSON, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides API calls that return structured JSON envelopes with Etsy listing, shop, review, credit, and response-time data.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
