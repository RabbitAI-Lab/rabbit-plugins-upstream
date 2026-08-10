## Description:

TikTok Shop ERP analytics skill that uses the LinkFox gateway to retrieve shop video performance metrics, including views, sales, and GMV, through the TikTok Shop Analytics Open API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agents use this skill to query TikTok Shop ERP analytics for authorized shops and summarize shop video performance over a requested date range.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access TikTok Shop ERP data through openId-backed credentials and the LinkFox gateway.

Mitigation: Install and use it only when the user trusts the LinkFox gateway and explicitly wants the agent to access TikTok Shop ERP analytics data.

Risk: The release exposes a broad credentialed proxy and authorized-shop lookup beyond the narrow video-performance workflow.

Mitigation: Prefer a version that disables the broad analytics proxy, limits allowed paths and methods to documented analytics endpoints, and requires explicit user intent before listing authorized shops.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-analytics)
- [TikTok Shop ERP Analytics API Reference](references/api.md)
- [Get Video Performances](references/apis/get_video_performances.md)
- [Get Authorized Shops](references/apis/get_authorized_shops.md)
- [TikTok Shop Partner Center: Get Video Performances](https://partner.tiktokshop.com/docv2/page/get-video-performances-202403)
- [TikTok Shop Partner Center: Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires openId-backed TikTok Shop ERP authorization through linkfox-tiktok-shop-auth; date ranges use YYYYMMDD.]

## Skill Version(s):

1.0.1 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
