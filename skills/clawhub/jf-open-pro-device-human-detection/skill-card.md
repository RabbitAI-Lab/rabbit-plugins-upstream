## Description: <br>
Supports JF device human detection and PTZ human tracking configuration, including enablement, sensitivity, and return-time settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to query and update human detection alarms and PTZ human tracking behavior on authorized JF camera devices through the JF OpenAPI. <br>

### Deployment Geography for Use: <br>
China, Asia, Europe, and North America through the documented JF regional API hosts. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change surveillance and PTZ tracking settings on JF cameras. <br>
Mitigation: Install and run it only for cameras the operator owns or is authorized to administer, and review local privacy, consent, and camera-motion policies before enabling detection or tracking. <br>
Risk: The skill sends signed device requests using environment-provided credentials and a configurable API host. <br>
Mitigation: Keep device credentials scoped and protected, avoid exposing them broadly to agents, and set JF_ENDPOINT only to documented JF regional API hosts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-device-human-detection) <br>
- [JF Open Platform documentation](https://docs.jftech.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI command examples and plain-text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JF OpenAPI credentials, a device token, an online bound device, and a documented JF regional API endpoint.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
