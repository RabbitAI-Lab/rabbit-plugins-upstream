## Description:

Helps Chinese middle and high school math teachers design assessment blueprints, select and label questions, analyze item-level results, and propose teacher-confirmed record updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Math teachers use this skill to plan Chinese middle and high school assessments with knowledge-by-skill blueprints, question sourcing, and item-level difficulty and discrimination analysis. It drafts candidate questions and record updates for teacher review rather than producing a finalized exam or grading students.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Classroom assessment records could be accessed or changed beyond the intended scope.

Mitigation: Enforce the documented workspace field whitelist and require teachers to review each proposed writeback before saving.

Risk: Draft AI-generated questions may contain errors or be mistaken for approved exam items.

Mitigation: Label drafts clearly and have a teacher check each question before including it in an exam.

Risk: Sensitive student results or unreleased exam questions may be exposed.

Mitigation: Keep access limited to necessary classroom fields, avoid uploading unreleased exam questions, and confirm sharing permissions before disclosing results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-exam-designer)
- [Assessment blueprint template](references/blueprint-template.md)
- [Assessment design process](references/exam-design-process.md)
- [Item analysis rubric](references/result-analysis-rubric.md)
- [High school blueprint example](references/math-hs-blueprint-sample.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown tables and prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes assessment blueprints, item statistics when scores are available, and draft questions or record updates requiring teacher confirmation.]

## Skill Version(s):

2.7.1 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
