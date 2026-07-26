## Description: <br>
Backup agent brain (workspace) and body (state) to local folder and optionally sync to cloud via rclone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vacinc](https://clawhub.ai/user/vacinc) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to create encrypted local backups of agent workspaces, OpenClaw state, and skills, with optional rclone synchronization to a trusted cloud destination. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill backs up sensitive workspace, state, and skills data. <br>
Mitigation: Use a strong dedicated backup password, prefer a permissions-restricted key file, and review included directories before enabling backups. <br>
Risk: Optional rclone sync sends encrypted archives to a configured remote destination. <br>
Mitigation: Set remoteDest or REMOTE_DEST only for trusted cloud storage and verify the rclone remote before first use. <br>
Risk: Retention pruning deletes older local backup archives, and rclone sync can mirror remote deletions. <br>
Mitigation: Choose retention values deliberately and confirm the backup root and remote destination before scheduled or repeated runs. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Files] <br>
**Output Format:** [Shell execution output and encrypted .tgz.gpg backup archives] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires tar, gpg, rclone, jq, an OpenClaw config file, and a backup password supplied by key file, environment variable, or skill config.] <br>

## Skill Version(s): <br>
2.2.0 (source: package.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
