## Description:

Helps creators prepare Chinese-platform emoji stickers with platform-sized assets, animated GIFs, content checks, and submission guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Sticker creators and developers use this skill to prepare images, animations, captions, and submission materials for WeChat, Xiaohongshu, and Douyin.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Platform requirements can change between releases.

Mitigation: Review the proposed rule changes and their sources before confirming updates; check current platform requirements before submission.

Risk: Offline content checks may miss prohibited language.

Mitigation: Use live checks when available and clearly identify offline checks as a limited fallback.

Risk: Optional image generation can use paid credits.

Mitigation: Confirm the image count and expected cost with the user before generating a batch.

Risk: An unreviewed install could include changes to platform rules.

Mitigation: Prefer a pinned, reviewed release and inspect rule-update differences before allowing writes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bonniegeng-max/skills/emoji-sticker-cn)
- [WeChat Sticker Platform specifications](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html#/makingSpecifications#specifications_stickers)
- [Chinese-platform sticker sizes](references/中文平台表情包尺寸规范.md)
- [Chinese-platform content checks](references/中文平台违禁词合规参考.md)
- [WeChat sticker review guidance](references/微信表情审核标准与高频拒因.md)
- [Animation matching rules](references/动效匹配规则.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Image files]

**Output Format:** [Markdown guidance and generated PNG, GIF, and ZIP assets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional submission checklist and asset-check results; image generation requires a host tool or user-provided images.]

## Skill Version(s):

3.1.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
