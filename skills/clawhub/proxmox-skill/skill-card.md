## Description: <br>
Manage Proxmox VE nodes, VMs, and containers by listing hardware stats and resources, controlling power states, and managing snapshots. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robnew](https://clawhub.ai/user/robnew) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to let an agent inspect Proxmox VE cluster resources, monitor node health, control VM and container power states, and manage snapshots through the Proxmox API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform infrastructure-control actions such as VM or container power operations and snapshot rollback or deletion. <br>
Mitigation: Install it only with a Proxmox API token scoped to the specific nodes, VMs, containers, and actions the agent should manage, and keep approval enabled for destructive actions. <br>
Risk: A broad Proxmox API token could allow an agent mistake to affect more infrastructure than intended. <br>
Mitigation: Use a dedicated non-root token, assign the least-privilege Proxmox role needed for the workflow, and avoid cluster-wide permissions unless they are required. <br>
Risk: Unpinned Python dependency ranges can change behavior across installations. <br>
Mitigation: Pin and review proxmoxer and requests versions in controlled or production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/robnew/skills/proxmox-skill) <br>
- [Publisher profile](https://clawhub.ai/user/robnew) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Proxmox API credentials from PVE_HOST, PVE_TOKEN_ID, and PVE_TOKEN_SECRET.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
