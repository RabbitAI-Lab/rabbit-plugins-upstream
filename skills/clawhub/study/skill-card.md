## Description: <br>
Study helps an agent plan a student's term, run retrieval-based study sessions, track coursework and grades, and prepare for exams or certifications without producing work for submission. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students and agents assisting them use this skill to turn syllabi, readings, deadlines, marks, and exam dates into weekly plans, retrieval practice, error logs, spaced review, and exam or coursework preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may keep persistent local study records, including grades, missed questions, contacts, project milestones, and exam booking details. <br>
Mitigation: Review the configured Clawic data paths before use and keep those local notes in an appropriate user-controlled environment. <br>
Risk: Sensitive portal, LMS, SRS sync, or proctoring credentials could appear in pasted study material. <br>
Mitigation: Strip credential values before writing notes and retain only pointers such as keychain, environment-variable, password-manager, or local-file references. <br>
Risk: Coursework support can cross academic-integrity boundaries if the agent produces material submitted for credit. <br>
Mitigation: Use the default scaffold posture for graded work: provide questions, hints, critique, and worked analogues only after the student has attempted the task. <br>


## Reference(s): <br>
- [ClawHub Study skill page](https://clawhub.ai/ivangdavila/skills/study) <br>
- [Clawic Study homepage](https://clawic.com/skills/study) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with local note and configuration updates when persistent study records are needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May maintain local study records under the configured Clawic data paths; does not store credentials.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
