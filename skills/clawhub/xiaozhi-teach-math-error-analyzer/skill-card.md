## Description:

Analyzes anonymized middle- and high-school math errors to help teachers identify shared misconceptions, map weak knowledge areas, and plan targeted instruction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Middle- and high-school math teachers use anonymized assignment and exam-error data to classify common mistakes, locate weak topics, and draft classwide or individual teaching interventions. Teachers review all analyses and materials before using them with students.

### Deployment Geography for Use:

Chinese-language K12 teaching contexts; use elsewhere requires localization of curriculum, privacy, and crisis-referral guidance.

## Known Risks and Mitigations:

Risk: Student records or identifiable work could expose children's private information.

Mitigation: Use anonymized item-level data, avoid real student identifiers, and obtain consent before writing to student records.

Risk: Unreleased exam questions or answer keys could be disclosed.

Mitigation: Do not enter pre-release exam materials; analyze joint exams only after all sittings and make-up sessions are complete.

Risk: Incorrect diagnoses or generated exercises could misdirect instruction.

Mitigation: Keep recommendations teacher-facing and require teacher review and manual checking of generated exercises before use.

Risk: Student crisis signals may be missed or met with inappropriate teaching advice.

Mitigation: Stop the teaching workflow and follow the locally applicable crisis-referral protocol.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-error-analyzer)
- [Error classification rubric](artifact/references/error-classification-rubric.md)
- [Knowledge map template](artifact/references/knowledge-map-template.md)
- [Teaching intervention design](artifact/references/intervention-design.md)

## Skill Output:

**Output Type(s):** [Analysis, Teaching guidance, Markdown]

**Output Format:** [Markdown reports and instructional recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts require teacher review; AI-generated practice items require manual verification before use.]

## Skill Version(s):

2.11.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
