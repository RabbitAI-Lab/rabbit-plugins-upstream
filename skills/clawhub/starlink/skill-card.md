## Description: <br>
Controls a Starlink dish through the local gRPC API to check status, list WiFi clients, run speed tests, stow or unstow the dish, reboot it, and get GPS location. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[danfedick](https://clawhub.ai/user/danfedick) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill when they want an agent to inspect or manage a Starlink dish on the local network, including connectivity checks, client listings, speed tests, location lookup, reboot, and stow or unstow actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose local device and location data. <br>
Mitigation: Verify the CLI source repository before use and require explicit approval before showing client or location information. <br>
Risk: The skill can interrupt Starlink service by rebooting or stowing and unstowing the dish. <br>
Mitigation: Require explicit approval before rebooting the dish or changing stow state. <br>


## Reference(s): <br>
- [Starlink CLI source repository](https://github.com/danfedick/starlink-cli) <br>
- [ClawHub Starlink skill page](https://clawhub.ai/danfedick/skills/starlink) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the starlink CLI, local Starlink network access, and location access enabled in the Starlink app for GPS output.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
