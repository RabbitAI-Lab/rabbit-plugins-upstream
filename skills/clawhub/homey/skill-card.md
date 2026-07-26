## Description: <br>
Control Athom Homey smart home devices via local (LAN/VPN) or cloud APIs, including device control, flow triggering, and zone queries for Homey Pro, Cloud, and Bridge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maxsumrall](https://clawhub.ai/user/maxsumrall) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect and control Homey smart-home devices, zones, and flows through local or cloud Homey APIs. It is intended for smart-home administration tasks such as reading device state, changing supported device capabilities, and triggering automations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate real smart-home devices and automations, including sensitive devices such as locks, alarms, garage doors, heaters, or critical flows. <br>
Mitigation: Use the least-privileged Homey token available, restrict access to sensitive devices unless explicit confirmation rules are in place, and verify device or flow IDs before running state-changing commands. <br>
Risk: Fuzzy matching can resolve partial or misspelled device and flow names, which may select an unintended target if names are similar. <br>
Mitigation: Use JSON listings or explicit IDs for important actions and review ambiguous candidate responses before issuing control commands. <br>


## Reference(s): <br>
- [Homey Skill Page](https://clawhub.ai/maxsumrall/skills/homey) <br>
- [Homey CLI Documentation](https://maxsumrall.github.io/homeycli/) <br>
- [Output contract](docs/output.md) <br>
- [Command reference](docs/commands.md) <br>
- [Homey Developer Tools](https://tools.developer.homey.app/api/clients) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports stable JSON output for agent parsing when commands use --json.] <br>

## Skill Version(s): <br>
1.1.2 (source: release evidence, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
