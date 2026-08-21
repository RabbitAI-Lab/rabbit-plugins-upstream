## Description:

A teacher-assistant skill for grading A1/A2/B1 Japanese reading audio with faster-whisper transcription, acoustic checks, four-dimension 10-point scoring, feedback, reports, and teacher final review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bianmaxingkong](https://clawhub.ai/user/bianmaxingkong)

### License/Terms of Use:

MIT-0

## Use Case:

External teachers use this skill to pre-grade Japanese reading audio assignments for A1/A2/B1 learners, generate concise feedback, and route uncertain or low-confidence cases to teacher review before final grades are recorded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student audio, grades, generated reports, progress files, and failure records may contain sensitive student data.

Mitigation: Store generated local files according to the school's student-data policy and confirm teachers are comfortable processing this data locally before installing.

Risk: Automatic transcription and acoustic analysis can misread student speech or overstate pronunciation issues.

Mitigation: Use the skill's high, medium, and low confidence routing; keep low-confidence scores as diagnostic only and require teacher review before final grading.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text grading reports with optional local report, progress, and failure files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are intended to stay within 1000 characters; batch progress and failed-audio records may be stored locally for teacher review.]

## Skill Version(s):

2.2.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
