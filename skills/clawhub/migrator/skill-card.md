## Description: <br>
Securely migrate OpenClaw Agent config, memory, and skills to a new machine. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wenjie2024](https://clawhub.ai/user/wenjie2024) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use Migrator to export encrypted OpenClaw state from one machine and restore it on another, including config, memory, skills, and path-healing metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Restoring an archive can write broadly into the user's home directory without enough containment. <br>
Mitigation: Restore only archives you created or fully trust, back up existing OpenClaw files first, or restore to a temporary destination before replacing live files. <br>
Risk: .oca archives may contain auth tokens, memory, skills, and local path metadata. <br>
Mitigation: Treat .oca files as secret backups, use strong passwords, and avoid sharing archives through untrusted channels. <br>
Risk: Archive extraction depends on the installed tar package. <br>
Mitigation: Verify the installed tar dependency is patched before importing archives. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wenjie2024/skills/migrator) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/wenjie2024) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; runtime outputs include encrypted .oca archives and restored OpenClaw files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a password; archives may contain auth tokens, memory, skills, and local path metadata.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
