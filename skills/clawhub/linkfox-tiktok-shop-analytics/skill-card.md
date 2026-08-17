## Description:

TikTok Shop ERP analytics skill that uses LinkFox to call TikTok Shop Analytics Open API endpoints for authorized shops and shop video performance metrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and commerce operators use this skill to retrieve authorized TikTok Shop information and analyze shop video performance metrics such as views, orders, and GMV through LinkFox-managed ERP access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access authorized-shop and shop analytics data through LinkFox.

Mitigation: Install only in environments where this data access is expected, and grant the LinkFox API key only to trusted agent sessions.

Risk: The bundled generic proxy is broader than the video-performance report workflow clearly requires.

Mitigation: Prefer named API scripts, restrict allowed endpoints and methods to required operations, or use a version that removes the generic proxy.

Risk: API credentials are sent to the configured LinkFox gateway.

Mitigation: Validate the gateway host before use and avoid overriding it with an untrusted LINKFOX_TOOL_GATEWAY or TIKTOK_SHOP_API_BASE_URL value.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-analytics)
- [TikTok Shop ERP Analytics API Reference](artifact/references/api.md)
- [Get Video Performances](artifact/references/apis/get_video_performances.md)
- [Get Authorized Shops](artifact/references/apis/get_authorized_shops.md)
- [TikTok Shop Partner Center: Get Video Performances](https://partner.tiktokshop.com/docv2/page/get-video-performances-202403)
- [TikTok Shop Partner Center: Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309)
- [TikTok Shop Seller Authorization Guide](https://partner.tiktokshop.com/docv2/page/678e3a344ddec3030b238fa0)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Guidance, Analysis]

**Output Format:** [JSON API responses and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires linkfox-tiktok-shop-auth, a LinkFox agent API key, openId, and date-range parameters for video performance queries.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
