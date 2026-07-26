## Description: <br>
Securely migrate OpenClaw Agent (config, memory, skills) to a new machine. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wenjie2024](https://clawhub.ai/user/wenjie2024) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to export encrypted agent state from one machine and restore it on another while updating workspace paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Imported archives can change sensitive OpenClaw state. <br>
Mitigation: Back up the destination OpenClaw state first and import only archives you created or fully trust. <br>
Risk: The archive extraction path needs review before normal use. <br>
Mitigation: Review the destination path and restored files before relying on the imported state. <br>
Risk: Migration archives can contain sensitive configuration, keys, memory, and agent state. <br>
Mitigation: Use strong passwords and keep archives private. <br>


## Reference(s): <br>
- [OpenClaw Migrator ClawHub release page](https://clawhub.ai/wenjie2024/skills/openclaw-migrator) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration] <br>
**Output Format:** [Encrypted .oca archive files, restored OpenClaw directories, and terminal status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a password for archive export and import.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; package.json reports 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
