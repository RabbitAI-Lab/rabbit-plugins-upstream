## Description:

This skill helps users create Chinese-platform compliant emoji and sticker packs for WeChat, Xiaohongshu, and Douyin by guiding image generation, platform-specific resizing and cropping, sequential naming, upload metadata, and sensitive-word compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and content operators use this skill to prepare Chinese-platform sticker assets, metadata, and compliance checks for WeChat sticker submission or inline use on Xiaohongshu and Douyin. It is also used to resize existing images, generate simple animated GIF stickers, and inspect maintained platform rule references before updating them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch image processing writes generated files and ZIP archives to a user-selected output directory.

Mitigation: Use a dedicated output directory and review generated filenames before running or sharing batch outputs.

Risk: Platform sticker dimensions, content rules, and prohibited-word expectations can change after the bundled references were authored.

Mitigation: Check reported source URLs and diffs before confirming rule-reference updates, and prefer active official-reference entries over pending or deprecated entries.

Risk: The offline prohibited-word checker is a fallback and may miss current platform-specific violations.

Mitigation: Use realtime multi-wordcheck-style review when available before publication, and treat the offline checker as preliminary screening only.

## Reference(s):

- [Chinese Platform Sticker Size Specification Reference](references/中文平台表情包尺寸规范.md)
- [Chinese Platform Prohibited Word Compliance Reference](references/中文平台违禁词合规参考.md)
- [WeChat Sticker Open Platform Guide](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html)
- [Feishu Enterprise Sticker Help Center](https://feishu.cn/hc/zh-CN/articles/360049068046)
- [WeChat Public Platform Operating Specification](https://fuwu.weixin.qq.com/community/develop/article/doc/000a46f78684f8b21d903690460013)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and local script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide creation of PNG, GIF, WebP, JPG, and ZIP sticker assets when the bundled scripts are run.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
