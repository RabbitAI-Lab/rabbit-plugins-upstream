## Description:

LinkFox TikTok Product Selection and Shoppable Video integrates EchoTik and FastMoss product data with TikTok official shoppable-video APIs for TikTok Shop product research, trend analysis, promotional-video analysis, OAuth/token workflows, and shoppable-video publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, creators, affiliate-commerce operators, and developers use this skill to research TikTok Shop products, analyze bestseller and new-product trends, inspect promotional-video performance, manage TikTok creator authorization, and publish shoppable videos through the supported API flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys and TikTok OAuth-linked creator tokens.

Mitigation: Install only in trusted environments, keep gateway environment variables private, mask tokens in user-facing output, and avoid committing local output directories.

Risk: The skill can publish public TikTok shoppable videos through the official video API flow.

Mitigation: Confirm the creator account, product_id, file_id, caption/title, and publish intent before calling publish endpoints; use precheck and status endpoints to review results.

Risk: The onboarding flow can create payment orders for LinkFox plans.

Mitigation: Require explicit user confirmation of plan and payment method before creating an order, and surface payment status without automatically retrying purchases.

Risk: The skill writes API responses and session metadata to local linkfox directories.

Mitigation: Use protected workspaces, restrict sharing of generated data files, and exclude linkfox output directories from version control when they may contain commerce or account data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-selection-and-shoppable-video)
- [TikTok product-selection and shoppable-video skill guide](SKILL.md)
- [EchoTik new-product ranking reference](references/linkfox-echotik-list-new-product-rank.md)
- [EchoTik product search reference](references/linkfox-echotik-list-product.md)
- [EchoTik product detail reference](references/linkfox-echotik-batch-product-detail.md)
- [EchoTik promotional-video reference](references/linkfox-echotik-product-video.md)
- [EchoTik video download URL reference](references/linkfox-echotik-get-video-download-url.md)
- [FastMoss top-selling ranking reference](references/linkfox-fastmoss-product-rank-top-selling.md)
- [FastMoss product search reference](references/linkfox-fastmoss-product-search.md)
- [TikTok video authorization reference](references/linkfox-tiktok-video-auth.md)
- [TikTok shoppable-video API reference](references/linkfox-tiktok-video.md)
- [TikTok shoppable-video products reference](references/linkfox-tiktok-video-products.md)
- [Large-file upload reference](references/large-file-upload.md)
- [Onboarding reference](references/onboarding.md)
- [TikTok Shop shoppable-video large-file upload documentation](https://partner.tiktokshop.com/docv2/page/shoppable-video-large-file-upload)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands and JSON response summaries; full API responses are saved as JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large API responses are summarized for display and persisted under a local linkfox session directory for follow-up extraction.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
