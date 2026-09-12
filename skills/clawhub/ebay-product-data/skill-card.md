## Description:

Search live and sold eBay listings, read full listings, and look up seller profile cards as structured JSON through Scavio's eBay endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research eBay resale prices, compare live and sold listings, inspect listing details, and review seller profile data. It is suited for marketplace research, resale pricing, seller checks, and product data workflows that need structured JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Scavio API key and consumes Scavio credits for eBay data lookups.

Mitigation: Keep SCAVIO_API_KEY in an environment variable or secret store, avoid committing it to source code, and monitor credit usage.

Risk: Returned eBay listing and seller data may be used for pricing or marketplace decisions.

Mitigation: Verify returned listing URLs and include sale timing when using sold-listing prices as market evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/ebay-product-data)
- [Scavio eBay search documentation](https://scavio.dev/docs/ebay-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio eBay product documentation](https://scavio.dev/docs/ebay-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio eBay seller documentation](https://scavio.dev/docs/ebay-seller?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands, Python examples, and structured JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each documented endpoint uses Scavio credits and returns data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
