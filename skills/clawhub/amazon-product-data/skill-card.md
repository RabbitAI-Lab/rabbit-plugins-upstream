## Description:

Search Amazon, read full product detail by ASIN, and list every seller offer on an ASIN with the buy-box winner.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Amazon marketplaces, look up product details by ASIN, and compare seller offers through Scavio's API for ecommerce and retail research workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Scavio API key grants access to paid API usage if exposed.

Mitigation: Load SCAVIO_API_KEY from an environment variable or secret store, and avoid committing or logging it.

Risk: Search, product, and offers calls consume Scavio credits, including empty searches.

Mitigation: Confirm before deep pagination or bulk ASIN lookups, and use the free options endpoint to validate marketplaces.

Risk: The optional LangChain package adds third-party dependency exposure.

Mitigation: Use direct HTTPS calls when possible, or install the package in an isolated environment without elevated privileges.

Risk: Amazon marketplace results can be unsorted, rounded in search counts, or limited to the first page of offers.

Mitigation: State when data was fetched, sort locally only when needed, avoid exact claims from rounded search counts, and label offers as first-page results when applicable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/amazon-product-data)
- [Scavio Amazon API Documentation](https://scavio.dev/docs/amazon-api?utm_source=agent-skills&utm_medium=skill&utm_campaign=amazon-product-data)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=amazon-product-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; data endpoints consume Scavio credits; API responses are normalized JSON.]

## Skill Version(s):

1.0.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
