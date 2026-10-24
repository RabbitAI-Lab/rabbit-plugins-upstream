## Description:

Guides industrial sensor profile drafting, validation, one-time readings, and collection across Modbus, IO-Link, serial, and MQTT/Sparkplug connections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and industrial engineers use this skill to describe and check sensor channels, read measurements with units and verification status, and prepare collection without automatically changing configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The available MQTT publish operation can write to connected infrastructure.

Mitigation: Use it only with explicit approval through the change-control gate; do not publish merely to test a sensor.

Risk: Unverified sensor profiles or incorrect units and decoding can produce misleading measurements.

Mitigation: Have a human verify the device, profile, units, and configuration before collection; retain verification status and exclude invalid readings.

## Reference(s):

- [iaiops-sensor ClawHub release](https://clawhub.ai/zw008/skills/iaiops-sensor)

## Skill Output:

**Output Type(s):** [Text, Configuration guidance, Shell commands]

**Output Format:** [Markdown with configuration and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sensor readings include units, accuracy bands, and profile verification status; invalid readings are identified as gaps.]

## Skill Version(s):

0.32.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
