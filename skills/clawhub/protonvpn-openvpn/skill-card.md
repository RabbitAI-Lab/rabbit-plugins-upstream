## Description: <br>
Manage ProtonVPN OpenVPN connections: connect, disconnect, rotate, and check status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage ProtonVPN OpenVPN sessions for privacy, geo-testing, IP rotation, and connection-status checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill recommends broad passwordless sudo for OpenVPN and process termination commands. <br>
Mitigation: Use tightly scoped root-owned helpers or sudoers rules limited to exact OpenVPN configuration paths and safe disconnect behavior. <br>
Risk: The skill uses writable /tmp paths for OpenVPN logs, process IDs, and rotation state involved in privileged network-control workflows. <br>
Mitigation: Prefer root-owned runtime paths with restricted permissions and validate PID ownership before terminating processes. <br>
Risk: Status checks contact ipinfo.io and expose active public IP and location metadata to that service. <br>
Mitigation: Only run status checks when that disclosure is acceptable, or replace the check with an approved internal endpoint. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/protonvpn-openvpn) <br>
- [ipinfo JSON endpoint](https://ipinfo.io/json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes OpenVPN connect, disconnect, rotate, and status-check commands that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
