## Description:

Helps agents use LinkFox gateway scripts and references to publish and manage Temu Partner US products, including V2 product creation, category attributes, specifications, image upload, listings, edits, category mapping, SKU inventory, and supply pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and developers use this skill to prepare Temu US product publishing workflows and run LinkFox-proxied Partner US product API scripts for product creation, catalog lookup, editing, stock, and price tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox account keys and Temu seller access tokens.

Mitigation: Install it only when the publisher is trusted, use appropriately scoped credentials, and prefer a secret manager or protected environment variables for sensitive tokens.

Risk: The skill can store Temu tokens and full API responses in local LinkFox files that may include business data or credentials.

Mitigation: Protect or delete the generated linkfox and ~/.linkfox files when they contain sensitive data, and use a secured token-store path when local storage is necessary.

Risk: Gateway override environment variables can redirect requests away from the default LinkFox gateway.

Mitigation: Use gateway overrides only in trusted testing environments and clear them before normal commercial use.

Risk: The broader LinkFox helper scripts include billing or order actions and product mutation workflows that can affect an account.

Mitigation: Review commands and JSON payloads before execution, avoid blind retries, and require user confirmation before actions that spend credits or modify catalog, stock, price, billing, or order state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-add-product-us)
- [API reference](references/api.md)
- [Temu access token authorization](references/access-token.md)
- [Authorization flow](references/authorization-flow.md)
- [Onboarding and account setup](references/onboarding.md)
- [Partner US catalog](references/partner-us-catalog.md)
- [Product publish APIs](references/product-publish-apis.md)
- [Product query APIs](references/product-query-apis.md)
- [Product edit APIs](references/product-edit-apis.md)
- [Category, attribute, and specification APIs](references/category-spec-apis.md)
- [Stock and price APIs](references/stock-price-apis.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON request/response examples; scripts write full JSON responses to local files and print small responses or summaries to stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LinkFox and Temu credentials; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
