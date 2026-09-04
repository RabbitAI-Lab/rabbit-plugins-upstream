## Description:

数学测评设计 helps math teachers turn intuition-based test writing into structured mathematics assessment design using goals, two-way blueprints, item selection, difficulty ratios, implementation plans, and item-level result analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External mathematics teachers use this skill to design junior-middle-school diagnostic, formative, and summative assessments, especially two-way blueprints aligned to knowledge points, curriculum-result levels, difficulty bands, item provenance, and post-test P/D analysis. It is intended for exam blueprinting and assessment interpretation, not for unsupported student labeling or full autonomous test publication.

### Deployment Geography for Use:

China-focused school contexts; use elsewhere requires localization of language, curriculum terms, privacy expectations, and crisis contacts.

## Known Risks and Mitigations:

Risk: The skill handles student assessment records and may write or summarize sensitive learning data.

Mitigation: Limit use to consent-gated assessment blueprinting, item statistics, and teacher-reviewed writeback; preserve the documented privacy controls for viewing, correcting, deleting, pausing, sharing, and exporting records.

Risk: Instructions can drift from exam design into learner diagnosis, student tiering, remediation planning, and parent-facing communication.

Mitigation: Keep deployment scope to exam blueprinting, item selection, and P/D item analysis unless adjacent specialist skills are explicitly enabled with clear controls.

Risk: Generated or adapted math items may be incorrect, unsuitable for the grade band, or lack publication rights.

Mitigation: Require teacher verification before items enter a test, label AI-generated items for review, and use the documented copyright status values so restricted sources are stored only as indexes.

Risk: Use outside a Chinese school context may produce mismatched language, curriculum assumptions, or crisis-contact guidance.

Mitigation: Localize curriculum terminology, reporting norms, privacy expectations, and crisis referral contacts before deployment in other contexts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-math-exam-designer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Exam design process](artifact/references/exam-design-process.md)
- [Blueprint template](artifact/references/blueprint-template.md)
- [Blueprint sample](artifact/references/blueprint-sample.md)
- [Difficulty gradient sample](artifact/references/difficulty-gradient-sample.md)
- [Result analysis rubric](artifact/references/result-analysis-rubric.md)
- [Class report sample](artifact/references/class-report-sample.md)
- [Student report sample](artifact/references/student-report-sample.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [AI item check protocol](artifact/shared/ai-item-check.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown text with structured tables and classWorkspace-compatible field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assessment blueprint rows, difficulty ratios, item metadata, P/D analysis notes, reliability caveats, and teacher verification flags.]

## Skill Version(s):

2.1.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
