## Description:

审查短剧项目的原著分析、剧本、资产连续性、分镜、关键帧、提示词和已有媒体，给出有证据的结论与修订要求，不直接修改来源文件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者和制作团队用它审查指定的项目资料，定位剧情、连续性及制作问题，并向相应负责人交付有出处的结论和修订要求。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 审查记录可能泄露私有项目内容、凭据或内部路径。

Mitigation: 仅保留定位问题所需的最小引文，发布前检查并去除敏感信息。

Risk: 缺少关键资料或仅凭文本审查媒体时，结论可能不完整。

Mitigation: 明确标注未核实部分和输入限制，仅对可见证据下结论。

Risk: 审查结论或结构校验可能被误当作内容修订或成片质量保证。

Mitigation: 由负责人员核对并执行修订，必要时复审；结构校验不替代人工内容判断。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/short-drama-review)
- [审查方法](references/review-method.md)
- [故事剧本审查表](references/rubric-story-script.md)
- [视觉运动审查表](references/rubric-visual-motion.md)
- [生产质量门](references/production-quality-gates.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [中文审查结论和证据定位的 Markdown；按需生成结构化 JSON/JSONL 发现记录]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [仅在需要落盘时写审查文件；不修改来源资料或提交媒体任务。]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
