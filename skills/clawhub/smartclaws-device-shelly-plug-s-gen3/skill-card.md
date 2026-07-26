## Description: <br>
Device contract for Shelly Plug S Gen3 that defines SmartClaws topics, payloads, local Shelly RPC methods, and safety rules for bridge and master agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eduv09](https://clawhub.ai/user/eduv09) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators using SmartClaws use this skill to describe how bridge and master agents should read telemetry from, and optionally send commands to, a Shelly Plug S Gen3 smart plug. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Command-enabled use can cause a bridge agent to turn a physical relay on or off. <br>
Mitigation: Enable command mode only for a Shelly plug and SmartClaws channels you control, and confirm the registered device name, command channel, and setup authority before sending commands. <br>
Risk: Incorrect credential handling could expose Shelly authentication details. <br>
Mitigation: Provide credentials through the configured path or mechanism and avoid printing credentials in agent output or logs. <br>
Risk: Misusing telemetry can lead to incorrect decisions, such as treating plug internal temperature as room temperature or replaying old commands. <br>
Mitigation: Use the defined telemetry fields as scoped device readings, check recent telemetry and command state before publishing, and persist handled command offsets in bridge state. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/eduv09/skills/smartclaws-device-shelly-plug-s-gen3) <br>
- [SmartClaws Homepage](https://github.com/skalenetwork/smartclaws) <br>
- [Shelly Plug S Gen3 Docs](https://shelly-api-docs.shelly.cloud/gen2/Devices/Gen3/ShellyPlugSG3) <br>
- [Shelly Switch Component RPC](https://shelly-api-docs.shelly.cloud/gen2/Components/FunctionalComponents/Switch/) <br>
- [Shelly RPC Protocol](https://shelly-api-docs.shelly.cloud/gen2/General/RPCProtocol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defines SmartClaws topics, payload schemas, Shelly RPC mappings, and safety constraints; it does not install SmartClaws or register a device.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
