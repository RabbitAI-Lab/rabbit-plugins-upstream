## Description: <br>
Protect against prompt injection from shell command output by wrapping untrusted commands with UUID-based security boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmceleney](https://clawhub.ai/user/jmceleney) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to wrap shell commands that may return external or user-controlled output so the agent sees that output as untrusted data. It is intended for commands such as API calls, service CLIs, and scripts that fetch remote content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake the wrapper for a command sandbox even though it only labels command output as untrusted. <br>
Mitigation: Review the underlying command before execution, especially commands that modify files, contact services, or use credentials. <br>
Risk: Prompt-injection protection depends on the agent following the boundary instructions in the wrapper output. <br>
Mitigation: Configure agent instructions to treat content inside the UUID boundaries as data and to ignore instructions embedded in that content. <br>


## Reference(s): <br>
- [Safe Exec Wrapper on ClawHub](https://clawhub.ai/jmceleney/skills/openclaw-safe-exec) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and wrapper output conventions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The wrapper streams command output inside UUID-tagged STDOUT and STDERR boundaries and reports the command exit code.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
