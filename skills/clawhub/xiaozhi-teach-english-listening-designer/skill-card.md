## Description:

Helps Chinese K12 English teachers design listening lessons with clear goals, level-appropriate materials, pre-listening prediction, layered listening tasks, post-listening work, and micro-skill practice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

External English teachers use this skill to turn listening classes from audio playback and answer checking into structured lessons with materials, tasks, rubrics, and follow-up training. It is designed for upper-primary and middle-school English listening instruction in a Chinese K12 context.

### Deployment Geography for Use:

China mainland; other regions require localized safety channels, curriculum alignment, and minor-data consent review before student-facing use.

## Known Risks and Mitigations:

Risk: The skill can handle minors' learning records and class listening data.

Mitigation: Confirm consent and storage practices before use, keep student data pseudonymized, and honor view, correction, deletion, pause, sharing-control, and export requests.

Risk: Listening materials or audio could be copied or shared without the right authorization.

Mitigation: Require a copyrightStatus for every material and add only authorized, self-owned, adapted, publicly reusable, or index-only materials to shared libraries.

Risk: AI-generated listening materials or questions may contain errors or unsuitable difficulty.

Mitigation: Label teacher-facing generated items as AI-generated and require teacher verification before adding them to resource libraries or exams.

Risk: Student crisis signals may appear during learning-support conversations.

Mitigation: Stop the teaching workflow when crisis signals appear, avoid recording sensitive details, and refer the student to a trusted adult and localized emergency support.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-listening-designer)
- [Listening material sources](references/listening-material-sources.md)
- [Listening rubric](references/listening-rubric.md)
- [Micro-skill training](references/micro-skill-training.md)
- [Pre-listening prediction sample](references/pre-listening-prediction-sample.md)
- [While-listening task sample](references/while-listening-task-sample.md)
- [Student listening profile template](references/student-listening-profile-template.md)
- [AI item check protocol](shared/ai-item-check.md)
- [Platform conventions and regional deployment notes](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)
- [Shared vocabulary and consent controls](shared/vocab.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Chinese Markdown lesson plans, listening-task templates, rubrics, and structured class-record update guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose class workspace updates; when voice synthesis is unavailable, it provides text and reading notes instead of audio.]

## Skill Version(s):

2.1.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
