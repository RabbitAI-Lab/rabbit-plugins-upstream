## Description: <br>
Set timers and alarms, then notify the user when a background timer completes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hisxo](https://clawhub.ai/user/hisxo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents use this skill to set countdown timers, alarms, and reminders for users, including labeled timers for tasks such as cooking, breaks, and meetings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Timers run as local background Node processes until they complete or are cancelled. <br>
Mitigation: Use the documented process controls to list, poll, inspect logs, or cancel running timers. <br>
Risk: On macOS, completed timers may play a system sound. <br>
Mitigation: Install and use the skill only when local sound playback is acceptable for the environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hisxo/skills/timer) <br>
- [Publisher profile](https://clawhub.ai/user/hisxo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and timer notification text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Timers run as local background Node processes; completion is reported through process output and optional macOS sound playback.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
