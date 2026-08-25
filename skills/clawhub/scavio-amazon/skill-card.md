## Description:

Search Amazon, retrieve full product details by ASIN, and list seller offers with buy-box status as normalized JSON across 22 marketplaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Amazon products, inspect ASIN-level product details, compare seller offers, and include returned Amazon URLs for verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Amazon searches and ASIN lookups are sent to Scavio and most data endpoints bill credits.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store and avoid broad automated loops unless the user intends the credit usage.

Risk: Product prices, availability, delivery estimates, and seller offers are point-in-time marketplace data.

Mitigation: Include the returned Amazon URL and have users verify important product or seller details before acting on them.

Risk: Search results are not sorted by Amazon, and search review counts may be rounded when Amazon abbreviates them.

Mitigation: Sort returned pages locally only when needed, disclose local sorting, and avoid treating rounded search review counts as exact.

## Reference(s):

- [Scavio Amazon API documentation](https://scavio.dev/docs/amazon-api)
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-amazon)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, text, markdown]

**Output Format:** [Markdown with JSON, bash, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to call Scavio Amazon endpoints and return normalized product, price, availability, shipping, and seller data.]

## Skill Version(s):

3.0.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
