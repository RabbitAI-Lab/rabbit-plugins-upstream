## Description: <br>
Control Google Nest thermostats, cameras, and doorbells via the Google Smart Device Management API using curl and jq commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mitchellbernstein](https://clawhub.ai/user/mitchellbernstein) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and smart-home operators use this skill to set up Google Smart Device Management API access and run commands for authorized Nest thermostats, cameras, doorbells, speakers, and displays. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OAuth credentials, access tokens, and config files can expose access to home devices. <br>
Mitigation: Keep tokens out of repositories and shared terminals, restrict config file permissions, and refresh or rotate credentials when needed. <br>
Risk: Commands can change device state or access cameras and streams. <br>
Mitigation: Use the skill only for devices the user owns or is authorized to control, and require explicit confirmation before camera access or device changes. <br>
Risk: The global helper symlink instruction is unsafe if the referenced helper script is missing or unreviewed. <br>
Mitigation: Avoid the /usr/local/bin symlink unless the helper script is present and reviewed; prefer local invocation or a controlled install path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mitchellbernstein/skills/google-home) <br>
- [Google Cloud Console](https://console.cloud.google.com) <br>
- [Nest Device Access registration](https://nests.google.com/frame/register-user) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance, configuration] <br>
**Output Format:** [Markdown or plain text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
