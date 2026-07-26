## Description: <br>
Adds HTTP OTA firmware update guidance for Unihiker K10 Arduino projects, including AP/STA workflows and ESP-NOW maintenance-mode update paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rockets-cn](https://clawhub.ai/user/rockets-cn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to add wireless HTTP firmware updates to Unihiker K10 Arduino projects after an initial USB partition-table setup. It is especially relevant for installed K10 devices, ArduinoOTA network-upload failures, and ESP-NOW projects that need a temporary OTA maintenance mode. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The examples can create an unauthenticated firmware flashing path. <br>
Mitigation: Add authentication or signed firmware validation before deployment, keep OTA mode short-lived and locally triggered, and run HTTP OTA only on an isolated trusted network. <br>
Risk: Default AP credentials in example code are weak if copied into deployed devices. <br>
Mitigation: Replace defaults with strong unique credentials and avoid reusing sample access points outside controlled maintenance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rockets-cn/skills/unihiker-k10-ota) <br>
- [K10 HTTP OTA Implementation Guide](references/ota-implementation.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with Arduino C++ snippets, partition-table configuration, and shell or PowerShell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes optional Python and PowerShell uploader scripts for HTTP OTA firmware uploads.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
