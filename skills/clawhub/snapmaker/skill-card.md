## Description: <br>
Monitor and control Snapmaker 3D printers, including Snapmaker U1 printers using Moonraker/Klipper, for status checks, temperatures, print progress, filament data, and print controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucakaufmann](https://clawhub.ai/user/lucakaufmann) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, makers, and printer operators use this skill to inspect Snapmaker printer state and issue common Moonraker/Klipper print-control commands from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This skill can directly control a physical 3D printer, including pause, resume, cancel, and raw G-code commands. <br>
Mitigation: Configure it only for the intended printer and require explicit user approval before running mutating commands. <br>
Risk: Raw G-code can have physical effects on printer motion, temperature, or print state. <br>
Mitigation: Avoid the raw G-code feature unless the exact command and its physical effect have been personally verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lucakaufmann/skills/snapmaker) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and plain-text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local printer IP configuration or SNAPMAKER_IP and SNAPMAKER_PORT environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
