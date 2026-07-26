## Description: <br>
Deploy and configure an OpenClaw instance on a GCP VM with Tailscale networking, Brave Search integration, and secure credential handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[divide-by-0](https://clawhub.ai/user/divide-by-0) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and infrastructure engineers use this skill to create a GCP VM and configure OpenClaw with Tailscale access, Brave Search, and secure credential handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to run powerful setup commands that install remote software and configure cloud services on a VM. <br>
Mitigation: Review each command before use, run it in a dedicated GCP project and VM, and consider pinning or verifying remote installers. <br>
Risk: API credentials and service configuration are kept on the VM. <br>
Mitigation: Use restricted file permissions, avoid exposing credentials in command-line arguments, and rotate Anthropic or Brave credentials if the VM is compromised or no longer needed. <br>
Risk: The deployment exposes access through SSH, firewall rules, and Tailscale service routing. <br>
Mitigation: Confirm cloud costs and network exposure, restrict inbound access to SSH and Tailscale as intended, and approve only trusted OpenClaw devices. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/divide-by-0/skills/create-new-openclaw-in-gcp) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with bash command blocks and setup notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes environment variable setup, VM provisioning commands, service configuration steps, troubleshooting notes, and security notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
