## Description: <br>
Comprehensive security hardening and installation guide for OpenClaw (formerly Clawdbot/Moltbot). Use this skill when the user wants to secure a server, install the OpenClaw agent, or configure Tailscale/Firewall for the agent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kime541200](https://clawhub.ai/user/kime541200) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and server operators use this skill to harden a self-hosted OpenClaw server, configure SSH, firewall, and Tailscale access, install OpenClaw, and run basic verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: SSH and firewall hardening steps can lock an operator out of the server if applied without recovery access. <br>
Mitigation: Confirm a sudo-capable non-root account, tested SSH keys, an open backup SSH session, and console recovery before changing SSH or UFW settings. <br>
Risk: The Tailscale installation command executes a remote installer with elevated privileges. <br>
Mitigation: Prefer a verified package-based Tailscale install or inspect the installer before execution. <br>
Risk: Restricting SSH and web access to the Tailscale subnet can remove public access before private network connectivity is confirmed. <br>
Mitigation: Validate Tailscale connectivity and UFW allow rules before deleting public SSH or web access rules. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kime541200/skills/openclaw-server-secure-skill) <br>
- [Tailscale install script referenced by the skill](https://tailscale.com/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Privileged server changes require operator review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
