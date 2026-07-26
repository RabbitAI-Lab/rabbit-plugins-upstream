## Description: <br>
Manages TikTok creator and video-account OAuth authorization, authorized-account listing, token lookup, and access-token refresh through LinkFox's /tiktokVideo APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and developers use this skill to authorize TikTok creator/video accounts, list authorized accounts, retrieve masked token details, and refresh access tokens before downstream video-upload API workflows. <br>

### Deployment Geography for Use: <br>
Global, with an explicit US region option for authorization flows. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles TikTok creator access and refresh tokens. <br>
Mitigation: Install only when LinkFox is trusted for the authorization flow, avoid exposing full token values, and avoid retaining response files that may contain account or token data. <br>
Risk: The gateway endpoint can be overridden with LINKFOX_TOOL_GATEWAY. <br>
Mitigation: Confirm LINKFOX_TOOL_GATEWAY is unset or points to the expected LinkFox host before running authorization or token scripts. <br>
Risk: The security guidance flags automatic feedback and onboarding-download behavior as review points. <br>
Mitigation: Review or disable automatic feedback and onboarding-download behavior if user context or installation actions should not be sent through LinkFox services. <br>


## Reference(s): <br>
- [TikTok 视频上传 API — 授权与令牌管理 API Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-video-auth) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Token values are intended to be masked in user-facing output; response files may persist API data when response_io.py is used.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
