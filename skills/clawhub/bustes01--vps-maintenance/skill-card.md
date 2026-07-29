## Description: <br>
Guides agents through VPS initialization, security hardening, performance tuning, time synchronization, and routine maintenance tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bustes01](https://clawhub.ai/user/bustes01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and operators use this skill to prepare and maintain Debian or Ubuntu VPS hosts, including SSH hardening, firewall setup, system tuning, time synchronization, cleanup, and routine maintenance checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Root-level SSH, firewall, package, kernel, and systemd changes can disrupt access or service availability. <br>
Mitigation: Review every command before execution, keep an active SSH session while changing SSH or firewall rules, and confirm new access paths before closing existing sessions. <br>
Risk: Broad cleanup commands for temporary directories, logs, and caches can remove useful operational data or files still needed by services. <br>
Mitigation: Replace broad deletion with age-based or service-aware cleanup and preserve logs required for audit, debugging, or incident response. <br>
Risk: Default ports, timezones, mirrors, and tuning values may not match the target VPS environment. <br>
Mitigation: Customize ports, timezone, package mirrors, swap size, and kernel parameters for the host before applying changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bustes01/skills/vps-maintenance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and operational checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces root-level VPS administration guidance that should be reviewed and customized before execution.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
