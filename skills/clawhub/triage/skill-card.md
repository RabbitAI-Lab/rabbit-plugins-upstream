## Description: <br>
Prioritizes competing tasks into P0-P3 by cost of delay and decides what to do first, what waits, and when to interrupt current work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and knowledge workers use this skill when multiple tasks, bugs, alerts, deadlines, or interrupt requests compete for attention. It assigns P0-P3 priority, orders the queue, and decides when to interrupt current work while learning explicitly confirmed priority preferences. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed rules and recent correction history may include sensitive task names, sender names, or deadlines in the local triage data folder. <br>
Mitigation: Review the local triage data folder before using the skill with sensitive work, and only confirm standing rules that are appropriate to persist. <br>
Risk: Incomplete urgency signals can lead to an incorrect queue order or an unnecessary interruption. <br>
Mitigation: Use the skill's P0/P1 boundary question and review announced queue changes before acting on high-impact priority decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/triage) <br>
- [Clawic skill page](https://clawic.com/skills/triage) <br>
- [Batch triage guidance](artifact/batch.md) <br>
- [Bug, ticket, and alert triage guidance](artifact/bugs.md) <br>
- [Deadline triage guidance](artifact/deadlines.md) <br>
- [Interrupt handling guidance](artifact/interrupts.md) <br>
- [Priority pattern learning protocol](artifact/patterns.md) <br>
- [Urgency signal guidance](artifact/signals.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown or plain text priority recommendations with optional local preference/configuration updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference or update local triage preference files only after explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.3 (source: artifact/SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
