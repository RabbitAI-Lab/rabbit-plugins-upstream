## Description:

Search live or SOLD eBay listings, read a listing in full, and look up a seller's profile card as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external marketplace researchers use this skill to query Scavio's eBay endpoints for sold-price research, live listing search, listing details, and public seller profile data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and API calls are sent to Scavio and each call spends one Scavio credit.

Mitigation: Confirm the user is comfortable sending eBay research queries to Scavio and spending credits before making API calls.

Risk: The Scavio API key could be exposed if placed in source files or shared examples.

Mitigation: Keep SCAVIO_API_KEY in the environment or a secret store rather than source files.

Risk: Marketplace results can be misleading if prices, sold dates, seller data, or item numbers are invented or detached from returned API data.

Mitigation: Return only values present in the API response, quote sold prices with the sale timing when available, and include listing URLs for verification.

## Reference(s):

- [Scavio eBay Search Documentation](https://scavio.dev/docs/ebay-search)
- [Scavio eBay Product Documentation](https://scavio.dev/docs/ebay-product)
- [Scavio eBay Seller Documentation](https://scavio.dev/docs/ebay-seller)
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON request examples, Python examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides calls that return structured JSON envelopes containing data, response time, credits used, and credits remaining.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
