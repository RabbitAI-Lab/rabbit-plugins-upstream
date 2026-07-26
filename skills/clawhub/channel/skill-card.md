## Description: <br>
WeChat Official Account Draft Box management tool for creating and managing graphic draft articles through the WeChat API with text, image, summary extraction, listing, publishing, and deletion support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manifoldor](https://clawhub.ai/user/manifoldor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, editors, and operators use this skill to prepare, inspect, publish, and remove WeChat Official Account draft articles from a command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing or deleting a draft can affect a live WeChat Official Account workflow. <br>
Mitigation: Review media IDs and article content before running publish or delete commands. <br>
Risk: WeChat AppSecret and cached access tokens grant account API access if exposed. <br>
Mitigation: Protect WECHAT_APPSECRET and ~/.config/channel/access_token.json, and rotate credentials if they are shared or leaked. <br>
Risk: Uploaded article and image files are sent to WeChat services. <br>
Mitigation: Only pass article and image files that are approved for upload to the target WeChat Official Account. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/manifoldor/skills/channel) <br>
- [WeChat Official Account Documentation](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html) <br>
- [WeChat Draft Box API Reference](references/wechat_api.md) <br>
- [WeChat Public Platform](https://mp.weixin.qq.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance and command-line output for WeChat draft operations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses WECHAT_APPID and WECHAT_APPSECRET environment variables and may cache access tokens under ~/.config/channel.] <br>

## Skill Version(s): <br>
1.0.6 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
