## Description: <br>
Backs up and restores OpenClaw workspace state, agent folders, memories, cron jobs, and configuration across machines using a private GitHub repository. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anthonyfrancis](https://clawhub.ai/user/anthonyfrancis) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
OpenClaw users and developers use this skill to checkpoint personal assistant state, migrate between macOS/Linux machines, recover after data loss, and configure scheduled backups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install documentation includes a curl-to-bash path for unverified remote shell code. <br>
Mitigation: Prefer the git-clone installation path and review scripts before executing them. <br>
Risk: Backups may contain personal assistant identity, memory, notes, cron jobs, scripts, configuration, and agent folders. <br>
Mitigation: Use a private repository, narrowly scoped GitHub authentication, and keep secrets such as API keys and OAuth tokens outside backups. <br>
Risk: Backup, restore, reset, and scheduling commands can change workspace files, agent copies, shell PATH setup, cron entries, or launchd agents. <br>
Mitigation: Confirm the workspace, agent, shell profile, cron, and launchd paths before enabling automatic backups or running restore and reset commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anthonyfrancis/skills/openclaw-checkpoint) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with command-line examples and setup workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Targets macOS and Linux OpenClaw installations; Windows is not supported.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
