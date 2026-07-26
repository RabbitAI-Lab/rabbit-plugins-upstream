## Description: <br>
Manage Plex Media Server with optional Nvidia Shield ADB device management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[grewingm](https://clawhub.ai/user/grewingm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and media-server operators use this skill to discover and configure Plex Media Server, search libraries with rich metadata, monitor sessions, refresh libraries, and optionally manage an Nvidia Shield device over ADB. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The Plex token grants full account and server access if the local config file or machine is exposed. <br>
Mitigation: Use the skill only on a trusted machine, keep the config file private, and revoke or rotate the token after exposure. <br>
Risk: Optional Shield ADB commands can reboot the device or restart Plex. <br>
Mitigation: Enable ADB features only when device control is intended and restrict use to a trusted local network. <br>


## Reference(s): <br>
- [Plex Web](https://app.plex.tv) <br>
- [Plex Web Desktop](https://app.plex.tv/desktop) <br>
- [ClawHub skill page](https://clawhub.ai/grewingm/skills/plex-server) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; CLI commands return JSON or formatted text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Stores local Plex and optional Shield configuration in a private config file.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
