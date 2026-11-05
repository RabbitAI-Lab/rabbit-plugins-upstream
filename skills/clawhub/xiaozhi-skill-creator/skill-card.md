## Description:

写一个新 SKILL 时用的编写工具：四层结构（角色/规则/记忆/输出）、安全与隐私边界、五步落地流程、常见问题诊断。面向 SKILL 开发者与有编程/写提示词基础的高中生，在"我要新写一个学习类 SKILL""帮我把这个 SKILL 的规则写清楚""我的 SKILL 行为不稳定怎么排查""这个 SKILL 该记哪些字段"时使用。它不替你写具体学科内容、不做学习辅导、不生成练习题；本仓库的词表与阈值一律以 shared/vocab.md 为准。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

SKILL 开发者和具备编程或提示词基础的高中生可用它来设计、编写或排查学习类 SKILL 的结构、规则、安全边界、记忆字段和输出格式。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated templates may be incomplete for student deployment while the security baseline and profile-field definitions are missing.

Mitigation: Complete the missing baseline and profile definitions before deploying templates to students, and review each generated skill's permissions separately.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-creator)
- [SKILL 提示词模板库](artifact/references/skill-templates-library.md)
- [DNA profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)
- [Handover protocol schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Markdown guidance, reusable SKILL prompt templates, and checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces text specifications and templates; no runtime actions.]

## Skill Version(s):

2.12.5 (source: server-resolved release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
