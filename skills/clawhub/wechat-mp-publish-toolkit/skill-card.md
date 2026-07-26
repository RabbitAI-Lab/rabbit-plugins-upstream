## Description: <br>
A toolkit for pushing article drafts to a WeChat Official Account draft box, publishing drafts through the WeChat MP API, and setting up scheduled publishing automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yyi162751-collab](https://clawhub.ai/user/yyi162751-collab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, publishers, and automation maintainers use this skill to configure WeChat MP credentials, push article HTML and cover images into drafts, publish selected drafts, and create daily publishing automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use WeChat Official Account secrets to publish or delete official-account content. <br>
Mitigation: Install only when granting the agent this publishing authority is acceptable, and keep the credential file locked down. <br>
Risk: Recurring automation can publish content without built-in confirmation controls. <br>
Mitigation: Prefer manual approval before recurring auto-publish runs and verify every media_id before publishing. <br>
Risk: The delete helper can remove a draft if given the wrong media_id. <br>
Mitigation: Avoid using the delete helper unless the target draft has been confirmed. <br>


## Reference(s): <br>
- [WeChat MP API Guide](references/api-guide.md) <br>
- [Daily Auto-Publish Automation Template](references/automation-template.md) <br>
- [WeChat Official Account Platform](https://mp.weixin.qq.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/yyi162751-collab/skills/wechat-mp-publish-toolkit) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands, Python command examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce WeChat API response identifiers such as media_id and publish_id; requires user-supplied credential paths and draft identifiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
