## Description:

Helps engineers profile, check, and read industrial sensors over Modbus, IO-Link, serial ASCII, and MQTT/Sparkplug, reporting units, accuracy, and verification status before collection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Industrial automation engineers use this skill to draft and check sensor profiles, test a channel reading, and assess whether readings are ready for collection. Operators review and apply configuration changes themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing MQTT messages can change connected devices or workflows.

Mitigation: Use read-only sensor onboarding by default; keep the separate mqtt_publish approval gate enabled and review each publish.

Risk: Unverified sensor profiles or incorrect units and decoding can produce misleading readings.

Mitigation: Have an engineer confirm device identity and profile details, check the profile, and test one channel before collecting data.

Risk: Connecting to industrial sensor infrastructure outside the intended environment can expose operational systems.

Mitigation: Install only where access to the intended Modbus, IO-Link, serial, or MQTT infrastructure is expected.

## Reference(s):

- [iaiops-sensor on ClawHub](https://clawhub.ai/zw008/skills/iaiops-sensor)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance, Shell commands]

**Output Format:** [Markdown with sensor readings, profile drafts, configuration examples, and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Readings include units, accuracy bands, and profile verification status; invalid readings are reported as gaps.]

## Skill Version(s):

0.31.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
