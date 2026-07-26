## Description: <br>
Remind helps an agent create, adjust, and deliver reminders for commitments the user already knows, such as meetings, deadlines, bills, promises, follow-ups, recurring obligations, and timing reactions, without treating new information as reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use Remind to detect explicit and implicit reminder opportunities, choose actionable lead times, phrase reminders, manage local reminder preferences, and avoid reminder fatigue. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reminder-like statements may activate the skill when intent or timing is ambiguous. <br>
Mitigation: Review proposed reminders before relying on them, especially for implicit commitments or unclear timing. <br>
Risk: Reminder history and preferences are stored locally and can include personal commitments or timing preferences. <br>
Mitigation: Keep stored reminder data in the disclosed local folder and confirm preference changes before recording them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/remind) <br>
- [Remind homepage](https://clawic.com/skills/remind) <br>
- [Timing defaults](timing.md) <br>
- [Reminder triggers](triggers.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Natural-language reminder guidance with Markdown-backed reminder and preference records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use local reminder history and preferences under ~/Clawic/data/remind/ when reminders or preferences are created or updated.] <br>

## Skill Version(s): <br>
1.0.4 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
