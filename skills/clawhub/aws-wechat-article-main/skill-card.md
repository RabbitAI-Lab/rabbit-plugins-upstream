## Description:

编排微信公众号内容从选题、写稿、审稿、排版、配图到发布的完整流程，并路由到配套子 skill 完成内容运营工作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

微信公众号编辑、自媒体运营者和品牌内容团队 use this skill to coordinate a full WeChat article workflow from topic selection through draft, review, formatting, imagery, and draft or publish preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can handle WeChat app credentials and unpublished article content, and the default configuration can route publishing traffic through a third-party proxy.

Mitigation: Keep secrets in aws.env rather than chat, use the official WeChat API unless the proxy is explicitly trusted, and review configuration before using production credentials.

Risk: High-impact publishing behavior depends on companion skills and account configuration.

Mitigation: Review or pin the companion skills used for publishing, keep the default draft flow until final approval, and verify publishing settings before enabling public release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-main)
- [Publisher profile](https://clawhub.ai/user/aiworkskills)
- [AI Work Skills homepage](https://aiworkskills.cn)
- [Repository URL declared in skill metadata](https://github.com/aiworkskills/wechat-article-skills)
- [First-time setup](references/first-time-setup.md)
- [Configuration example](references/config.example.yaml)
- [Article screening schema](references/articlescreening-schema.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, YAML configuration, and generated article files or assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update workspace files such as .aws-article configuration, article.yaml, article.md, article.html, and image assets when used with companion skills.]

## Skill Version(s):

1.0.26 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
