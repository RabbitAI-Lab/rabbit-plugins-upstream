## Description: <br>
Brainz Calendar helps agents manage Google Calendar events with gcalcli, including creating, listing, and deleting events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, teams, and automation users can use this skill to plan work, query schedules, and manage Google Calendar events through an agent. It is intended for explicit Google Calendar tasks and is not suitable for personnel performance evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar deletion actions can remove Google Calendar events. <br>
Mitigation: Require the agent to show the exact event or events before deletion and proceed only after explicit confirmation. <br>
Risk: Command execution through gcalcli can operate against authenticated calendar data. <br>
Mitigation: Grant command execution only when gcalcli authentication and calendar scopes are understood and appropriate for the task. <br>
Risk: The security review flagged the skill as not clearly scoped enough for command execution and deletion capabilities. <br>
Mitigation: Review the skill before installing and use it only for explicit Google Calendar tasks. <br>


## Reference(s): <br>
- [Brainz Calendar on ClawHub](https://clawhub.ai/thcjp/skills/brainz-calendar) <br>
- [Publisher profile: thcjp](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline command and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Google Calendar event details, deletion confirmations, troubleshooting steps, and setup guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
