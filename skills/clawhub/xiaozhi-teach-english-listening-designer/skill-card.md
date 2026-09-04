## Description:

Designs English listening lessons for Chinese-language teaching contexts, turning simple playback and answer checking into a structured workflow for goals, material selection, pre-listening prediction, layered listening tasks, post-listening activities, micro-skill practice, and teacher-authorized workspace updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External English teachers use this skill to design listening lessons, select or adapt materials with copyright status, create pre-listening and while-listening tasks, and plan micro-skill training for upper-primary and middle-school learners. It is intended for Chinese-language classroom support and teacher-facing planning rather than automatic student scoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crisis-support wording includes mainland China emergency and hotline references that may not fit other locations.

Mitigation: Verify or replace crisis hotline text before using the skill outside mainland China.

Risk: Student listening records and profile writeback may expose learner performance data.

Mitigation: Pseudonymize student records, honor privacy controls, and require teacher authorization before profile writeback.

Risk: AI-generated listening materials or questions may be incorrect, unsuitable for the grade band, or unready for formal assessment.

Mitigation: Run the item self-check, mark AI-generated items, and require teacher verification before adding them to a resource bank or exam.

Risk: Listening materials may include audio or text with unclear usage rights.

Mitigation: Require copyrightStatus for each material and keep only source links or index entries when authorization is unclear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-listening-designer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Listening material sources](artifact/references/listening-material-sources.md)
- [Listening rubric](artifact/references/listening-rubric.md)
- [Micro-skill training](artifact/references/micro-skill-training.md)
- [Pre-listening prediction sample](artifact/references/pre-listening-prediction-sample.md)
- [While-listening task sample](artifact/references/while-listening-task-sample.md)
- [Student listening profile template](artifact/references/student-listening-profile-template.md)
- [AI item check protocol](artifact/shared/ai-item-check.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Platform conventions](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance, lesson plans, listening-task designs, rubrics, and JSON-compatible workspace entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is required for student profile writeback and AI-generated exam or resource-bank items.]

## Skill Version(s):

2.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
