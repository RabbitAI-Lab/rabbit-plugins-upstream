## Description: <br>
Control NordVPN on Linux via the `nordvpn` CLI for connect and disconnect actions, location selection, status checks, settings changes, and allowlist management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maciekish](https://clawhub.ai/user/maciekish) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation users use this skill to operate the NordVPN Linux CLI when workflows need VPN status checks, region routing, temporary tunneling, or controlled VPN setting changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: VPN connect, disconnect, settings, killswitch, and allowlist changes can affect local connectivity and privacy. <br>
Mitigation: Review proposed network-changing commands before execution and verify the resulting state with `nordvpn status` or `nordvpn settings`. <br>
Risk: The skill relies on a local NordVPN CLI binary and account login outside the skill. <br>
Mitigation: Install the CLI from a trusted NordVPN source and complete login manually before allowing the agent to operate it. <br>


## Reference(s): <br>
- [NordVPN homepage](https://nordvpn.com/) <br>
- [ClawHub NordVPN skill page](https://clawhub.ai/maciekish/skills/nordvpn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs human-readable CLI guidance and command sequences; NordVPN CLI status output may require defensive line-based parsing.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
