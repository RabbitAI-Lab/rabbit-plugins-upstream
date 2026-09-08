## Description:

Search live and sold eBay listings, retrieve full listing details, and look up seller profile cards as structured JSON through Scavio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill for eBay resale research, listing lookup, seller profile checks, and price comparison against other retail sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-directed eBay search terms, item IDs, and seller names to Scavio.

Mitigation: Use the skill only when sharing those lookup inputs with Scavio is acceptable for the user's data-handling requirements.

Risk: The skill uses a Scavio API key with credit-based billing.

Mitigation: Store SCAVIO_API_KEY in an environment variable or secret store and monitor credits_used and credits_remaining in API responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/ebay-product-data)
- [Scavio eBay search documentation](https://scavio.dev/docs/ebay-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio eBay product documentation](https://scavio.dev/docs/ebay-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio eBay seller documentation](https://scavio.dev/docs/ebay-seller?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Structured JSON from Scavio API calls with concise text or Markdown summaries, code snippets, and shell configuration commands when setup is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; Scavio endpoints use credit-based billing and return credits_used and credits_remaining in the response envelope.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
