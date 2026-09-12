## Description:

Publishes prepared WeChat Official Account articles to a draft box or submits them for public release through the WeChat API, with checks for credentials, article assets, cover images, and publishing mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operations teams, and developers use this skill to move finalized WeChat article content into the official-account draft workflow or submit it for publication. It supports credential checks, account-slot selection, article metadata preparation, cover and content image handling, and draft or published mode selection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configurable WeChat API endpoint could send WeChat credentials and unpublished article content to an unintended service.

Mitigation: Leave WECHAT_N_API_BASE and config.yaml.wechat_api_base empty unless a trusted HTTPS proxy is intentionally required and reviewed.

Risk: Publication settings can move content from draft creation to direct public submission.

Mitigation: Review publish_method before running publishing commands and use draft mode first when confirming layout or content.

Risk: WeChat AppID, AppSecret, and access tokens may be exposed through local configuration or command output.

Mitigation: Keep aws.env out of source control, limit command logging around token operations, and install only in trusted workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-publish)
- [Publisher profile](https://clawhub.ai/user/aiworkskills)
- [Artifact-declared homepage](https://aiworkskills.cn)
- [Artifact-declared project link](https://github.com/aiworkskills/wechat-article-skills)
- [Usage guide](references/usage.md)
- [Submit guide](references/submit-guide.md)
- [API reference](references/api-reference.md)
- [Pre-publish checklist](references/pre-publish-checklist.md)
- [WeChat draft add API](https://developers.weixin.qq.com/doc/subscription/api/draftbox/draftmanage/api_draft_add)
- [WeChat freepublish submit API](https://developers.weixin.qq.com/doc/subscription/api/public/api_freepublish_submit.html)
- [WeChat permanent material upload API](https://developers.weixin.qq.com/doc/subscription/api/material/permanent/api_addmaterial.html)
- [WeChat content image upload API](https://developers.weixin.qq.com/doc/subscription/en/api/material/permanent/api_uploadimage)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON output from helper commands, and YAML or environment-file configuration updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload article HTML and images to WeChat, create drafts, submit publication jobs, and update article.yaml status fields after successful publishing.]

## Skill Version(s):

1.0.24 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
