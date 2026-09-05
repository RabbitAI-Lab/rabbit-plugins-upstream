## Description:

Mock Interview (zjh) guides users through experience intake, generates five personalized interview questions, collects answers in a local web page with optional voice input, and produces five-dimension scoring feedback and an HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[2641183145-oss](https://clawhub.ai/user/2641183145-oss)

### License/Terms of Use:

MIT

## Use Case:

Developers and interview candidates use this skill to run a local, experience-driven mock interview workflow. The agent gathers the user's background, generates tailored deep-dive questions, waits for web-based answers, scores the responses, and creates an actionable feedback report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Interview background, answers, scores, and generated reports may contain sensitive personal information and are stored as plaintext local files.

Mitigation: Run the skill only on a trusted local machine and delete generated data files when the interview practice session is no longer needed.

Risk: Using browser voice input may involve browser speech services outside the local skill workflow.

Mitigation: Use typed answers instead of microphone input when speech-service processing is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/2641183145-oss/skills/mock-interview)
- [Experience intake reference](references/intake.md)
- [Question generation reference](references/question-gen.md)
- [Scoring rubric reference](references/rubrics.md)
- [API contract](api-contract.md)
- [Interview coach skill attribution](https://github.com/noamseg/interview-coach-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON session and score files, local HTML answer and report pages, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated questions and feedback are grounded in user-provided interview background and answers; generated reports are stored locally as HTML.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
