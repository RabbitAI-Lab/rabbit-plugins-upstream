## Description: <br>
Device contract for a telemetry-only room thermal sensor. Defines SmartClaws topics, payload fields, and master-agent interpretation rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eduv09](https://clawhub.ai/user/eduv09) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and SmartClaws master-agent users use this skill to interpret telemetry-only room thermal sensor readings, validate payload fields, and avoid treating the sensor as commandable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may treat stale or missing telemetry as current readings. <br>
Mitigation: Report that no fresh thermal reading is available when telemetry is missing, and use stale_relay plus stale_relay_seconds before trusting relay correlation. <br>
Risk: Agents may attempt to command a telemetry-only sensor. <br>
Mitigation: Use the contract as read-only sensor guidance and do not publish commands to this device. <br>


## Reference(s): <br>
- [SmartClaws project homepage](https://github.com/skalenetwork/smartclaws) <br>
- [ClawHub skill page](https://clawhub.ai/eduv09/skills/smartclaws-device-thermal-room-sensor) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only sensor contract; no shell commands or device-control instructions are produced.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
