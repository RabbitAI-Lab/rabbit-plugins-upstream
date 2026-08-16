## Description:

Automates the WorkBuddy desktop Buddy Gas Station daily check-in on Windows using calibrated local mouse control and screenshot-based result checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

WorkBuddy users and automation agents use this skill to run or schedule the daily Buddy Gas Station check-in on a Windows desktop after calibrating click positions. The skill helps execute the bundled Python script and confirm the result with a local screenshot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill controls the local Windows mouse and may interfere with active desktop use.

Mitigation: Run it only when the desktop is idle and rely on the skill's idle-wait and visible handoff behavior before clicking.

Risk: Saved screenshots may contain visible WorkBuddy window contents.

Mitigation: Review and handle local screenshot outputs according to the user's privacy expectations before sharing or forwarding them.

Risk: Incorrect calibration can click the wrong area or produce an unreliable check-in result.

Mitigation: Complete calibration before first use and re-run calibration when screen layout, DPI, or WorkBuddy window geometry changes.

## Reference(s):

- [Coordinate calibration guide](references/calibration.md)
- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/wb-buddy-checkin)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-only workflow; execution can create local calibration JSON and screenshot files.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
