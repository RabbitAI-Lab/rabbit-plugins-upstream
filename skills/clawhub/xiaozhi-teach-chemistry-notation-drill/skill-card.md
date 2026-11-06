## Description:

帮助化学教师按教学进度设计分级化学用语过关训练，并安排间隔回看与分层跟进。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

化学教师用它为初高中班级规划元素符号、化合价、化学式与化学方程式的分级训练，制作分层过关卡并安排补救回看。生成的题目和面向学生的材料由教师核验后再用于课堂或作业。

### Deployment Geography for Use:

China (Mainland)

## Known Risks and Mitigations:

Risk: Student identifiers or confidential exam material may be included in the information used to prepare drills.

Mitigation: Use student aliases or seat numbers and exclude confidential exam material.

Risk: Generated chemistry questions may contain errors.

Mitigation: Verify generated questions before classroom or homework use.

Risk: Class information may be retained or shared according to platform settings.

Mitigation: Check that the platform honors the intended memory and sharing controls.

## Reference(s):

- [ClawHub release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chemistry-notation-drill)
- [notation-drill-system.md](references/notation-drill-system.md)
- [notation-drill-hs.md](references/notation-drill-hs.md)
- [AI item check](shared/ai-item-check.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration]

**Output Format:** [Chinese prose, tables, and structured class assignment records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed drafts; AI-generated questions require manual chemistry verification before classroom use.]

## Skill Version(s):

2.12.6 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
