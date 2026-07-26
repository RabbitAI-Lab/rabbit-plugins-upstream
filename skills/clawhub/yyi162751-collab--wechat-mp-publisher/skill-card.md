## Description: <br>
WeChat Official Account draft push and auto-publish toolkit for creating article drafts, publishing drafts, setting up scheduled publishing, and handling credential, IP whitelist, and API permission setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yyi162751-collab](https://clawhub.ai/user/yyi162751-collab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to push HTML articles and cover images into a WeChat Official Account draft box, publish selected drafts, or configure scheduled daily publishing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish irreversible WeChat posts using stored account credentials. <br>
Mitigation: Use it only for intended WeChat account operations, protect AppID and AppSecret files, and add confirmation, dry-run, or allowlist controls before scheduled publishing. <br>
Risk: Scheduled automation can broadcast content to all subscribers without a built-in human review step. <br>
Mitigation: Review the target draft media ID and article content before enabling auto-publish, and keep a documented skip or manual-publish path for each scheduled run. <br>
Risk: Credential or token exposure could allow unauthorized draft or publish actions. <br>
Mitigation: Restrict .env file permissions, avoid logging commands or tokens, rotate secrets if exposed, and keep API access limited by WeChat IP whitelisting. <br>


## Reference(s): <br>
- [WeChat MP API Guide](references/api-guide.md) <br>
- [Daily Auto-Publish Automation Template](references/automation-template.md) <br>
- [WeChat Official Account Platform](https://mp.weixin.qq.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/yyi162751-collab/skills/wechat-mp-publisher) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces WeChat API calls, draft media IDs, publish IDs, automation prompts, and status guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
