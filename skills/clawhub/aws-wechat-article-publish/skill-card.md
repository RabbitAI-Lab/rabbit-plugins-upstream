## Description:

Publishes prepared WeChat Official Account articles to draft or submission workflows through the WeChat API, with cover upload, pre-publish checks, and draft/published mode controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, automation teams, and developers use this skill to move finalized WeChat Official Account content into the official draft box or submit it for publication. It supports account selection, configuration checks, media upload, and status tracking for prepared article directories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured custom API endpoints can receive WeChat secrets, access tokens, article content, and images.

Mitigation: Keep WECHAT_N_API_BASE and wechat_api_base empty unless intentionally using a trusted HTTPS proxy, and verify the destination before running token, query, upload, full, or publish commands.

Risk: The skill can move content from draft preparation into WeChat publication workflows.

Mitigation: Prefer draft mode first, confirm account and publish_method configuration, and require explicit confirmation before submitting content for publication.

Risk: WeChat credentials are expected in aws.env.

Mitigation: Keep aws.env out of source control and use tightly scoped WeChat credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-publish)
- [Publisher profile](https://clawhub.ai/user/aiworkskills)
- [微信公众号 API 参考](references/api-reference.md)
- [发布脚本用法](references/usage.md)
- [提交到公众号](references/submit-guide.md)
- [发布前检查清单](references/pre-publish-checklist.md)
- [WeChat draft add API](https://developers.weixin.qq.com/doc/subscription/api/draftbox/draftmanage/api_draft_add)
- [WeChat freepublish submit API](https://developers.weixin.qq.com/doc/subscription/api/public/api_freepublish_submit.html)
- [WeChat add permanent material API](https://developers.weixin.qq.com/doc/subscription/api/material/permanent/api_addmaterial.html)
- [WeChat upload article image API](https://developers.weixin.qq.com/doc/subscription/en/api/material/permanent/api_uploadimage)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON/YAML configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue WeChat API calls and update article status files when the user proceeds with publishing.]

## Skill Version(s):

1.0.23 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
