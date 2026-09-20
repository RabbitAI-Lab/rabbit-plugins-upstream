## Description:

Publish Markdown to WeChat Official Account drafts with a self-contained Python toolchain for rich articles and image posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content operators, and technical writers use this skill to convert Markdown articles or image posts into WeChat Official Account drafts, preview rendered output, and upload content through WeChat APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses WeChat Official Account API credentials to upload drafts and images.

Mitigation: Install it only for intended WeChat accounts, keep the credential file private, and rotate credentials if they are exposed.

Risk: Local token and upload caches may persist account-linked access data or media metadata on shared machines.

Mitigation: Protect or delete the local wechat-publisher token and upload cache files when using shared or untrusted systems.

Risk: Rendered drafts may contain sensitive, internal, or unintended content before publication.

Mitigation: Use local render previews where appropriate and review the WeChat draft before sending or group publishing.

Risk: WeChat image and SVG handling constraints can cause broken or rejected draft content.

Mitigation: Follow the documented SVG conversion and image-format guidance, then preview the draft in WeChat before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dqsjqian/skills/wechat-publisher)
- [Theme reference](artifact/references/themes.md)
- [Troubleshooting guide](artifact/references/troubleshooting.md)
- [WeChat draft/add API documentation](https://developers.weixin.qq.com/doc/subscription/api/draftbox/draftmanage/api_draft_add.html)
- [WeChat permanent asset API documentation](https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/Adding_Permanent_Assets.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated HTML or WeChat draft content when commands are executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local preview HTML, local token and upload caches, and WeChat draft entries during execution.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
