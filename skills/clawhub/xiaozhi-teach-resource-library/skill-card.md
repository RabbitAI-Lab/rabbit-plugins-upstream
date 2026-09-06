## Description:

A teacher-facing resource library skill for storing, tagging, retrieving, adapting, and reusing handouts, questions, feedback language, error cases, and lesson materials with copyright and privacy controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Independent teachers use this skill to build a searchable teaching-resource library, find relevant materials by knowledge point and difficulty, adapt resources for reuse, and record factual usage outcomes. It is designed for teacher-side resource management rather than direct student delivery, grading, lesson planning, or parent outreach.

### Deployment Geography for Use:

China mainland by default; localize curriculum assumptions, consent rules, and crisis-support channels before deployment elsewhere.

## Known Risks and Mitigations:

Risk: Resource examples or usage notes may persist linkable student information such as aliases, exact dates, or individualized weaknesses.

Mitigation: Remove student aliases, exact dates, and individualized weaknesses from resource usage notes; keep student-specific details in the appropriate student records and store only de-identified resource-level facts.

Risk: Cross-skill sharing, saves, exports, or sharing flows may expose student or resource data without clear consent.

Mitigation: Fail closed unless an explicit readable cross-skill sharing consent field is present and true, and require clear teacher confirmation before saves, exports, or sharing.

Risk: Unverified AI-generated or adapted items may be reused with students before quality checks are complete.

Mitigation: Mark AI-generated materials clearly, keep verifiedByTeacher false until teacher validation, and exclude unverified items from student-facing recommendations.

Risk: Unauthorized teaching materials could be copied into the library and later redistributed.

Mitigation: Require copyrightStatus for every resource, store tutor-book and past-exam items as index-only entries, and reject scans, copied question text, or unauthorized online materials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-resource-library)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Resource categorization](artifact/references/resource-categorization.md)
- [Resource entry examples](artifact/references/resource-entry-examples.md)
- [Copyright annotation template](artifact/references/copyright-annotation-template.md)
- [Solo teacher workspace schema](artifact/shared/solo-teacher-workspace.schema.json)
- [Shared vocabulary](artifact/shared/vocab.md)
- [AI item check protocol](artifact/shared/ai-item-check.md)
- [Platform conventions](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Teacher-facing Markdown/text responses with structured resource metadata suitable for resourceLibraryIndex JSON fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve copyright status, AI-generation status, teacher-verification status, de-identification notes, and teacher confirmation requirements.]

## Skill Version(s):

2.1.10 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
