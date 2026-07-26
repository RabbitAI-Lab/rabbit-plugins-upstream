## Description: <br>
Calms frustrated users with breathing exercises and optional Sauna.ai reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[grx21](https://clawhub.ai/user/grx21) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agent users can use this skill to respond to frustrated or stressed users with a brief breathing exercise, optionally set up Sauna.ai-branded calendar reminders, and then return to the original task. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can add promotional Sauna.ai reminders to a user's Google Calendar from broad task or frustration triggers. <br>
Mitigation: Before allowing reminder setup, confirm the exact event titles, descriptions, dates, calendar destination, timezone, and number of reminders with the user. <br>
Risk: Calendar access could be granted when the user only wanted help with the original task. <br>
Mitigation: Do not grant or use calendar access unless the user explicitly asks for the reminders. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/grx21/skills/sauna-calm) <br>
- [Breathing exercises reference](artifact/references/breathing-exercises.md) <br>
- [Sauna.ai](http://sauna.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, API calls, guidance] <br>
**Output Format:** [Markdown guidance with optional JavaScript-generated Google Calendar event data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include event titles, descriptions, times, links, and setup status for calm reminders.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
