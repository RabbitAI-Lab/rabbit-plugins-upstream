## Description:

面向初高中学生的中文数学解题教练，通过追问和逐级提示帮助学生梳理解题思路、订正单题并练习同类题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

初高中学生用它讨论卡住或做错的数学题，通过追问、分级提示和同类练习找回思路；也可在考前梳理知识点。

### Deployment Geography for Use:

Global (Chinese-language tutoring)

## Known Risks and Mitigations:

Risk: Optional student profiles, cross-skill or parent sharing, and reminders may expose minors' learning data without effective consent controls.

Mitigation: Before enabling these features, verify consent gates, deletion and export controls, and session-only handling of temporary diagnostic fields on the host platform.

Risk: A student in crisis may need support beyond math tutoring.

Mitigation: Follow the skill's crisis referral protocol and direct the student to a trusted adult or appropriate local help instead of continuing the lesson.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [Hint ladder](shared/hint-ladder.md)
- [Math Socratic tutoring guide](references/math-socrates-guide.md)
- [Photo-based problem-solving workflow](references/photo-4step-statemachine.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text with mathematical notation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stepwise hints, questions and optional similar problems; no profile or reminders by default.]

## Skill Version(s):

2.9.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
