## Description:

引导初高中学生通过画物理图景、建立模型、列式计算和检验反思，逐步解决具体物理题目。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking middle and high school students use this skill to work through a specific physics problem with step-by-step questions and diagram guidance. It can optionally coordinate learning records and review reminders after explicit consent.

### Deployment Geography for Use:

Global (Chinese-language K12 tutoring)

## Known Risks and Mitigations:

Risk: Optional memory, wrong-answer logging and reminders can share a student's learning records with other skills.

Mitigation: Keep these features off by default; obtain the student's and, when required, guardian's consent before enabling each one.

Risk: An unclear problem image may lead to incorrect physics guidance.

Mitigation: Ask for the known quantities and question in text and confirm the problem statement rather than guessing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Four-step physics problem-solving guide](references/physics-4step-statemachine.md)
- [Physics diagram guide](references/physics-diagram-guide.md)
- [Socratic questioning guide](references/physics-socrates-guide.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stepwise hints, diagram prompts, calculations and checks; optional handoffs for wrong-answer logging or reminders with consent.]

## Skill Version(s):

2.11.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
