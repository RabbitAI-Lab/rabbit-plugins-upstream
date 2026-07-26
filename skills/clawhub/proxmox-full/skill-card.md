## Description: <br>
Complete Proxmox VE management - create/clone/start/stop VMs and LXC containers, manage snapshots, backups, storage, and templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msarheed](https://clawhub.ai/user/msarheed) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to manage Proxmox VE nodes, virtual machines, containers, snapshots, backups, storage, and templates through REST API commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This skill can give an agent broad control over Proxmox infrastructure. <br>
Mitigation: Use a dedicated least-privilege API token scoped to the required nodes, pools, or VMs, and keep privilege separation enabled where possible. <br>
Risk: Destructive actions such as stop, rollback, delete, purge, restore, clone, and template operations can disrupt workloads or remove resources. <br>
Mitigation: Require explicit human confirmation before running destructive or high-impact operations. <br>
Risk: Examples include insecure TLS bypass and plaintext credential patterns. <br>
Mitigation: Configure trusted TLS instead of using -k, and avoid plaintext passwords in commands. <br>


## Reference(s): <br>
- [Proxmox](https://www.proxmox.com/) <br>
- [ClawHub Skill Page](https://clawhub.ai/msarheed/skills/proxmox-full) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and Proxmox API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses curl and jq examples with PVE_URL and PVE_TOKEN environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
