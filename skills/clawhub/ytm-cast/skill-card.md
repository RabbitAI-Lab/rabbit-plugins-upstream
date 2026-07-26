## Description: <br>
Download music from YouTube/YouTube Music and stream to Chromecast via Home Assistant with a CLI toolset, local web server integration, configuration wizard, and playback controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aidanthebandit](https://clawhub.ai/user/aidanthebandit) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Home Assistant and Chromecast users can use this skill to download YouTube or YouTube Music media locally, host it on a trusted local network, and control playback through Home Assistant media players. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a Home Assistant long-lived access token in a local configuration file. <br>
Mitigation: Use a dedicated or least-privilege token, keep the configuration file private, and revoke the token if it is exposed. <br>
Risk: The skill runs a local media web server for Chromecast playback. <br>
Mitigation: Run the server only on trusted local networks and stop or restrict it when casting is not needed. <br>
Risk: The skill relies on external command-line tools and referenced scripts to download and cast media. <br>
Mitigation: Install only when the external scripts and tools are trusted, and review generated commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aidanthebandit/skills/ytm-cast) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/aidanthebandit) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce setup, download, server, casting, playback, and troubleshooting commands for local execution.] <br>

## Skill Version(s): <br>
6.0.0 (source: server release and artifact/SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
