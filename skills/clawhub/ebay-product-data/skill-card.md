## Description:

Search live or SOLD eBay listings, read a listing in full, and look up a seller's profile card as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to research eBay resale prices, inspect live or sold listings, and retrieve public seller profile data through Scavio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends eBay queries, item IDs, and seller names to Scavio using a third-party API key.

Mitigation: Use the skill only when that data sharing is acceptable, and store SCAVIO_API_KEY in the environment or a secret store instead of source code.

Risk: Each endpoint call spends Scavio API credits and an exhausted balance returns a billing path.

Mitigation: Monitor credits_used and credits_remaining in responses, and require an intentional top-up before continuing after a 402 response.

Risk: Marketplace data can be incomplete or misleading if filters, category IDs, or sold-listing counts are treated as stronger evidence than the API provides.

Mitigation: Return only API-provided prices, seller data, item IDs, and dates; include listing URLs and describe null sold-listing totals as unavailable rather than zero.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/ebay-product-data)
- [Scavio eBay search documentation](https://scavio.dev/docs/ebay-search)
- [Scavio eBay product documentation](https://scavio.dev/docs/ebay-product)
- [Scavio eBay seller documentation](https://scavio.dev/docs/ebay-seller)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API response examples and shell or Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses use structured JSON envelopes with data, response_time, credits_used, and credits_remaining.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
