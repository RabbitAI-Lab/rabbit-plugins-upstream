## Description: <br>
Control Bambu Lab 3D printers locally via MQTT without cloud dependency. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tanguyvans](https://clawhub.ai/user/tanguyvans) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and printer operators use this skill to inspect and control supported Bambu Lab printers on a trusted local network. It can report printer status and issue light, print, speed, temperature, and G-code commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad control over a physical 3D printer, including stop, temperature, and raw G-code commands. <br>
Mitigation: Install only on trusted local systems and require explicit human confirmation before any non-status command. <br>
Risk: MQTT TLS certificate verification is weakened by the implementation. <br>
Mitigation: Use the skill only on a trusted local network and avoid exposing the printer or MQTT endpoint to untrusted networks. <br>
Risk: The required config.json stores printer access details. <br>
Mitigation: Keep config.json private, do not publish it with the skill, and restrict filesystem access to trusted users. <br>


## Reference(s): <br>
- [Bambu Lab Local Control release page](https://clawhub.ai/tanguyvans/skills/bambu-local) <br>
- [OpenBambuAPI project homepage](https://github.com/Doridian/OpenBambuAPI) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell commands, JSON configuration examples, and CLI text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, paho-mqtt, local printer network access, and a private config.json containing printer connection details.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence, released 2026-01-25) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
