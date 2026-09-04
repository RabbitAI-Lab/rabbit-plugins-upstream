## Description:

iaiops-building helps agents read building automation data over BACnet/IP, Modbus, IO-Link, MQTT, and BAS controller REST layers, run facility diagnostics, and prepare dry-run, MOC-gated commands for authorized non-life-safety controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Facility operators, controls engineers, and developers use this skill to inspect building automation networks, collect point and trend evidence, diagnose comfort, alarm, downtime, and data-quality issues, and stage tightly controlled operational changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Building automation write tools can affect operating equipment, including setpoints and outputs.

Mitigation: Install only in authorized building-automation environments; keep dry-run defaults and MOC approval enabled before any write.

Risk: BACnet, BAS, and MQTT command paths are operationally sensitive and can be misused with overly broad credentials.

Mitigation: Use scoped credentials from the secret store and avoid plaintext credential parameters.

Risk: Connection to life-safety systems could create high-impact operational risk.

Mitigation: Avoid life-safety systems unless documented refusal behavior and site controls have been validated; the artifact states life-safety BAS command targets are refused before network dispatch.

Risk: Live device behavior for some write, COV, trend, master, and vendor-controller paths may require site validation.

Mitigation: Follow read-first workflows, validate point mappings and protocol readiness, and treat unverified live paths as requiring local commissioning review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-building)
- [ClawHub publisher profile](https://clawhub.ai/user/zw008)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured tool plans, command examples, configuration snippets, diagnostic findings, and operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run and MOC approval steps, cited readings, bounded scan results, and refusal messages for life-safety commands.]

## Skill Version(s):

0.27.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
