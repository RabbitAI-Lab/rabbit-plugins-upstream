## Description: <br>
Real-time companion monitor for OpenClaw agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luccast](https://clawhub.ai/user/luccast) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use Crabwalk to install, start, and manage a real-time monitor for OpenClaw agent activity, workspace browsing, and markdown viewing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The monitor can expose live agent activity and workspace files through a network-facing server. <br>
Mitigation: Prefer localhost access, review the workspace path before starting the monitor, and avoid sharing LAN URLs on untrusted networks. <br>
Risk: Gateway-token-backed access may expose sensitive OpenClaw activity if the server is reachable by unintended users. <br>
Mitigation: Provide the gateway token explicitly only when needed and keep the server scoped to trusted local access. <br>
Risk: Optional QR support may trigger noninteractive package installs using sudo on supported package managers. <br>
Mitigation: Review install commands before execution and install optional dependencies manually when elevated privileges are required. <br>


## Reference(s): <br>
- [Crabwalk ClawHub skill page](https://clawhub.ai/luccast/skills/public) <br>
- [Crabwalk homepage](https://crabwalk.app) <br>
- [Crabwalk repository](https://github.com/luccast/crabwalk) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes install, verification, startup, update, and troubleshooting instructions for a monitoring server.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
