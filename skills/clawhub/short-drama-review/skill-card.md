## Description:

审查短剧项目中的原著分析、故事、剧本、视觉设定、图片提示词、分镜、冻结关键帧、视频提示词和已有媒体。用户提出“审稿/检查剧本”“检查资产或连续性”“检查图片/视频提示词”“检查原著分析”“审查模板感”“根据生产观察做项目校准”时使用；只写审查问题、结论和修订要求，不代替负责人修改来源文件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

短剧创作者和审稿人可用此技能审查故事、剧本、资产连续性、提示词、分镜和制作素材，并形成带位置与证据的结论及修订要求。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source-analysis validation relies on a separate companion skill whose rules may affect the review result.

Mitigation: Review the companion validator independently, specify the project files and sections in scope, and state whether a report should be saved.

## Reference(s):

- [ClawHub release: 短剧审查](https://clawhub.ai/worldwonderer/skills/short-drama-review)
- [Review method](artifact/references/review-method.md)
- [Stage contract](artifact/references/stage-contract.md)
- [Source analysis rubric](artifact/references/rubric-source-analysis.md)
- [Story and script rubric](artifact/references/rubric-story-script.md)
- [Assets and prompts rubric](artifact/references/rubric-assets-prompts.md)
- [Visual motion rubric](artifact/references/rubric-visual-motion.md)
- [Generated media review](artifact/references/generated-media.md)
- [Production quality gates](artifact/references/production-quality-gates.md)
- [Project calibration](artifact/references/project-calibration.md)
- [Anti-template review and repair](artifact/references/anti-template-repair.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Evidence-based review findings in Markdown or concise conversational text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies scope, evidence, impact, required revision, responsible skill, severity, and review status; leaves source-file changes to the responsible owner.]

## Skill Version(s):

1.0.8 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
