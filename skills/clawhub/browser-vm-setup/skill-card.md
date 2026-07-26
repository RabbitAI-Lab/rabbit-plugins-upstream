## Description: <br>
Run a browser-driving agent on a Linux VM by covering Xvfb setup, Chromium launch traps, egress cost tiers, and mandatory stop points for bot defenses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexbloch-ia](https://clawhub.ai/user/alexbloch-ia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to provision and harden a Linux VM for browser-driving agents, including Xvfb, Chromium launch troubleshooting, SSH-tunneled access, retention cleanup, and direct-egress operating rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Privileged VM setup and a local dashboard with shell-level access can expose administrative control if made public. <br>
Mitigation: Keep the dashboard bound to loopback, use SSH tunneling or a private mesh, and avoid public exposure. <br>
Risk: Browser sessions, screenshots, and logs may contain personal data or authenticated state. <br>
Mitigation: Use the skill only on infrastructure you control, minimize captured data, and install and verify retention cleanup. <br>
Risk: Proxy or residential egress paths can create authorization and compliance risk. <br>
Mitigation: Use direct egress by default and require explicit target authorization before any non-direct egress path is configured. <br>


## Reference(s): <br>
- [OpenClaw](https://openclaw.ai) <br>
- [ClawHub skill page](https://clawhub.ai/alexbloch-ia/skills/browser-vm-setup) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash, JSON, and checklist blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces human-facing setup guidance and an operational status block for browser-agent VM provisioning.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
