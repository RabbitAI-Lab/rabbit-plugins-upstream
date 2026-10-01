## Description:

Helps create, size, animate, and check emoji stickers for WeChat, Xiaohongshu, and Douyin publishing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Creators and developers use this skill to prepare Chinese-platform sticker sets, resize or animate images, check submission assets and copy, and assemble publishing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fetched platform rules may be outdated or incorrect.

Mitigation: Review the proposed rule changes and source differences before approving updates.

Risk: Offline prohibited-word checks may miss current platform restrictions.

Mitigation: Treat offline results as a fallback and verify against current platform rules or a live word-check service before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bonniegeng-max/skills/emoji-sticker-cn)
- [WeChat sticker production specifications](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html#/makingSpecifications#specifications_stickers)
- [WeChat sticker review standards](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html#/auditingStandards#auditingStandards_demand)
- [Chinese-platform sticker size reference](artifact/references/中文平台表情包尺寸规范.md)
- [Chinese-platform copy compliance reference](artifact/references/中文平台违禁词合规参考.md)

## Skill Output:

**Output Type(s):** [Markdown, Image files, Shell commands, Guidance]

**Output Format:** [Markdown guidance and submission checklists; PNG or GIF sticker assets and optional ZIP packages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes asset and copy checks; image generation and live word checks depend on available host tools.]

## Skill Version(s):

3.1.5 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
