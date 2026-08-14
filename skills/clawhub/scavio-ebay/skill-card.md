## Description:

Search live or SOLD eBay listings, read a listing in full, and look up a seller's profile card as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce analysts use this skill to research eBay sold prices, inspect live listings, retrieve listing details, and check seller profile data through Scavio's eBay API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: eBay search terms, item IDs, or seller names are sent to Scavio, and searches consume Scavio credits.

Mitigation: Use a dedicated Scavio API key, avoid submitting sensitive private notes as query text, and be deliberate with high-volume searches.

Risk: Marketplace results can be misread if the agent fabricates missing values or treats incomplete sold-listing counts as zero.

Mitigation: Return only API-provided prices, dates, item numbers, feedback scores, and seller names; when sold totals are null, count returned rows and explain that eBay did not publish a headline count.

## Reference(s):

- [Scavio eBay Search Documentation](https://scavio.dev/docs/ebay-search)
- [Scavio eBay Product Documentation](https://scavio.dev/docs/ebay-product)
- [Scavio eBay Seller Documentation](https://scavio.dev/docs/ebay-seller)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown instructions with inline bash and Python examples; API responses are structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SCAVIO_API_KEY for authenticated Scavio API calls; each endpoint is documented as costing 1 credit.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
