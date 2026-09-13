## Description:

中文平台(微信表情开放平台 / 小红书 / 抖音)合规表情包生成助手。提供平台尺寸硬约束裁切与命名、违禁词校验(实时 API + 离线兜底)、静态贴纸转内容匹配动效 GIF、合规参考数据维护与平台规范规则巡检工作流。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External creators and developers use this skill to prepare Chinese-platform sticker packs for WeChat, Xiaohongshu, and Douyin by generating platform-aware prompts, resizing assets, checking copy for prohibited terms, and producing GIF animations when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Realtime prohibited-term checking can send unpublished or confidential copy to an external checker.

Mitigation: Use the local offline checker for sensitive drafts, or only use the realtime checker when its operator and data handling are trusted.

Risk: Installer and Pillow dependency commands are not pinned in the release guidance.

Mitigation: Pin the installer and Pillow versions in controlled deployments, and scan the installed artifact before use.

Risk: The offline prohibited-term checker is a fallback and may miss current platform-specific rules.

Mitigation: Run realtime compliance checks or human review before publishing, especially for commercial copy, platform descriptions, and search terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/emoji-sticker-cn)
- [Chinese platform sticker size reference](references/中文平台表情包尺寸规范.md)
- [Chinese platform prohibited-terms compliance reference](references/中文平台违禁词合规参考.md)
- [Animation matching rules](references/动效匹配规则.md)
- [Static pose action library](references/静态姿势动作库.md)
- [WeChat sticker open platform guide](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html)
- [WeChat public platform operations specification](https://fuwu.weixin.qq.com/community/develop/article/doc/000a46f78684f8b21d903690460013)
- [AI-generated content labeling measures reference](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated sticker asset files such as PNG, GIF, and ZIP outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local Python scripts for resizing, GIF animation, and offline copy checks; realtime prohibited-term checking may depend on an external checker when available.]

## Skill Version(s):

3.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
