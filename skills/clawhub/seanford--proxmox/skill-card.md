## Description: <br>
Manage Proxmox VE clusters via REST API. Use when user asks to list, start, stop, restart VMs or LXC containers, check node status, create snapshots, view tasks, or manage Proxmox infrastructure. Requires API token or credentials configured. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[seanford](https://clawhub.ai/user/seanford) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to inspect and manage Proxmox VE clusters, including VM and container lifecycle actions, node status checks, snapshots, task logs, storage, and backups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform disruptive Proxmox operations, including VM or container stop, shutdown, reboot, snapshot rollback, delete, and backup actions. <br>
Mitigation: Use a least-privileged Proxmox API token and require explicit human confirmation before shutdown, reboot, delete, rollback, or backup actions. <br>
Risk: The skill uses Proxmox API credentials from environment variables or a local credentials file. <br>
Mitigation: Protect the credentials file, avoid broad shell-session credential exports where possible, and restrict token permissions to the required cluster scope. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown with inline bash and curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Proxmox host and API token credentials configured by environment variables or a credentials file.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
