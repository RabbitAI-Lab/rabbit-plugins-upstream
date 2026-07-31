## Description: <br>
Provides TikTok Shop ERP analytics through LinkFox, mainly retrieving authorized shops and shop video performance data from TikTok Shop Analytics Open API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External TikTok Shop sellers, commerce operators, and developers use this skill to retrieve authorized shops and analyze video performance metrics such as views, orders, and GMV for a selected date range. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generic analytics proxy can reach broader analytics and authorization API paths than the named video performance helpers. <br>
Mitigation: Prefer the named API scripts for routine use, or remove or restrict analytics_proxy.py before deployment. <br>
Risk: The skill can access TikTok Shop ERP data through LinkFox credentials and a seller openId. <br>
Mitigation: Protect LINKFOX_AGENT_API_KEY, use least-privileged runtime access, and run only in trusted agent environments. <br>
Risk: Video performance requests depend on the companion auth skill and correct shop selection. <br>
Mitigation: Verify linkfox-tiktok-shop-auth first, and pass an explicit shop_cipher or shop_id when multiple shops are authorized. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-shop-analytics) <br>
- [TikTok Shop ERP Analytics API Reference](references/api.md) <br>
- [Get Authorized Shops](references/apis/get_authorized_shops.md) <br>
- [Get Video Performances](references/apis/get_video_performances.md) <br>
- [TikTok Shop Get Authorized Shops](https://partner.tiktokshop.com/docv2/page/get-authorized-shops-202309) <br>
- [TikTok Shop Get Video Performances](https://partner.tiktokshop.com/docv2/page/get-video-performances-202403) <br>
- [TikTok Shop seller authorization guide](https://partner.tiktokshop.com/docv2/page/678e3a344ddec3030b238fa0) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials, an openId from linkfox-tiktok-shop-auth, and start_date/end_date for video performance requests.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
