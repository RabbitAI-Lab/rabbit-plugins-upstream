## Description:

将 Markdown 文章转换为微信公众号支持的 HTML，上传图片，并创建草稿或提交发布。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gaolfun](https://clawhub.ai/user/gaolfun)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and operators use this skill to prepare Markdown articles for WeChat Official Accounts, upload required images, and create drafts or submit publication jobs through the WeChat API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WeChat AppSecret values and cached access tokens may be stored in plaintext workspace files.

Mitigation: Store AppSecret outside shared workspace or memory when possible, restrict file permissions, and rotate secrets if exposed.

Risk: The skill can use WeChat Official Account API authority to submit final public-account publishing actions.

Mitigation: Require explicit manual confirmation before any final publish action and review article content before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gaolfun/skills/wechat-publisher)
- [Publisher profile](https://clawhub.ai/user/gaolfun)
- [微信公众平台](https://mp.weixin.qq.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown with JSON, HTML, and API status snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include access-token status, image URL mappings, thumb media IDs, converted HTML previews, draft media IDs, publish IDs, and troubleshooting guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
