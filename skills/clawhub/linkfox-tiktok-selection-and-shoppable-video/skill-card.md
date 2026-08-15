## Description:

One-stop TikTok product-selection and shoppable-video toolkit for EchoTik and FastMoss product research, promotional-video analysis, and TikTok official shoppable-video publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, creators, and developers use this skill to research TikTok Shop products, compare sales and GMV signals, analyze product-linked videos, manage TikTok creator authorization, and prepare or publish shoppable videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys, TikTok OAuth flows, account tokens, and billed API calls.

Mitigation: Install only for trusted LinkFox use, keep credentials scoped, mask tokens in outputs, and confirm user intent before actions that authorize accounts, consume credits, or affect payments.

Risk: Gateway URL override environment variables and helper behavior can broaden where requests go or where responses are written.

Mitigation: Review or restrict LINKFOX_TOOL_GATEWAY and related URL override variables, run the skill in a controlled workspace, and inspect saved response paths before sharing outputs.

Risk: No-watermark video downloads can involve rights-sensitive content.

Mitigation: Only retrieve or use download links when the user has appropriate rights and the action is consistent with platform terms.

## Reference(s):

- [Linkfox Tiktok选品与带货视频](references/linkfox-tiktok-video.md)
- [TikTok Video Authorization](references/linkfox-tiktok-video-auth.md)
- [TikTok Video Products](references/linkfox-tiktok-video-products.md)
- [Large File Upload](references/large-file-upload.md)
- [EchoTik Product Search](references/linkfox-echotik-list-product.md)
- [EchoTik New Product Rank](references/linkfox-echotik-list-new-product-rank.md)
- [EchoTik Product Detail](references/linkfox-echotik-batch-product-detail.md)
- [EchoTik Product Video](references/linkfox-echotik-product-video.md)
- [EchoTik Video Download URL](references/linkfox-echotik-get-video-download-url.md)
- [FastMoss Product Search](references/linkfox-fastmoss-product-search.md)
- [FastMoss Top Selling Product Rank](references/linkfox-fastmoss-product-rank-top-selling.md)
- [Onboarding](references/onboarding.md)
- [TikTok Shop Shoppable Video Large File Upload](https://partner.tiktokshop.com/docv2/page/shoppable-video-large-file-upload)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses or saved response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write full API responses under a local linkfox data directory and print summaries for large responses.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
