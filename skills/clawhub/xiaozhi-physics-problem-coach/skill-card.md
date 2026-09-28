## Description:

面向初中至高一学生的中文物理解题教练，通过画图、建模、计算和检验四步引导学生完成当前题目。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

中文 K12 学生可就具体物理题接受分步追问，练习建立物理图景、选择模型、列式计算和检查答案；高中内容目前覆盖高一必修第一册。

### Deployment Geography for Use:

China (mainland); other regions require localized curriculum, student-data consent practices, and crisis resources.

## Known Risks and Mitigations:

Risk: Optional record lookup, wrong-answer archiving, cross-skill sharing, and reminders may handle student information.

Mitigation: Leave these features off by default and enable each only after explicit student and, where required, guardian consent.

Risk: Tutoring guidance designed for Chinese K12 students may not fit other curricula or regions.

Mitigation: Deploy in the intended Chinese K12 context; localize curriculum, consent practices, and crisis resources before use elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach)
- [Four-step physics problem-solving guide](references/physics-4step-statemachine.md)
- [Physics diagram guide](references/physics-diagram-guide.md)
- [Socratic questioning guide](references/physics-socrates-guide.md)
- [Grade 10 worked examples](references/physics-hs1-worked-examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese conversational text or Markdown with step-by-step prompts and optional text diagrams]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional wrong-answer handoff and review reminders require separate explicit consent; no persistent records or reminders by default.]

## Skill Version(s):

2.7.1 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
