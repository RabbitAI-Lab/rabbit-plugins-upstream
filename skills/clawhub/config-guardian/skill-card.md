## Description: <br>
Safe OpenClaw config updates with automatic backup, validation, and rollback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abdhilabs](https://clawhub.ai/user/abdhilabs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and developers use this skill to propose and apply OpenClaw configuration changes with backup, validation, and automatic rollback before changes are accepted. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An incorrect config path or value could change local OpenClaw behavior unexpectedly. <br>
Mitigation: Review the exact config path and value before approving any run, and rely on validation plus rollback when a change fails. <br>
Risk: Backups may preserve sensitive values from the local OpenClaw configuration. <br>
Mitigation: Periodically remove old backups and protect the backup directory if the configuration contains sensitive values. <br>


## Reference(s): <br>
- [Config Guardian on ClawHub](https://clawhub.ai/abdhilabs/skills/config-guardian) <br>
- [Publisher profile](https://clawhub.ai/user/abdhilabs) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local OpenClaw config update guidance and commands that create backups, validate changes, and roll back on failure.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
