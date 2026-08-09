## Description: <br>
Automates the WorkBuddy desktop client's daily Buddy gas-station check-in on Windows by clicking the profile, Buddy gas-station, and claim controls, then using screenshot grayscale checks to confirm completion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noaheleven](https://clawhub.ai/user/noaheleven) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and automation users use this skill to run a Windows desktop check-in flow for WorkBuddy daily points after calibrating screen coordinates. Developers can use the included guidance to configure manual or scheduled execution and inspect the resulting screenshot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs Windows desktop automation that clicks inside WorkBuddy and saves local screenshots. <br>
Mitigation: Run it manually first, review the saved screenshot, and enable scheduling only after the calibrated flow behaves as expected. <br>
Risk: If a neighboring desktop-control-win skill is installed, the script can run its PowerShell screenshot helper. <br>
Mitigation: Inspect that helper before use, remove it if not needed, or only run this skill in an environment where the neighboring skill is trusted and unmodified. <br>
Risk: Uncalibrated or stale coordinates can click the wrong locations or report failed check-ins. <br>
Mitigation: Run the provided calibration flow before real use and recalibrate after screen layout, DPI, or WorkBuddy UI changes. <br>


## Reference(s): <br>
- [Coordinate calibration guide](references/calibration.md) <br>
- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/wb-buddy-checkin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; runtime execution writes PNG screenshots and optional JSON calibration data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Windows-only desktop automation; produces local checkin_result.png and may produce calibrate.json during calibration.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
