## Description:

WallySmarter-商品详情 helps agents retrieve a single Walmart product's current details plus WallySmarter price history and sales trends when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce analysts use this skill to inspect a known Walmart ItemId, including current product attributes, price history, and sales trend data. It is suited for single-product review rather than keyword search, bulk comparison, or category-level analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox account setup, SMS-code login, API-key output, paid plan purchase steps, and API requests to LinkFox/WallySmarter.

Mitigation: Prefer the official LinkFox site for signup, payment, and key management; run onboarding or payment commands only with clear user consent.

Risk: Environment variables can redirect LinkFox endpoints or expose account/API credentials to the configured service.

Mitigation: Review LINKFOX-related environment variables before running the skill and use only trusted endpoint values.

Risk: The skill can persist full API responses and local cache files in the workspace.

Mitigation: Review generated linkfox data/cache files before sharing the workspace or logs.

Risk: Product detail requests consume paid LinkFox credits, especially when historical statistics are included.

Mitigation: Confirm credit use before requests and set includeStats to false when historical data is unnecessary.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-wallysmarter-product-detail)
- [WallySmarter-商品详情 API reference](artifact/references/api.md)
- [Authentication and credits onboarding](artifact/references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)
- [WallySmarter product detail API endpoint](https://tool-gateway.linkfox.com/wallysmarter/productDetail)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries with JSON API responses and onboarding shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses may be written to local session data files and cached; historical coverage depends on WallySmarter tracking.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
