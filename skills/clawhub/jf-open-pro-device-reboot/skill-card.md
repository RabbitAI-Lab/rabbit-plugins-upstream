## Description: <br>
JFTech device reboot skill for remotely rebooting JF devices and, where supported, shutting them down. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and device operators use this skill to send reboot or shutdown commands to bound, online JF devices through the JF OpenAPI after configuring required credentials. <br>

### Deployment Geography for Use: <br>
China, Asia, Europe, and North America, based on the documented JF API endpoints. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can reboot or shut down remote devices using configured credentials without requiring confirmation by default. <br>
Mitigation: Require an explicit user confirmation step before invoking reboot or shutdown actions. <br>
Risk: Credentials and device tokens are used to call the JF API, and endpoint selection is configurable. <br>
Mitigation: Use only intended JF credentials and set JF_ENDPOINT only to a trusted documented JF API host. <br>


## Reference(s): <br>
- [JFTech Open Platform documentation](https://docs.jftech.com) <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-device-reboot) <br>
- [JFTech publisher profile](https://clawhub.ai/user/jftech) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and command output text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires JF credentials, a device token, and a trusted JF API endpoint before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
