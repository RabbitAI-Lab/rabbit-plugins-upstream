## Description: <br>
Helps agents manage TikTok creator shoppable-video workflows through LinkFox, including creator profile lookup, video precheck, publishing, and publish-status checks for authorized accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External commerce operators and developers use this skill to manage TikTok creator video tasks for authorized accounts, including profile lookup, shoppable-video precheck, posting, and status review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish or check TikTok creator video content through authorized accounts. <br>
Mitigation: Confirm the account, video, product, and publish intent before running post actions. <br>
Risk: API keys and creator access tokens may be present during use. <br>
Mitigation: Do not expose full tokens in prompts, logs, or summaries; prefer account identifiers where supported. <br>
Risk: Saved API responses may contain sensitive business or account data. <br>
Mitigation: Use response persistence only in controlled output directories with appropriate retention. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-tiktok-video) <br>
- [TikTok Video API Reference](references/api.md) <br>
- [Shoppable Video Large File Upload Solution](references/large-file-upload.md) <br>
- [TikTok Partner Center large file upload documentation](https://partner.tiktokshop.com/docv2/page/shoppable-video-large-file-upload) <br>
- [TikTok Partner Center creator profile documentation](https://partner.tiktokshop.com/docv2/page/get-creator-profile-202508) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials and TikTok creator authorization; can post content externally and can optionally save API responses to local files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
