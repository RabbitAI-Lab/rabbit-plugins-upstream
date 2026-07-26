## Description: <br>
Controls Chromecast devices through catt for local device discovery, media casting, and basic playback controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to have an agent propose and run catt commands for Chromecast discovery, casting URLs or local media, and playback control on a trusted local network. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The activation instructions incorrectly point to database and SQL tasks, which could cause unrelated requests to trigger Chromecast-related local network or media-control commands. <br>
Mitigation: Review and correct trigger text so the skill is invoked only for Chromecast control tasks. <br>
Risk: LAN scanning and casting local files can affect nearby devices or expose local media through temporary HTTP serving. <br>
Mitigation: Run only on trusted networks, confirm before scanning or casting local files, and avoid serving sensitive local media. <br>
Risk: Commands may control the wrong Chromecast device when multiple devices are present. <br>
Mitigation: Confirm the target device and use explicit device selection before playback, volume, or stop commands. <br>


## Reference(s): <br>
- [Chromecast Control Tool Free on ClawHub](https://clawhub.ai/thcjp/skills/chromecast-control-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires tool-use capability and a local environment with Python, catt, and network access to Chromecast devices.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
