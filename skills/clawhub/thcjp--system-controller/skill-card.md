## Description: <br>
系统控制器 helps an AI agent manage operating-system processes, services, files, environment settings, scheduled tasks, and system information across Linux, macOS, and Windows through a unified command posture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and automation-focused agent users use this skill to inspect and change local system state, troubleshoot services, initialize environments, edit files with rollback posture, and manage scheduled tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct broad system-administration actions across processes, services, files, environment settings, and scheduled tasks. <br>
Mitigation: Install it only for agents expected to administer the local system, restrict activation and policy settings, and require explicit approval for persistent changes, cron edits, service changes, permission changes, deletes, and force kills. <br>
Risk: Incorrect process, service, or file changes can disrupt running systems or damage data. <br>
Mitigation: Use the skill's lower-risk modes where available, including graceful termination, dry runs, atomic writes, backups, rollback, and audit-log review. <br>
Risk: The server security verdict flags this release as suspicious because of its broad command-execution authority. <br>
Mitigation: Review the skill before deployment and confirm that its audit, backup, and approval expectations match the target environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/system-controller) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose privileged system-administration actions that require appropriate local permissions and explicit approval for higher-risk changes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
