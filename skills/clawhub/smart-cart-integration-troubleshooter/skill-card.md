## Description:

Diagnose and document assembly, calibration, deployment, communication, camera, motion, and obstacle-avoidance problems for a lightweight OpenClaw smart cart using a 12V battery, a multi-channel servo controller, three ST3215 servos, omnidirectional wheels, and a USB camera.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jason15336804](https://clawhub.ai/user/jason15336804)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, integrators, and operators use this skill to triage OpenClaw smart-cart faults, sequence safe hardware checks, isolate likely root causes, and produce repeatable diagnostic reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hardware troubleshooting can involve powered motion, batteries, wiring, servos, and controller resets.

Mitigation: Follow the skill's safety gates: stop motion, isolate the 12V supply before wiring changes, secure or lift the chassis for wheel tests, keep hands clear, and stop for swelling, overheating, smoke, damaged insulation, short-circuit signs, uncontrolled motion, or repeated resets.

Risk: Missing controller, port, protocol, calibration, camera index, or motion-mapping details can lead to incorrect tests on a real cart.

Mitigation: Verify those values from trusted project documentation before hardware testing, and keep unspecified values labeled as unknown rather than inventing them.

Risk: Reports use Chinese section labels by default, which may not match every installer's expected locale.

Mitigation: Edit or override the report template labels before deployment when English or another locale is required.

## Reference(s):

- [Project Baseline](artifact/references/project-baseline.md)
- [Diagnostic Matrix](artifact/references/diagnostic-matrix.md)
- [Sample Diagnosis](artifact/examples/sample-diagnosis.md)
- [ClawHub Skill Page](https://clawhub.ai/jason15336804/skills/smart-cart-integration-troubleshooter)
- [Publisher Profile](https://clawhub.ai/user/jason15336804)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown diagnostic report with optional checklist command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Chinese report section labels by default; optional checklist generation requires python3.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
