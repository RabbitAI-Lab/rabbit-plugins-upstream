## Description: <br>
Runs shell commands inside a dedicated tmux session named claw, captures pane output, and returns it to the agent with basic checks for destructive commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[imaginelogo](https://clawhub.ai/user/imaginelogo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to run shell commands in a dedicated tmux session and read recent terminal output without attaching to other sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill grants broad local shell access to an agent, and the built-in destructive-command checks are limited. <br>
Mitigation: Install only when shell access is intended, use a disposable or sandboxed environment, and review commands before they run. <br>
Risk: Command output and secrets may remain visible in the claw tmux session. <br>
Mitigation: Avoid exposing secrets in the session and clear or kill the tmux session when finished. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, text] <br>
**Output Format:** [JSON object containing the submitted command and captured terminal output, or an error object for invalid or blocked commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the tmux session named claw and captures recent pane output after a short delay.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
