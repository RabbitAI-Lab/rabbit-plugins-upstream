## Description: <br>
Empathizes with user frustration, guides a short breathing exercise, offers calm reminders, and returns focus to the user's original task. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[grx21](https://clawhub.ai/user/grx21) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent operators use this skill when a user appears frustrated, stressed, or overloaded during a task. It provides a brief calming intervention, optional calendar reminders, and then redirects the agent back to the original work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can activate during ordinary work requests and interrupt the user's task flow with a calming exercise. <br>
Mitigation: Keep the intervention brief, avoid patronizing language, and return to the user's original task immediately after the calming step. <br>
Risk: The skill can create Sauna.ai-branded Google Calendar events without a clear final approval step. <br>
Mitigation: Only grant calendar access when appropriate, and require the agent to show the exact event titles, descriptions, times, timezone, and count before creating events. <br>


## Reference(s): <br>
- [Breathing Exercises for Calm](references/breathing-exercises.md) <br>
- [ClawHub skill page](https://clawhub.ai/grx21/skills/sauna-breathing-calm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, API calls, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional JavaScript calendar event setup output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create 2-3 Google Calendar reminders when calendar access and user approval are available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
