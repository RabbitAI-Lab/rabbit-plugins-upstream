## Description: <br>
Helps agents diagnose, repair, and harden Linux hosts across permissions, storage, memory, systemd, networking, SSH, boot, packages, monitoring, backups, compromise response, and desktop issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, system administrators, and operators use this skill to troubleshoot Linux host incidents, plan safer operational changes, harden exposed systems, and maintain host notes without storing credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest sudo or root-level commands that affect SSH, firewalls, fstab, storage, package state, or deletion targets. <br>
Mitigation: Review commands before execution, use validators where available, and keep rollback or recovery access in place for remote changes. <br>
Risk: Operational notes could accidentally capture secret values if pasted or summarized carelessly. <br>
Mitigation: Store pointers to secrets such as file, environment, keychain, or vault locations instead of credential values. <br>
Risk: Linux distributions and host environments differ, so an otherwise valid command can be wrong for a specific machine. <br>
Mitigation: Confirm the host identity, distribution family, init system, firewall tool, and relevant baseline before applying changes. <br>


## Reference(s): <br>
- [ClawHub Linux skill page](https://clawhub.ai/ivangdavila/skills/linux) <br>
- [Clawic Linux skill page](https://clawic.com/skills/linux) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include sudo or root-level operational commands; review before execution.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
