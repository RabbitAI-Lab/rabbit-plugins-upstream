## Description:

查询 TikTok Shop 公共商品详情，支持商品 URL 或 19 位商品 ID 和多个区域，返回价格、库存、SKU、媒体、店铺、评论、物流和促销等当前公开数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch the current public detail snapshot for one known TikTok Shop product by URL or 19-digit product ID, then review listing data such as title, category, price, SKU inventory, media, seller, reviews, shipping, and promotions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide phone-based login and API-key issuance.

Mitigation: Prefer the LinkFox self-service account portal for credentials, avoid sharing phone codes or API keys in chat transcripts, and rotate any key that may have been exposed.

Risk: The onboarding flow can create payment orders and render payment QR codes.

Mitigation: Confirm the billing plan and payment method with the user before order creation, and avoid automatic retries or polling that could create confusion or extra charges.

Risk: Full API responses and cache files may be written to local LinkFox output directories.

Mitigation: Clean or exclude the LinkFox output/cache directory from shared repositories and review saved files before sharing a workspace.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-product-detail)
- [TikTok Shop 商品详情 API 参考](artifact/references/api.md)
- [解决认证和积分问题](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with JSON response files and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One product per call; large API responses are saved locally and summarized for the agent.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
