## Description: <br>
Manage Proxmox VE clusters via REST API. Use when user asks to list, start, stop, restart VMs or LXC containers, check node status, create snapshots, view tasks, or manage Proxmox infrastructure. Requires API token or credentials configured. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weird-aftertaste](https://clawhub.ai/user/weird-aftertaste) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to inspect and manage Proxmox VE nodes, virtual machines, LXC containers, snapshots, tasks, storage, and backups through configured Proxmox REST API credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Powerful Proxmox credentials can allow disruptive infrastructure actions such as stop, reboot, rollback, delete, or backup operations. <br>
Mitigation: Use a dedicated least-privilege API token and require explicit confirmation before disruptive operations. <br>
Risk: Credential material may be exposed if stored with broad permissions or pasted into shared shells and logs. <br>
Mitigation: Protect ~/.proxmox-credentials with strict permissions and avoid placing secrets in shared shells or logs. <br>
Risk: Skipping TLS verification can reduce confidence in the Proxmox endpoint connection. <br>
Mitigation: Prefer valid TLS certificates over curl -k whenever possible. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/weird-aftertaste/skills/proxmox) <br>
- [Publisher Profile](https://clawhub.ai/user/weird-aftertaste) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Proxmox REST API command guidance and helper-script usage notes that require user-provided cluster credentials.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
