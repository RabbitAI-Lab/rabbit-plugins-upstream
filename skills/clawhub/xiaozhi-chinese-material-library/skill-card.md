## Description:

帮助学生保存、标记和检索语文写作素材，并在学生请求时汇总素材使用情况。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use this skill to collect tagged Chinese-language writing materials, find relevant quotations or examples, and review student-confirmed usage. It supports the writing coach without taking over the writing process.

### Deployment Geography for Use:

Global (localize curriculum, guardian consent and crisis contacts outside Mainland China)

## Known Risks and Mitigations:

Risk: Student writing materials may be retained or usage counts shared beyond the current session.

Mitigation: Check memory and consent controls before use; save only on student request and share usage counts only with explicit consent.

Risk: Chinese curriculum assumptions, guardian-consent rules and crisis contacts may not fit users outside Mainland China.

Mitigation: Localize educational guidance, consent rules and emergency referrals for the user's region before deployment.

Risk: Recommended quotations may be attributed incorrectly or usage totals may overstate verified activity.

Mitigation: Mark uncertain sources for student confirmation and count usage only when the student confirms it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-material-library)
- [Learning profile schema](https://xiaozhi-skills.openclaw.dev/schemas/dna-profile.schema.json)
- [Skill handover schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown and plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tagged material lists, writing-placement suggestions and on-request usage summaries; cross-session history depends on platform memory and consent.]

## Skill Version(s):

2.7.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
