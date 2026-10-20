## Description:

面向中国初高中学生，通过逐步绘制遗传图解、确定基因组成和核对概率，辅导遗传题推理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

中国初高中学生用它逐步分析遗传性状、家系图和遗传概率，按学习阶段理解遗传规律。它提供教学指导，而非个人遗传病诊断。

### Deployment Geography for Use:

China (Chinese K–12 curriculum; localize before use elsewhere)

## Known Risks and Mitigations:

Risk: Sensitive learner profile data could be shared or retained without appropriate consent.

Mitigation: Keep the platform's consent gates enabled and require the student's permission before profile access, recording mistakes, or scheduling reminders.

Risk: Chinese curriculum, crisis contacts, and minor-consent practices may not apply elsewhere.

Mitigation: Use in the intended Chinese K–12 setting, or localize those rules and contacts before deployment.

Risk: A textbook genetics exercise could be mistaken for personal medical risk advice.

Mitigation: Do not assess an individual's inherited-disease risk; refer personal medical questions to a clinician.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-biology-genetics-coach)
- [Genetics reasoning reference](references/genetics-reasoning.md)
- [High-school genetics, expression, and variation reference](references/genetics-hs-expression-variation.md)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Conversational text with stepwise genetics diagrams and calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hints precede worked answers; learner-record and reminder handoffs require consent.]

## Skill Version(s):

2.11.2 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
