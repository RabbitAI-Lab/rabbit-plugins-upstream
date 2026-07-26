## Description: <br>
A Proxmox-native orchestration skill that helps an agent manage, monitor, provision, and evolve a home-lab mesh of worker nodes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[spamtylor](https://clawhub.ai/user/spamtylor) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and home-lab operators use this skill to let an agent scan a local mesh, inspect workspace planning files for stalled projects, and prepare host provisioning steps for OpenClaw, Docker, Node.js, and Tailscale. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can scan local network addresses and alter home-lab machines. <br>
Mitigation: Run scans only on systems you own or administer, and review proposed machine changes before execution. <br>
Risk: The provisioning flow installs system tooling and runs remote installer scripts. <br>
Mitigation: Audit or rewrite the provisioning script before use, and avoid unattended mesh_provision execution. <br>
Risk: Proxmox credentials may grant broad infrastructure access. <br>
Mitigation: Use least-privilege Proxmox tokens and keep PVE_TOKEN_ID and PVE_TOKEN_SECRET out of logs and shared workspaces. <br>
Risk: The artifact claims hardening behavior that is not verified by the security evidence. <br>
Mitigation: Treat hardening claims as unverified and apply independent prompt-injection and network-safety controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/spamtylor/skills/hydra-evolver) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>
- [Artifact package manifest](artifact/package.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON outputs and shell-command oriented setup steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, docker, pm2, PVE_TOKEN_ID, and PVE_TOKEN_SECRET when using the relevant workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
