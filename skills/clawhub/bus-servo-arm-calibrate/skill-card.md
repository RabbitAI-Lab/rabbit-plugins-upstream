## Description:

Calibrate a multi-DOF bus-servo robotic arm when servo position readback is unavailable and grasp success must be confirmed visually.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sharinchan233](https://clawhub.ai/user/sharinchan233)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, roboticists, and operators use this skill to calibrate tabletop bus-servo arms for reliable slot pickup and tray placement when servo angle readback is unavailable. It guides channel mapping, lift-hold-confirm grasp tuning, placement testing, parameter storage, and diagnosis of release failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect servo channel direction or motion-limit assumptions can cause failed grasps, table contact, or unintended arm movement.

Mitigation: Verify channel-to-joint mapping, joint directions, and safe motion limits on the target hardware before tuning slots.

Risk: Running grasp and placement motions without visual confirmation can hide whether failure occurred during pickup, lift, or release.

Mitigation: Use the lift-hold-confirm loop and keep manual control and visual confirmation during movement.

## Reference(s):

- [Worked example](artifact/reference.md)
- [ClawHub skill page](https://clawhub.ai/sharinchan233/skills/bus-servo-arm-calibrate)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and calibration parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Human visual confirmation is required during hardware movement; no structured machine-readable output is produced by the skill itself.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
