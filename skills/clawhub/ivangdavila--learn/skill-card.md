## Description: <br>
Runs self-directed learning as a system: a curriculum with an exit test, deliberate practice, spaced review, and proof that learning transferred. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to plan and operate self-directed learning for subjects without a course or exam. It helps an agent create testable curricula, run retrieval practice and spaced review, diagnose stalled progress, and persist learning records across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill keeps persistent local learning records and related project, contact, and subscription notes under ~/Clawic/data/. <br>
Mitigation: Review the configured local paths before installing, avoid storing secrets or unnecessary personal details, and back up or inspect local notes according to the user's data policy. <br>
Risk: Retiring a topic may update or delete a local paid-learning subscription row, but that bookkeeping does not cancel external billing. <br>
Mitigation: Treat subscription-row changes as reminders only and confirm cancellation directly with the external course, tutor, or platform. <br>
Risk: The skill can migrate, write, update, or delete local note rows as part of its learning workflow. <br>
Mitigation: Use the skill's announced file-operation lines to audit changes, and keep durable records inside the declared Clawic data paths. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/learn) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic Learn page](https://clawic.com/skills/learn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured local-note updates and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write or update local learning records, review queues, project notes, contact notes, and paid-learning subscription bookkeeping under the configured local Clawic data paths.] <br>

## Skill Version(s): <br>
1.0.4 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
