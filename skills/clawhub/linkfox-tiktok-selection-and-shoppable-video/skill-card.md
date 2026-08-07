## Description:

TikTok 选品与带货视频一站式 AI 工具集，整合 EchoTik/FastMoss 选品数据与 TikTok 官方带货视频 API，覆盖 TikTok Shop 选品、爆品趋势、带货视频分析与可购物视频发布。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, creators, and agent workflows use this skill to research TikTok Shop products, compare EchoTik and FastMoss trend data, inspect promotional video performance, authorize TikTok creator accounts, and publish shoppable videos through the supported LinkFox and TikTok API flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox API keys and TikTok creator authorization tokens.

Mitigation: Install only when this credential access is acceptable, avoid exposing full tokens, and protect or remove local response and cache files that may contain sensitive business data.

Risk: The skill can perform user-directed TikTok shoppable-video publishing and LinkFox billing or order-related flows.

Mitigation: Review commands and parameters before posting videos or starting chargeable API calls, and require explicit user confirmation for actions that publish content or consume paid credits.

Risk: Changing the LinkFox gateway endpoint could route requests away from the intended service.

Mitigation: Keep LINKFOX_TOOL_GATEWAY pointed only at the legitimate LinkFox gateway before running the scripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-selection-and-shoppable-video)
- [Publisher profile](https://clawhub.ai/user/linkfox-ai)
- [EchoTik product search reference](references/linkfox-echotik-list-product.md)
- [EchoTik new product ranking reference](references/linkfox-echotik-list-new-product-rank.md)
- [FastMoss top-selling product ranking reference](references/linkfox-fastmoss-product-rank-top-selling.md)
- [FastMoss product search reference](references/linkfox-fastmoss-product-search.md)
- [TikTok video authorization reference](references/linkfox-tiktok-video-auth.md)
- [TikTok shoppable video reference](references/linkfox-tiktok-video.md)
- [TikTok shoppable video products reference](references/linkfox-tiktok-video-products.md)
- [Large file upload reference](references/large-file-upload.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON parameters, shell commands, and saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local LinkFox response/cache files and may initiate user-directed API calls for TikTok product research, authorization, uploads, and shoppable-video publishing.]

## Skill Version(s):

1.2.1 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
