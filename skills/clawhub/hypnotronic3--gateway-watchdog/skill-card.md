## Description: <br>
Monitor an OpenClaw gateway, auto-restart on failure, and alert when recovery fails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hypnotronic3](https://clawhub.ai/user/hypnotronic3) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators can use this skill on Linux servers running an OpenClaw gateway that should recover automatically from health-check failures. It provides watchdog setup guidance, restart behavior, status files, and optional nginx endpoints for remote monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic restarts can disrupt an intentionally stopped or misconfigured OpenClaw gateway service. <br>
Mitigation: Install only where automatic recovery is intended, and review the configured service name, paths, restart limits, and cooldown before enabling the watchdog. <br>
Risk: Exposed nginx status endpoints may reveal operational state if published without access controls. <br>
Mitigation: Protect watchdog endpoints with authentication, IP allowlisting, or private-network access before exposing them. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/hypnotronic3/skills/gateway-watchdog) <br>
- [Publisher profile](https://clawhub.ai/user/hypnotronic3) <br>
- [Nginx status endpoint snippet](references/nginx-snippet.conf) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python, systemd, nginx, and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup steps and operational artifacts that should be reviewed before enabling automatic gateway restarts or exposing status endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
