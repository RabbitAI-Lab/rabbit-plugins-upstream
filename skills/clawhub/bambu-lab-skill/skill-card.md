## Description: <br>
Controls and monitors Bambu Lab 3D printers over local-network MQTT for status checks, print progress, pause/resume/stop commands, lighting, fan control, and completion or error notifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[photonixlaser-ux](https://clawhub.ai/user/photonixlaser-ux) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, makers, and operators use this skill to check and control supported Bambu Lab printers in LAN mode from an agent session. It is intended for local printer monitoring, print-state reporting, basic printer commands, and completion or error notifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill ships with hardcoded printer host, serial number, and access code values. <br>
Mitigation: Replace bundled connection values with the user's own secure configuration before installation or use, and rotate the access code if the included values were ever real. <br>
Risk: The MQTT client configuration weakens TLS verification. <br>
Mitigation: Use the skill only on a trusted local network and review TLS settings before relying on it for sensitive printer environments. <br>
Risk: Printer-control commands can pause, resume, stop, or otherwise affect an active physical print job. <br>
Mitigation: Confirm printer identity and job state before sending control commands, especially stop, pause, fan, light, or notification-monitoring commands. <br>


## Reference(s): <br>
- [Bambu Lab MQTT API Reference](references/mqtt.md) <br>
- [Bambu Lab Wiki](https://wiki.bambulab.com/en/home) <br>
- [bambu-mqtt documentation](https://github.com/Doridian/bambu-mqtt) <br>
- [ClawHub skill page](https://clawhub.ai/photonixlaser-ux/skills/bambu-lab-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and text status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke local MQTT command scripts that read printer status, send printer-control commands, or produce notification text.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
