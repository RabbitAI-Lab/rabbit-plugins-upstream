## Description:

按四步法陪初中至高中学生解决当前化学题，并通过逐级提示引导核验方程式、计算与守恒。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

初中和高中学生可用它逐步解决当前化学题，包括物质推断、反应后溶液成分、物质鉴别和计算。它根据题目条件逐级给提示，并在解题后检查守恒与结果合理性；默认只处理当前会话中的题目。

### Deployment Geography for Use:

中国大陆（按中国课程标准与中考口径设计）

## Known Risks and Mitigations:

Risk: 启用可选学习记录、跨技能档案读取或提醒后，学生信息可能用于当前题目以外的学习功能。

Mitigation: 保持默认的会话内模式；分别启用各项功能前取得学生及适用时监护人的同意，并在分享学生数据前查看相关档案、错题本和提醒技能。

Risk: 化学实验题涉及的操作可能带来安全风险。

Mitigation: 实验操作建议遵守实验安全约定；不要给出在家操作化学实验的步骤。

## Reference(s):

- [ClawHub 发布页](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-problem-coach)
- [四步化学解题指南](artifact/references/chemistry-4step-guide.md)
- [高中必修例题](artifact/references/chemistry-hs2-worked-examples.md)
- [高中选择性必修例题](artifact/references/chemistry-hs3-worked-examples.md)
- [实验安全约定](artifact/shared/lab-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [中文分步讲解、提示、化学式与计算式]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [默认按当前题目进行辅导；记录、错题交接和提醒须分别获得同意。]

## Skill Version(s):

2.12.6 (source: frontmatter; server release evidence agrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
