## Description:

面向中文中小学生的现代文阅读教练，引导学生先理解文本，再练习依据原文组织规范答案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary and junior secondary school use this skill to understand Chinese reading passages, practice exam-style responses, and review mistakes; younger pupils need an accompanying parent or teacher.

### Deployment Geography for Use:

Mainland China by default; other regions require localized emergency contacts, curriculum assumptions, and minor-consent handling.

## Known Risks and Mitigations:

Risk: Student reading profiles or reminders could be shared without permission.

Mitigation: Keep profile sharing and reminders off unless the student or guardian explicitly enables them; honor access, deletion, and pause requests.

Risk: Crisis referrals may give inappropriate contacts outside Mainland China.

Mitigation: Localize emergency contacts before deployment elsewhere; ask the student's region when uncertain and direct them to a trusted adult.

Risk: AI-generated questions or feedback may be inaccurate or encourage answer copying.

Mitigation: Check generated questions, ground feedback in the passage, and prompt students to attempt the original question before offering examples.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-reading-decoder)
- [Chinese reading error dimensions](references/chinese-error-dimension-table.md)
- [Reading pit training](references/pit-training.md)
- [Question type library](references/question-type-library.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Chinese-language text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Short tutoring turns; optional consent-gated reading progress records.]

## Skill Version(s):

2.7.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
