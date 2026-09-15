## Description:

中文平台(微信表情开放平台 / 小红书 / 抖音)合规表情包生成助手。提供平台尺寸硬约束裁切与命名、违禁词校验(实时 API + 离线兜底)、静态贴纸转内容匹配动效 GIF、合规参考数据维护与平台规范规则巡检工作流。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External creators, designers, and developers use this skill to prepare Chinese-platform sticker packs for WeChat sticker submission or Xiaohongshu and Douyin inline use. It guides prompt posture selection, platform sizing, naming, ZIP packaging, GIF animation, and copy compliance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned installs or unreviewed rule updates can change compliance guidance unexpectedly.

Mitigation: Install pinned, trusted releases where possible and review rule-update diffs before confirming writes.

Risk: Very large or untrusted images and GIFs can consume significant CPU or memory in the media scripts.

Mitigation: Process only trusted or size-limited media inputs and apply size limits before batch resizing or animation.

Risk: Offline word-list checks may miss current platform policy changes.

Mitigation: Use the realtime multi-wordcheck workflow when available and treat the bundled offline checker as a fallback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/emoji-sticker-cn)
- [中文平台表情包尺寸规范参考](references/中文平台表情包尺寸规范.md)
- [中文平台违禁词合规参考](references/中文平台违禁词合规参考.md)
- [动效匹配规则](references/动效匹配规则.md)
- [静态姿势动作库](references/静态姿势动作库.md)
- [微信表情开放平台指南](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html)
- [飞书企业表情贴图帮助中心](https://feishu.cn/hc/zh-CN/articles/360049068046)
- [QQ 表情设计规则](https://yuanchuang.qq.com/html/design_rule.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and generated image, GIF, ZIP, or checklist files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Python/Pillow scripts for resizing, GIF animation, ZIP packaging, and offline compliance checks; generated media and copy should be checked against current platform rules before publication.]

## Skill Version(s):

3.1.1 (source: server release metadata; artifact frontmatter reports 3.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
