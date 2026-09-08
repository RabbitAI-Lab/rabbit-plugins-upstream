## Description:

Helps agents prepare Chinese-platform sticker packs by resizing assets, checking copy against platform-sensitive terms, creating simple animated GIFs, and maintaining platform rule references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and agents use this skill to prepare sticker assets and supporting copy for WeChat Sticker Open Platform, Xiaohongshu, Douyin, and similar Chinese-platform workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Offline prohibited-term checks may miss current platform policy issues and do not guarantee approval.

Mitigation: Prefer the live multi-wordcheck workflow when available, disclose fallback limitations, and review final copy against the target platform before publication.

Risk: Platform sticker rules can change after the packaged references were captured.

Mitigation: Use only active official-verified reference entries, run the rule-update workflow for suspected changes, and review diffs before approving any writes.

Risk: The README advertises helper scripts that are not present in this package.

Mitigation: Rely on the bundled resize, animation, and compliance scripts; manually verify asset packages or add the missing helpers before claiming automated checks or submit-list generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/emoji-sticker-cn)
- [Chinese platform sticker size reference](artifact/references/中文平台表情包尺寸规范.md)
- [Chinese platform prohibited-terms compliance reference](artifact/references/中文平台违禁词合规参考.md)
- [Animation matching rules](artifact/references/动效匹配规则.md)
- [WeChat Sticker Open Platform guide](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html)
- [Feishu sticker help center](https://feishu.cn/hc/zh-CN/articles/360049068046)
- [Douyin community policy](https://www.douyin.com/rule/policy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, guidance]

**Output Format:** [Markdown guidance with shell commands; helper scripts can produce resized image files, GIFs, and ZIP packages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on local Python and Pillow availability; offline compliance checks are fallback guidance, not a platform approval guarantee.]

## Skill Version(s):

3.0.2 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
