## Description: <br>
Operate and troubleshoot BambuLab printers with the bambu-cli, including status and watch workflows, print control, files, camera, G-code, AMS, calibration, motion, fans, lights, configuration, and diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobiasbischoff](https://clawhub.ai/user/tobiasbischoff) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and 3D printer users use this skill to translate BambuLab printer tasks into safer bambu-cli commands with correct flags, output formats, and confirmation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can affect a physical printer or active print, especially raw G-code, --no-check, temperature changes, motion, calibration, reboot, file deletion, and print stop actions. <br>
Mitigation: Review every command before execution and require explicit confirmation for destructive or hardware-affecting actions. <br>
Risk: Printer access codes can be exposed if passed directly in command flags or logs. <br>
Mitigation: Use access-code files or stdin as documented, protect access-code files, and install bambu-cli only from a trusted source. <br>


## Reference(s): <br>
- [bambu-cli command reference](artifact/references/commands.md) <br>
- [ClawHub skill page](https://clawhub.ai/tobiasbischoff/skills/bambu-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and concise operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend JSON or plain key=value output flags for scripting when appropriate.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
