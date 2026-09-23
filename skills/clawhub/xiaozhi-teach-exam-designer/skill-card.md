## Description:

测评设计师 helps K12 teachers design assessment products from a two-way specification table, including exam blueprints, item selection or adaptation, difficulty balance, scoring rubrics, and post-exam review lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External teachers use this skill to draft classroom exams, two-way specification tables, scoring rubrics, item revision plans, and ordered review lists. It is intended for teacher-mediated K12 assessment design, with teacher review required before any AI-generated items enter a formal exam.

### Deployment Geography for Use:

Mainland China Chinese K12 deployments; confirm locale and local policy fit before deployment elsewhere.

## Known Risks and Mitigations:

Risk: Deployment outside the intended education and locale context could produce guidance that does not fit local policy or safety expectations.

Mitigation: Treat the release as a Mainland China Chinese K12 teacher workflow and confirm locale, school policy, and emergency-resource localization before deployment.

Risk: AI-generated or adapted exam items can be incorrect, ambiguous, misaligned with the blueprint, or unsuitable for a formal exam.

Mitigation: Keep teacher review mandatory: each AI-generated item should be solved and checked by a teacher before it is marked verified or used in a formal paper.

Risk: Exam records, student-related data, or cross-skill sharing could expose classroom information beyond the intended audience.

Mitigation: Use the provided privacy controls for exam records and sharing, avoid unnecessary sensitive data, and respect teacher-controlled export, deletion, and sharing settings.

Risk: Student safety or crisis signals could be mishandled if the assessment workflow continues as normal.

Mitigation: Stop exam-design activity when crisis signals appear and follow the bundled crisis referral protocol with localized emergency guidance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-exam-designer)
- [Exam Blueprint and Two-Way Specification Template](artifact/references/exam-blueprint.md)
- [AI Item Self-Check Protocol](artifact/shared/ai-item-check.md)
- [Class Teaching Workspace Schema](artifact/shared/class-teaching-workspace.schema.json)
- [Crisis Referral Protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown with structured tables and JSON-compatible classroom workspace fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are teacher-facing drafts; AI-generated exam items require teacher verification and the skill does not perform automatic grading.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
