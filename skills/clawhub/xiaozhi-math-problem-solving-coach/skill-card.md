## Description:

通过循序追问和分级提示，帮助初高中学生理解数学题、练习同类题并进行考前梳理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

初高中学生用它梳理单道数学题的解题思路、完成同类练习，并在考前复习相关知识；默认仅使用当前会话的信息。

### Deployment Geography for Use:

Chinese-language K–12 tutoring settings, with locally appropriate guardian and crisis-response safeguards

## Known Risks and Mitigations:

Risk: Student learning records or reminders could be enabled without appropriate consent or guardian safeguards.

Mitigation: Keep the default session-only; enable records and reminders only after explicit consent and platform-enforced guardian rules.

Risk: Student information could be shared across skills beyond the student's permission.

Mitigation: Enforce cross-skill sharing limits and honor student controls before passing learning information to other skills.

Risk: Crisis guidance could give a student an inappropriate regional contact.

Mitigation: Use locally appropriate crisis contacts and confirm the student's region before suggesting a specific number.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [分级提示规范](artifact/shared/hint-ladder.md)
- [四步拍照法](artifact/references/photo-4step-statemachine.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text with stepwise hints and practice questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Student records, cross-skill sharing and reminders require explicit consent in the current conversation.]

## Skill Version(s):

2.10.0 (source: ClawHub release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
