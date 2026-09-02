## Description:

Emoji Gh Check helps agents create and prepare Chinese-platform emoji and sticker packs by guiding image generation, resizing and cropping assets, checking platform dimensions and sensitive words, producing upload metadata, and creating simple animated GIF effects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT

## Use Case:

Developers, creators, and content teams use this skill to prepare sticker packs for Chinese platforms such as WeChat, Xiaohongshu, and Douyin. It supports platform-specific asset sizing, local preflight checks, sensitive-word screening, upload checklists, and lightweight GIF animation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes local images and text and can create generated sticker assets, GIFs, ZIP packages, reports, and upload checklists.

Mitigation: Run it in a dedicated workspace, review output paths before execution, and inspect generated files before publishing or uploading.

Risk: Online compliance checking may send sticker copy to an external checker.

Mitigation: Use online checking only for text that is appropriate to share externally; otherwise use the offline fallback and treat its results as limited preflight guidance.

Risk: Platform rules and sensitive-word policies can change after the bundled references were captured.

Mitigation: Before publishing, verify active official references or run the rule-inspection workflow and apply updates only after explicit confirmation.

Risk: Automated asset and text checks do not fully cover rights, likeness, originality, restricted subjects, or final platform reviewer judgment.

Mitigation: Use the local checks as preflight gates and add human review for IP rights, portrait authorization, content suitability, and platform-specific submission requirements.

## Reference(s):

- [Chinese Platform Sticker Size Reference](references/中文平台表情包尺寸规范.md)
- [Chinese Platform Sensitive-Word Compliance Reference](references/中文平台违禁词合规参考.md)
- [WeChat Sticker Review Standards and Common Rejection Reasons](references/微信表情审核标准与高频拒因.md)
- [Animation Matching Rules](references/动效匹配规则.md)
- [WeChat Sticker Making Specifications](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html#/makingSpecifications)
- [WeChat Sticker Auditing Standards](https://sticker.weixin.qq.com/cgi-bin/mmemoticon-bin/readtemplate?t=guide/index.html#/auditingStandards)
- [Feishu Custom Sticker Help Center](https://feishu.cn/hc/zh-CN/articles/360049068046)
- [WeChat Public Platform Operating Specification](https://fuwu.weixin.qq.com/community/develop/article/doc/000a46f78684f8b21d903690460013)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, generated local files, ZIP packages, JSON reports, and upload checklists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local sticker image files, animated GIFs, ZIP archives, compliance reports, and submit.md upload checklists.]

## Skill Version(s):

3.0.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
