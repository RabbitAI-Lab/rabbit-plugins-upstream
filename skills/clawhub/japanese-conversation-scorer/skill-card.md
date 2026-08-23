## Description:

A Japanese conversation grading skill for A1/A2/B1 learners that transcribes audio with faster-whisper, creates teacher-reviewed content, accuracy, and fluency pre-scores, and generates teacher and student feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bianmaxingkong](https://clawhub.ai/user/bianmaxingkong)

### License/Terms of Use:

MIT-0

## Use Case:

External language teachers use this skill to review Japanese conversation-test recordings, generate preliminary scores and feedback, and export grade summaries while keeping final grading under teacher review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student audio, transcripts, grades, and feedback may be sensitive educational records.

Mitigation: Confirm the school permits AI-assisted processing before use and keep student data within approved local or institutional workflows.

Risk: Optional course-platform adapters may access submissions or post grades and feedback.

Mitigation: Prefer the default CSV workflow unless an adapter has been reviewed, keep API tokens in local configuration or environment variables, and require teacher confirmation before posting grades.

Risk: ASR and automated scoring can misread speech or produce uncertain preliminary scores.

Mitigation: Use the skill's confidence checks, exclude low-confidence AI scores from student-facing output, and require teacher review before final grading or error deductions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bianmaxingkong/skills/japanese-conversation-scorer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown feedback, local text reports, CSV summaries, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces separate teacher-facing detailed feedback and student-facing concise feedback; low-confidence ASR results require teacher grading.]

## Skill Version(s):

1.1.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
