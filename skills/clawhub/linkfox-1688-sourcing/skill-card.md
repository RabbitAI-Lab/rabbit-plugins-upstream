## Description:

1688 货源一站式 AI 工具集，整合商品搜索、热销榜单、以图搜图与已授权采购履约，覆盖找货、选品、比价、图搜同款与下单全流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and sourcing teams use this skill to search 1688 products and suppliers, compare prices and sales signals, find visually similar products from images, and complete authorized procurement steps. It is intended for LinkFox users with configured API access and, for procurement actions, active 1688 OAuth authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles API keys and login data.

Mitigation: Install only when LinkFox is trusted, keep API keys in environment variables, and ensure LinkFox endpoint environment variables are unset or point to trusted LinkFox hosts.

Risk: Local image upload can make product images publicly accessible for search.

Mitigation: Do not upload confidential or sensitive images, and use image search only with files that are safe to share with the LinkFox service.

Risk: Search and procurement responses may be saved or cached locally.

Mitigation: Periodically clean the local linkfox output and cache directories, and avoid placing sensitive response files in shared workspaces.

Risk: Procurement operations can create orders, request payment links, cancel orders, or confirm receipt.

Mitigation: Verify order details and require explicit user confirmation before create, payment-link, cancel, or confirm-receipt actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-sourcing)
- [LinkFox 1688 procurement reference](references/linkfox-1688-procurement.md)
- [LinkFox 1688 image search reference](references/linkfox-1688-search-by-image.md)
- [LinkFox product search reference](references/linkfox-dld-product-search.md)
- [LinkFox product billboard reference](references/linkfox-dld-product-billboard.md)
- [LinkFox onboarding reference](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce concise stdout summaries and local JSON data files for product search, image search, procurement, and onboarding responses.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
