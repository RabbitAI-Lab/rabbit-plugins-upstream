## Description:

面向中文学习者的病句辅导技能，帮助识别六类常见语病、引导自主修改，并在同意后追踪反复出现的问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary and middle school use this skill to spot and revise Chinese grammar errors through guided questions and targeted practice. With consent, it tracks recurring error types and can provide progress summaries; primary-school students require adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A student's recurring-error profile or progress data could be recorded or shared without permission.

Mitigation: Keep profile tracking, cross-skill sharing, parent sharing, and reminders off until the student or guardian explicitly enables each; honor pause, correction, export, and deletion requests.

Risk: Incorrect grammar judgments or invented historical comparisons could mislead students.

Mitigation: Check examples and exercises before presenting them, acknowledge uncertain diagnoses, and avoid cross-session comparisons without available history.

Risk: A student's safety disclosure could be mistaken for an ordinary learning issue.

Mitigation: Stop grammar coaching and follow the skill's crisis-referral protocol; do not put incident details in the grammar profile.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-grammar-tracker)
- [Grammar error examples and checking methods](artifact/references/grammar-error-library.md)
- [Chinese error classification](artifact/shared/chinese-error-dimension-table.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language conversational guidance, exercises, and optional progress summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persistent tracking and sharing require separate consent; without history access, reports cover only the current session.]

## Skill Version(s):

2.8.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
