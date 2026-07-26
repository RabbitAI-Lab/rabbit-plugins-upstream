## Description: <br>
Send and receive messages via Meshtastic LoRa mesh network. Use for off-grid messaging, mesh network status, reading recent mesh messages, or sending texts via LoRa radio. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lukevr](https://clawhub.ai/user/lukevr) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to connect agents to Meshtastic-compatible LoRa mesh nodes for off-grid messaging, mesh status checks, message monitoring, alerts, digests, and optional MCP integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bridge can publish location and device data externally through map reporting. <br>
Mitigation: Disable map publishing before use and require explicit approval before broadcasting position or forcing a map report. <br>
Risk: The skill logs mesh messages and node positions under /tmp, which may be readable or short-lived depending on host configuration. <br>
Mitigation: Protect or relocate the log and cache paths before running the bridge on shared or persistent systems. <br>
Risk: Setup guidance includes broad serial-device permissions. <br>
Mitigation: Use a restricted device group or udev rule instead of broad chmod access. <br>
Risk: MCP and socket tools expose high-impact radio and device operations, including position broadcasts and device reboot. <br>
Mitigation: Require explicit user approval before sending alerts, broadcasting position, forwarding digests externally, or rebooting the connected device. <br>


## Reference(s): <br>
- [Meshtastic Setup Guide](references/SETUP.md) <br>
- [Claude Desktop MCP Config Example](references/claude_desktop_config.json) <br>
- [Meshtastic Docs](https://meshtastic.org/docs/) <br>
- [Meshtastic MQTT Integration](https://meshtastic.org/docs/configuration/module/mqtt/) <br>
- [Meshtastic Hardware Options](https://meshtastic.org/docs/hardware/) <br>
- [Meshtastic Python CLI](https://meshtastic.org/docs/software/python/cli/) <br>
- [Meshtastic Community Software](https://meshtastic.org/docs/software/community-software/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON socket examples, configuration snippets, and Python/MCP integration code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operational guidance for local USB hardware, localhost socket commands, MQTT bridge behavior, local log files, and optional MCP tools.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
