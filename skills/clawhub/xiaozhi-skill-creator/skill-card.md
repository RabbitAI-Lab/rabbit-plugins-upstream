## Description:

写一个新 SKILL 时用的编写工具：四层结构（角色/规则/记忆/输出）、安全与隐私边界、五步落地流程、常见问题诊断。面向 SKILL 开发者与有编程/写提示词基础的高中生，在‘我要新写一个学习类 SKILL’‘帮我把这个 SKILL 的规则写清楚’‘我的 SKILL 行为不稳定怎么排查’‘这个 SKILL 该记哪些字段’时使用。它不替你写具体学科内容、不做学习辅导、不生成练习题；本仓库的词表与阈值一律以 shared/vocab.md 为准。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

SKILL 开发者和具备编程或提示词基础的高中生可用它规划、编写和排查学习类 SKILL，明确角色、规则、记忆、输出以及安全与隐私边界。

### Deployment Geography for Use:

China (mainland; the included educational conventions target Chinese K–12 use)

## Known Risks and Mitigations:

Risk: Examples used while drafting skills could expose student information.

Mitigation: Use anonymized examples.

Risk: Generated skills that store student data may be deployed before their security and data controls are complete.

Mitigation: Before deployment, complete the security baseline and schemas, and verify consent and deletion controls.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-creator)
- [Skill templates library](references/skill-templates-library.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [Markdown guidance and templates, with JSON Schema examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-first authoring guidance; no automatic execution.]

## Skill Version(s):

2.12.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
