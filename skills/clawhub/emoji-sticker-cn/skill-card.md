## Description:

Emoji Sticker CN helps agents prepare Chinese-platform emoji and sticker assets by applying platform size rules, copy compliance checks, resizing and packaging workflows, and simple animated GIF generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and publishing teams use this skill to resize, name, package, animate, and pre-check sticker assets for WeChat sticker submissions and inline use on Chinese social platforms. It also guides agents through rule review workflows for platform specification changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Advertised asset inspection and submission helper commands are not present in the artifact, which can overstate final publication readiness.

Mitigation: Before publication, independently verify generated assets against the target platform requirements and do not treat absent helper commands as available.

Risk: The local prohibited-terms checker is an offline fallback and may miss current platform enforcement changes.

Mitigation: Use real-time platform or word-checking review where available, and perform a final manual review before public release.

Risk: Platform size, format, and policy rules can change, and some referenced entries are marked for verification rather than active use.

Mitigation: Use only active, officially verified reference entries and confirm pending or changed rules with the relevant platform before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/emoji-sticker-cn)
- [Chinese platform sticker size specification reference](artifact/references/中文平台表情包尺寸规范.md)
- [Chinese platform prohibited terms compliance reference](artifact/references/中文平台违禁词合规参考.md)
- [Animation matching rules](artifact/references/动效匹配规则.md)
- [WeChat Sticker Open Platform guide](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html)
- [WeChat public platform operating specification](https://fuwu.weixin.qq.com/community/develop/article/doc/000a46f78684f8b21d903690460013)
- [Douyin community rules](https://www.douyin.com/rule/policy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, files, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, generated image files, ZIP archives, GIF files, and plain-text compliance findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on Pillow and on host-provided image generation or real-time word-checking tools; local compliance checking is an offline fallback.]

## Skill Version(s):

3.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
