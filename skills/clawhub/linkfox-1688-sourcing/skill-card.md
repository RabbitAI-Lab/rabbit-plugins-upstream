## Description:

1688 货源一站式 AI 工具集，整合商品搜索、热销榜单、以图搜图与已授权采购履约，覆盖找货、选品、比价、图搜同款与下单全流程。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, operators, and sourcing teams use this skill to search 1688 products and suppliers, compare prices and sales signals, find visually similar products from images, and manage authorized 1688 procurement steps including order preview, creation, payment link retrieval, order status, logistics, cancellation, and receipt confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform order-changing 1688 procurement actions, including creating orders, retrieving payment links, cancelling orders, and confirming receipt.

Mitigation: Require a separate explicit user confirmation for each high-risk action and review the account, item, quantity, amount, order ID, and status before execution.

Risk: The skill sends credential-bearing requests to LinkFox and 1688 services.

Mitigation: Store the LinkFox API key only in supported environment variables, review configured gateway variables, and never paste 1688 tokens, refresh tokens, app secrets, or Authorization headers into prompts.

Risk: Image search may transmit product images and search data to LinkFox or 1688 services, and local image uploads create public URLs.

Mitigation: Avoid uploading confidential, personal, or proprietary images; use only images that are acceptable to share with the service.

Risk: Search, image-search, procurement, and cache outputs may persist locally with product, order, address, or logistics details.

Mitigation: Periodically clean the local linkfox output and cache directories, especially on shared machines, and avoid forcing full inline output unless needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-sourcing)
- [1688采购全流程（1688 Procurement Workflow）](artifact/references/linkfox-1688-procurement.md)
- [1688 以图搜图（1688 Image-Based Product Search）](artifact/references/linkfox-1688-search-by-image.md)
- [1688 商品热销榜单（DLD Product Billboard）](artifact/references/linkfox-dld-product-billboard.md)
- [1688 商品搜索（DLD Product Search）](artifact/references/linkfox-dld-product-search.md)
- [解决认证和积分问题](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples and JSON API responses or saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call LinkFox gateway APIs, upload local images to public URLs for image search, and save full responses or cache files under local linkfox output directories.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
