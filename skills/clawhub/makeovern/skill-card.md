## Description: <br>
This skill helps users run timed focus sessions using the Pomodoro technique from the terminal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abeljseba](https://clawhub.ai/user/abeljseba) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to start Pomodoro focus blocks, customize timer duration, log completed sessions, and review today's local session log from the terminal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional logging command creates or updates ~/pomodoro.log with session timestamps. <br>
Mitigation: Review the logging command and use it only if local session history in that file is acceptable. <br>
Risk: Timer commands wait in the terminal and may run for the configured focus duration. <br>
Mitigation: Run the commands in an appropriate shell session and adjust the duration before execution when needed. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes terminal timer commands, optional macOS notification command, and optional local logging to ~/pomodoro.log.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
