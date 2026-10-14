## Description:

Creates and reviews Simplified Chinese WeChat public-account articles in Markdown and converts them into publish-ready HTML, a copy page, and a draft API request with static checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aladooo](https://clawhub.ai/user/aladooo)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-language writers and publishing teams use this skill to draft, format, and check WeChat public-account articles before copying them into the editor or preparing a draft API request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional parity check executes a supplied HTML template, and an explicit opt-in can fetch a remote template.

Mitigation: Use only trusted templates and leave OIMD_REMOTE_TEMPLATE disabled unless the remote template is intentionally trusted.

Risk: A copy page generated from untrusted Markdown may contain content that should not be opened or shared without review.

Mitigation: Review generated copy pages before opening or sharing them when the source Markdown is untrusted.

Risk: Skipping checks can leave formatting problems in publishing output.

Mitigation: Avoid --no-check for real publishing output and review reported issues before publishing.

## Reference(s):

- [Orangeink on ClawHub](https://clawhub.ai/aladooo/skills/orangeink)
- [Orangeink writing guide](references/writing-guide.md)
- [WeChat formatting rules](references/wechat-rules.md)
- [WeChat draft API notes](references/wechat-api.md)
- [WeChat article structure specification](https://developers.weixin.qq.com/doc/subscription/guide/product/plugin_spec.html)
- [WeChat draft API documentation](https://developers.weixin.qq.com/doc/service/api/draftbox/draftmanage/api_draft_add.html)

## Skill Output:

**Output Type(s):** [Markdown, HTML, JSON, Guidance]

**Output Format:** [Simplified Chinese Markdown articles or review guidance; HTML fragments and copy pages; JSON draft requests and check reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes static formatting checks and an image list when rendering.]

## Skill Version(s):

1.2.7 (source: skill frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
