## Description: <br>
Access passwords, secure notes, secrets and OTP codes from Dashlane vault. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gnarco](https://clawhub.ai/user/gnarco) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and other users can use this skill to ask an agent for Dashlane CLI guidance for vault lookup, synchronization, authentication, secret retrieval, and secret injection workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can expose vault contents through console output, JSON output, clipboard operations, logs, or command history. <br>
Mitigation: Review each command before execution, avoid console or JSON output in logged sessions, and prefer workflows that do not reveal secrets outside the intended destination. <br>
Risk: Secret persistence and injection workflows can store or pass master passwords and vault secrets into local files, environment variables, CI jobs, or subprocesses. <br>
Mitigation: Use backup, exec, inject, SSH-key piping, and master-password environment variables only when explicitly intended and approved for the operating environment. <br>


## Reference(s): <br>
- [Dashlane CLI documentation](https://cli.dashlane.com) <br>
- [ClawHub Dashlane skill page](https://clawhub.ai/gnarco/skills/dashlane) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that expose, copy, persist, inject, or back up secrets; review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
