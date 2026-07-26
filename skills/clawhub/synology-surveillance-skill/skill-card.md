## Description: <br>
Controls Synology Surveillance Station cameras through the Web API for snapshots, live streams, recordings, PTZ movement, and event monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[photonixlaser-ux](https://clawhub.ai/user/photonixlaser-ux) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to configure an agent for Synology Surveillance Station camera operations, including listing cameras, capturing snapshots, generating stream URLs, managing recordings, moving PTZ cameras, and checking events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent sensitive surveillance access, including snapshots, live streams, PTZ movement, recordings, and event logs. <br>
Mitigation: Require explicit user approval before snapshots, live streams, PTZ movement, or recording changes, and restrict NAS/API access to trusted networks. <br>
Risk: Weak credential handling could expose Synology account credentials. <br>
Mitigation: Use a dedicated least-privilege Synology account, avoid admin credentials, and do not store the password in TOOLS.md or committed files. <br>
Risk: Insecure transport can expose surveillance credentials or camera data. <br>
Mitigation: Require HTTPS with a trusted certificate for Synology API access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/photonixlaser-ux/skills/synology-surveillance-skill) <br>
- [Publisher profile](https://clawhub.ai/user/photonixlaser-ux) <br>
- [Synology Surveillance Station API Reference](references/api.md) <br>
- [Official Synology Surveillance Station Web API PDF](https://global.download.synology.com/download/Document/Software/DeveloperGuide/Package/SurveillanceStation/All/enu/SurveillanceStation_Web_API.pdf) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, files, guidance] <br>
**Output Format:** [Markdown guidance with bash commands, configuration examples, API request patterns, and generated snapshot file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce camera snapshots and live-stream URLs when commands are executed against a configured Synology NAS.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
