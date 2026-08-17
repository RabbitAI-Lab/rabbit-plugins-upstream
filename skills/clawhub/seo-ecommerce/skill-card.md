## Description:

E-commerce SEO analysis for Google Shopping visibility, Amazon marketplace intelligence, product schema validation, competitor pricing analysis, and marketplace keyword gaps, combining on-page product SEO with optional DataForSEO Merchant API data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, SEO practitioners, and e-commerce operators use this skill to audit product pages, validate Product schema, compare marketplace listings, identify keyword gaps, and prepare merchant sites for shopping and agentic-commerce discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch product or store URLs and optionally probe UCP endpoints.

Mitigation: Run active endpoint probing only for sites the user owns or is authorized to assess; use non-probing analysis when authorization is unclear.

Risk: Optional DataForSEO Merchant API calls may incur paid request charges.

Mitigation: Use the documented cost checks and obtain user approval before paid Google Shopping or Amazon marketplace calls.

Risk: SEO and schema recommendations may be incomplete or unsuitable for a specific merchant implementation.

Mitigation: Review recommendations before publishing changes to product pages, Merchant Center feeds, schema markup, or checkout-related configuration.

## Reference(s):

- [DataForSEO Merchant API Reference](artifact/references/marketplace-endpoints.md)
- [UCP - Universal Commerce Protocol](artifact/references/ucp-universal-commerce-protocol.md)
- [Schema.org](https://schema.org)
- [Google Merchant UCP Developer Guide](https://developers.google.com/merchant/ucp)
- [UCP Spec and Overview](https://ucp.dev)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with tables, scores, recommendations, JSON schema snippets, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include optional paid marketplace API analysis when credentials and user approval are available; otherwise produces on-page and schema guidance from fetched pages.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
