## Description:

LinkFox 1688 Sourcing helps agents search 1688 products and bestseller lists, perform image-based matching, and guide authorized procurement steps such as SKU checks, order previews, ordering, payment links, order status, and logistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, sourcing teams, and procurement operators use this skill to find 1688 suppliers and products, compare bestseller or image-match results, and carry out authorized 1688 purchasing workflows with explicit confirmation for high-risk actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags combined purchasing authority, endpoint override flexibility, public image uploads, and local data handling as requiring careful review.

Mitigation: Install only when the LinkFox publisher is trusted, pin or review gateway environment variables, avoid sensitive or proprietary image uploads, and inspect local response storage behavior before use.

Risk: The skill can initiate high-impact procurement operations such as order creation, payment-link retrieval, cancellation, and receipt confirmation.

Mitigation: Require separate user confirmation for each high-risk procurement action and review order identifiers, amounts, addresses, and status before execution.

Risk: The skill requires an API key for LinkFox services, and onboarding output may expose credentials in logs or terminal history.

Mitigation: Treat API keys and onboarding credentials as secrets, avoid pasting them into shared logs, and rotate credentials if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-sourcing)
- [1688 procurement workflow reference](references/linkfox-1688-procurement.md)
- [1688 image search reference](references/linkfox-1688-search-by-image.md)
- [DLD product search reference](references/linkfox-dld-product-search.md)
- [DLD product billboard reference](references/linkfox-dld-product-billboard.md)
- [Authentication and billing onboarding reference](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, JSON, Markdown, Files]

**Output Format:** [Markdown guidance with shell commands and JSON request or response summaries; some scripts write full JSON responses to local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses LinkFox API-key authentication; search, billboard, and image-search scripts cache or save responses locally, while procurement scripts may save larger sanitized responses.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
