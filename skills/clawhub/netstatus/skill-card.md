## Description: <br>
Combined network and gateway status with VPN information, IP location, local network details, Tailscale status, and system health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[space-cadet](https://clawhub.ai/user/space-cadet) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to quickly inspect network routing, VPN state, public IP location, local interfaces, Tailscale connectivity, gateway health, and system uptime from an agent chat. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The status output can expose local network addresses, Tailscale details, gateway state, and public-IP metadata in chat. <br>
Mitigation: Use only in contexts where sharing network and public-IP details is acceptable, and avoid posting outputs into sensitive or public channels. <br>
Risk: The skill contacts ipinfo.io to identify public IP location. <br>
Mitigation: Run only when third-party public-IP geolocation lookup is acceptable for the environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/netstatus) <br>
- [ipinfo.io API](https://ipinfo.io/json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown status report with shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local interface addresses, Tailscale IPs, VPN details, public IP metadata, gateway status, and system uptime.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
