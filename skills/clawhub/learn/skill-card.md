## Description: <br>
Runs self-directed learning as a durable system for curriculum planning, deliberate practice, spaced review, transfer checks, and learning records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to help a learner turn self-directed study into testable goals, practice sessions, review queues, verification tests, maintenance schedules, and persistent learning records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persistently edit learning records and related contacts, projects, and finance subscription records without clear per-action confirmation. <br>
Mitigation: Require confirmation before edits outside ~/Clawic/data/learn/ and before any deletion or migration. <br>
Risk: Learning records may include sensitive study context or account-adjacent details if the user asks the agent to save them. <br>
Mitigation: Follow the skill's credential-handling rule: store pointers to secrets, strip secret values, and avoid writing credentials under ~/Clawic/data/. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/learn) <br>
- [Clawic Learn Skill](https://clawic.com/skills/learn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance and structured learning records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update durable learning files and related shared project, contact, and subscription records when the agent has filesystem access.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
