## Description: <br>
TikTok product-selection and shoppable-video toolkit that integrates EchoTik and FastMoss commerce data with TikTok shoppable-video APIs for product research, trend analysis, promotional-video analysis, and shoppable-video publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, e-commerce operators, marketers, and developers use this skill to research TikTok Shop products, compare sales and GMV signals, inspect promotional videos, manage creator authorization, and prepare or publish shoppable videos through the supported TikTok video workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can call external LinkFox, EchoTik, FastMoss, and TikTok-related services using configured credentials. <br>
Mitigation: Use only trusted gateway settings and scoped API credentials, and avoid running the skill in workspaces where commerce or account data should not be retained. <br>
Risk: The skill can save full API responses locally, including commerce, account, or token-adjacent workflow data. <br>
Mitigation: Review saved response paths, restrict workspace access, and remove retained response files when they are no longer needed. <br>
Risk: Some product-research calls may consume paid API credits or quota. <br>
Mitigation: Require explicit user confirmation before paid calls, repeated pagination, changed search parameters, or retries after empty results. <br>
Risk: The TikTok workflow can prepare and publish public shoppable videos. <br>
Mitigation: Require explicit confirmation before posting, verify the selected account, product_id, video file, title, and precheck status, and mask access or refresh tokens in user-facing output. <br>


## Reference(s): <br>
- [Skill source](artifact/SKILL.md) <br>
- [EchoTik TikTok new product ranking](artifact/references/linkfox-echotik-list-new-product-rank.md) <br>
- [EchoTik TikTok product search](artifact/references/linkfox-echotik-list-product.md) <br>
- [EchoTik TikTok batch product detail](artifact/references/linkfox-echotik-batch-product-detail.md) <br>
- [EchoTik TikTok product video](artifact/references/linkfox-echotik-product-video.md) <br>
- [EchoTik TikTok video download URL](artifact/references/linkfox-echotik-get-video-download-url.md) <br>
- [FastMoss TikTok top-selling ranking](artifact/references/linkfox-fastmoss-product-rank-top-selling.md) <br>
- [FastMoss TikTok product search](artifact/references/linkfox-fastmoss-product-search.md) <br>
- [TikTok video authorization and token management](artifact/references/linkfox-tiktok-video-auth.md) <br>
- [TikTok shoppable-video products](artifact/references/linkfox-tiktok-video-products.md) <br>
- [TikTok shoppable-video API workflow](artifact/references/linkfox-tiktok-video.md) <br>
- [Shoppable video large-file upload](artifact/references/large-file-upload.md) <br>
- [TikTok Shop Partner Center large-file upload documentation](https://partner.tiktokshop.com/docv2/page/shoppable-video-large-file-upload) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, code] <br>
**Output Format:** [Markdown guidance with JSON parameters, shell commands, and saved JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts can save full API responses under the workspace linkfox data directory and may print summaries for large responses.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata; artifact frontmatter reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
