## Description:

英语口语活动设计 helps Chinese K-12 English teachers turn recitation-style speaking lessons into task-based speaking activities with clear goals, classroom-ready workflows, feedback patterns, and teacher-reviewed workspace writeback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External educators and teaching agents use this skill to design English speaking classes for upper-primary and junior-middle-school learners, including task-based activities, differentiated prompts, feedback language, speaking rubrics, and optional teacher-controlled class-workspace updates.

### Deployment Geography for Use:

China mainland by default for curriculum, consent assumptions, and safety-channel defaults; localize curriculum, minor-data consent rules, and crisis referral channels before using elsewhere.

## Known Risks and Mitigations:

Risk: Student oral records and speaking notes may contain sensitive information about minors.

Mitigation: Confirm an approved school basis for storing oral records, keep records pseudonymized, and leave student-profile writeback disabled unless the required consent is present.

Risk: Generated lesson content or workspace entries could be used as authoritative teaching material without teacher review.

Mitigation: Require teacher review before student-facing use, resource-bank entry, or class-workspace writeback.

Risk: Speaking tasks, rubrics, and AI-generated items may be inaccurate, age-inappropriate, or misaligned with the target class.

Mitigation: Use the artifact's AI item check, grade-band constraints, and speaking rubric before classroom use; mark generated tasks as AI-generated until a teacher validates them.

Risk: Pronunciation feedback may be overclaimed when the platform only has text or speech transcription.

Mitigation: Do not make phoneme-level pronunciation judgments without an approved speech-assessment capability; keep pronunciation comments to teacher-observed intelligibility.

Risk: Student text may include crisis or safety signals outside the learning-support scope.

Mitigation: Stop the lesson workflow and follow the bundled crisis exception and referral protocol, including region-appropriate emergency guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-speaking-designer)
- [Task-based speaking activity template](references/task-based-template.md)
- [Speaking rubric](references/speaking-rubric.md)
- [Error-correction strategies](references/error-correction-strategies.md)
- [Feedback phrases](references/feedback-phrases.md)
- [Speaking profile template](references/speaking-profile-template.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured teaching-plan text with rubrics, task cards, feedback phrases, and workspace-ready field suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher review is required before student-facing use or workspace writeback; generated tasks should be marked as AI-generated before resource-bank entry.]

## Skill Version(s):

2.2.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
