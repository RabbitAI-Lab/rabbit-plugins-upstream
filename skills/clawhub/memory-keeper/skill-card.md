## Description: <br>
Memory Keeper copies and snapshots important agent context files into a dedicated archive directory or repository for backup, recovery, or host transfer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crimsondevil333333](https://clawhub.ai/user/crimsondevil333333) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use Memory Keeper to archive OpenClaw memory and context files before maintenance, recovery, migrations, or other operations where context loss is a concern. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can archive sensitive agent memory, context, and optional extra workspace files to a target directory or Git remote. <br>
Mitigation: Install it only when memory archiving is intentional, prefer local-only backups or a private repository, review copied files before pushing, and keep --allow-extra patterns narrow. <br>
Risk: Git remotes, commands, or memory logs may expose credentials or credential-bearing URLs. <br>
Mitigation: Use SSH keys or a credential helper, avoid embedding tokens in URLs or commands, and check memory logs and Git remotes before sharing or pushing archives. <br>


## Reference(s): <br>
- [Memory Keeper usage reference](references/usage.md) <br>
- [ClawHub skill page](https://clawhub.ai/crimsondevil333333/skills/memory-keeper) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated archive files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May copy selected workspace context files, append a memory log entry, and optionally create Git commits or pushes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
