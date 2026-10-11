## Description:

Helps agents retrieve live Amazon product, pricing, review, search, deal, stock, and seller data across 23 marketplaces through Apiguru.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apiguru-app](https://clawhub.ai/user/apiguru-app)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer specific Amazon marketplace questions about products, prices, reviews, inventory, deals, and sellers, or to monitor those details with the user's approval for paid requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests with a user-provided API key may incur charges, including unsuccessful product lookups or calls that time out locally.

Mitigation: Use the free keyless path first, confirm pricing and a spending cap before keyed calls, and ask before retrying timed-out paid requests.

Risk: Feedback submissions are publicly visible and could expose private details.

Mitigation: Submit feedback only with the user's consent, and omit API keys, personal data, prompts, and private results.

Risk: Marketplace results can omit fields or misrepresent a specific product variant.

Mitigation: Confirm the marketplace and inspect full product details before making variant-specific claims.

## Reference(s):

- [Apiguru project homepage (listed in release metadata)](https://github.com/apiguru-app/agent-kit)
- [Apiguru endpoint reference](references/endpoints.md)
- [Apiguru costs and error handling](references/errors-and-costs.md)
- [Apiguru API capabilities and prices](https://agent.apiguru.app/.well-known/x402)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with structured Amazon marketplace data and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested Amazon marketplace and the availability of live API data.]

## Skill Version(s):

1.1.52 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
