## Description:

A Chinese-language K12 writing-teaching aid for teachers that supports writing-task design, process guidance, rubric-based review, style tracking, lesson review design, and class writing records without writing student essays or replacing teacher grading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K12 educators use this skill to design作文 tasks, structure student writing guidance, apply rubric-based correction criteria, prepare review lessons, and maintain class writing/style records under consent controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may handle student writing records and class-level learning data.

Mitigation: Use the platform consent fields before record use or parent sharing, prefer aliases, avoid retaining raw作文全文 unless necessary, and honor pause, delete, and share-control requests.

Risk: Teacher-facing outputs could be mistaken for final grades or official evaluations.

Mitigation: Treat rubric analysis and lesson-review text as drafts; the teacher remains responsible for final grading, sharing decisions, and classroom use.

Risk: Student writing may contain self-harm, bullying, family safety, or other crisis signals.

Mitigation: Stop normal writing-review workflows when crisis signals appear and follow the bundled crisis referral protocol, including region-aware emergency guidance.

Risk: Writing prompts or examples may create copyright or attribution issues if copied from external sources.

Mitigation: Require copyrightStatus labels for writing topics and keep textbook, workbook, and exam-bank questions as source indexes rather than copied prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-chinese-writing-guide)
- [Writing task design template](artifact/references/writing-task-template.md)
- [Three-dimensional writing rubric](artifact/references/three-dim-rubric.md)
- [Correction sample template](artifact/references/correction-sample-template.md)
- [Style DNA profile template](artifact/references/style-dna-profile-template.md)
- [Style DNA long-term record](artifact/references/style-dna-record.md)
- [Review lesson scripts](artifact/references/review-lesson-scripts.md)
- [Class teaching workspace schema](artifact/shared/class-teaching-workspace.schema.json)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Platform conventions](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with structured templates and JSON-compatible class record fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-facing drafts and criteria; final grading, sharing, and record updates require teacher review and consent checks.]

## Skill Version(s):

2.3.0 (source: server release evidence, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
