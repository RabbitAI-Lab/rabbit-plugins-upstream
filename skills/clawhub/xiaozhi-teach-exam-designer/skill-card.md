## Description:

Helps teachers design curriculum-aligned assessments using exam blueprints, balanced question difficulty, item revisions, and scoring rubrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers in Chinese primary and middle schools use this skill to plan tests, prepare question-by-objective blueprints and marking rubrics, and identify questions to revise from existing post-exam statistics. Teachers must review generated questions before using them in a formal exam.

### Deployment Geography for Use:

Mainland China; localize crisis contacts, curriculum assumptions, and consent defaults before use elsewhere.

## Known Risks and Mitigations:

Risk: AI-generated questions may contain incorrect answers or unsuitable difficulty.

Mitigation: Require the teacher to solve and verify each generated question before it enters a formal exam.

Risk: Crisis referrals, curriculum expectations, and consent assumptions may not fit other regions.

Mitigation: Localize these defaults before use outside the intended Chinese K12 setting.

Risk: Exam records may expose student information or be written without appropriate oversight.

Mitigation: Confirm that the platform enforces workspace controls and teacher-approved writebacks; use pseudonyms and aggregate statistics.

Risk: Unreleased exam questions or copyrighted source material may be disclosed.

Mitigation: Do not submit confidential exam materials; retain source and reuse status, and avoid copying unauthorized questions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-exam-designer)
- [Exam blueprint and scoring templates](references/exam-blueprint.md)
- [AI-generated question review checklist](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Structured text and Markdown tables for exam blueprints, questions, scoring rubrics, and revision lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional teacher-confirmed exam blueprint writeback; post-exam statistics are read-only.]

## Skill Version(s):

2.7.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
