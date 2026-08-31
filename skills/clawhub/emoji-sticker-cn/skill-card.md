## Description:

Helps agents create Chinese-platform compliant emoji and sticker packs for WeChat, Xiaohongshu, and Douyin, including platform-specific resizing, naming, upload metadata, animated GIF generation, and sensitive-word compliance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

External creators, designers, and developers use this skill to prepare sticker packs and related copy for Chinese social platforms. It supports image resizing, animation, package preparation, metadata guidance, and compliance pre-checks before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sticker copy or metadata may miss current platform policy requirements when only the offline compliance checker is used.

Mitigation: Use the real-time multi-wordcheck workflow when available, treat the local checker as a fallback, and review official platform rules before publication.

Risk: Platform size, format, or prohibited-content rules may change after the bundled references were captured.

Mitigation: Follow the rule-inspection workflow, review source URLs and diffs, and only confirm writes when the proposed updates are acceptable.

Risk: Local image processing can create files that still exceed target platform limits or are visually unsuitable for review.

Mitigation: Inspect generated images and GIFs, check reported file sizes, and rerun resizing or animation options before upload.

## Reference(s):

- [Chinese Platform Sticker Size Specification](references/中文平台表情包尺寸规范.md)
- [Chinese Platform Prohibited Words Compliance Reference](references/中文平台违禁词合规参考.md)
- [Animation Matching Rules](references/动效匹配规则.md)
- [WeChat Sticker Open Platform Guide](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html)
- [Feishu Custom Sticker Help](https://feishu.cn/hc/zh-CN/articles/360049068046)
- [WeChat Official Account Operations Rules](https://fuwu.weixin.qq.com/community/develop/article/doc/000a46f78684f8b21d903690460013)
- [Douyin Community Rules](https://www.douyin.com/rule/policy)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Files]

**Output Format:** [Markdown with inline bash code blocks and local file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce resized sticker images, ZIP packages, animated GIFs, upload metadata guidance, and compliance check results.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
