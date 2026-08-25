## Description:

Search Etsy listings, pull one listing with its variations and reviews, open a shop's profile and catalogue, and page through a shop's reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and market researchers use this skill to search Etsy listings, inspect shops and products, compare prices, and retrieve review data through Scavio's structured Etsy API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Scavio as a third-party service for Etsy lookups and requires a Scavio API key.

Mitigation: Store SCAVIO_API_KEY as a secret, confirm the user is comfortable using Scavio, and avoid unnecessary private or identifying search terms.

Risk: Each Etsy endpoint call consumes credits, including calls that return empty results.

Mitigation: Check filters before making requests, monitor credit usage, and handle rate or usage limits by waiting before retrying.

## Reference(s):

- [Scavio Documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=etsy-product-data)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=etsy-product-data)
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/etsy-product-data)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with HTTP request examples and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Etsy API calls cost 2 credits each and return a data envelope with response time, credits used, and credits remaining.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
