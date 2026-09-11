## Description:

Search Etsy listings, pull one listing with its variations and reviews, open a shop's profile and catalogue, and page through a shop's reviews. 5 endpoints, 2 credits each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce researchers use this skill to search Etsy listings, inspect product and shop data, compare prices, and summarize shop or listing reviews through Scavio's structured Etsy API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key for a third-party service.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and do not commit it to source control.

Risk: API calls consume credits, including calls that return empty results.

Mitigation: Monitor credits_used and credits_remaining in responses and narrow or test queries before running large batches.

Risk: Returned buyer review text may contain personal or sensitive context.

Mitigation: Summarize review trends and avoid profiling individual reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/etsy-product-data)
- [Scavio documentation](https://scavio.dev/docs?utm_source=agent-skills&utm_medium=skill&utm_campaign=etsy-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=etsy-product-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides API calls that return structured JSON envelopes with data, response_time, credits_used, and credits_remaining fields.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
