## Description: <br>
Linux GUI Control lets an agent operate X11/GNOME desktop applications with xdotool, wmctrl, dogtail, and screenshots for window management, input simulation, and UI hierarchy inspection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dreamtraveler13](https://clawhub.ai/user/dreamtraveler13) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent interact with non-browser Linux desktop applications when command-line or browser automation is insufficient. It supports targeting windows, inspecting accessible UI trees, sending mouse and keyboard input, and capturing screenshots for visual tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent direct control over a local Linux desktop, including mouse input, keyboard input, window activation, and screenshots. <br>
Mitigation: Use it only when desktop operation is intended; close or hide sensitive windows, verify the target window, and avoid exposing passwords or private data before execution. <br>
Risk: Some workflows may kill or restart applications to enable accessibility inspection. <br>
Mitigation: Save work and confirm the target application before running commands that restart or terminate a process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dreamtraveler13/skills/guicountrol) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that interact with the active Linux desktop session.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
