## Description:

面向初高中学生的数学解题教练，通过逐级提示、追问和同类题练习帮助学生理解题目，也支持考前梳理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Secondary-school students use the skill to work through individual math problems, understand mistakes, practice with similar questions, and review material before an exam. It guides students with questions and graduated hints before giving a worked solution.

### Deployment Geography for Use:

China (mainland curriculum context)

## Known Risks and Mitigations:

Risk: Enabling saved records, sharing, or reminders may expose student information or exceed expected consent.

Mitigation: Keep these features off by default, require the student's explicit current-turn consent, and review companion skill and platform storage controls before enabling them.

Risk: A crisis referral may conflict with ordinary sharing preferences, and notifying a potentially abusive family member could increase danger.

Mitigation: Follow the crisis exception and referral protocol, use locally appropriate help contacts, and avoid involving a person who may be causing harm.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach)
- [Hint ladder](shared/hint-ladder.md)
- [Generated-item checks](shared/ai-item-check.md)
- [Four-step problem-solving workflow](references/photo-4step-statemachine.md)
- [Socratic questioning guide](references/math-socrates-guide.md)
- [High-school worked examples: first-year topics](references/math-hs1-worked-examples.md)
- [High-school worked examples: core topics](references/math-hs2-worked-examples.md)
- [High-school worked examples: electives](references/math-hs3-worked-examples.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Mathematical explanations, Practice questions]

**Output Format:** [Chinese conversational text with mathematical notation and structured solution steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adaptive hints; generated practice questions are checked for mathematical correctness and fit to the student's level.]

## Skill Version(s):

2.12.5 (source: frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
