## Description: <br>
Create a full local backup of the OpenClaw workspace and configuration using the existing backup-local.sh script. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[trumppo](https://clawhub.ai/user/trumppo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
OpenClaw users and operators use this skill to trigger a complete local backup and receive the resulting archive path and size. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Backup archives may contain workspace files, configuration, or secrets. <br>
Mitigation: Protect access to archives stored under /root/.openclaw/backups and review storage permissions before broad use. <br>
Risk: Repeated local backups may consume disk space. <br>
Mitigation: Monitor available disk capacity and manage backup retention through an approved operational process. <br>
Risk: The wrapper depends on an external backup-local.sh script for the actual backup behavior. <br>
Mitigation: Review that script before deployment and confirm it matches the intended backup policy. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text status report with the backup archive path and size.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs a local backup wrapper when the expected backup script is executable.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
