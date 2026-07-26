## Description: <br>
Control Apple TV via pyatv for playback, navigation, volume, app launching, power control, and checking what is playing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucakaufmann](https://clawhub.ai/user/lucakaufmann) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to let an agent operate a configured Apple TV through pyatv, including playback, navigation, volume, app launch, power, discovery, and now-playing checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Apple TV state through playback, navigation, volume, app launch, and power commands. <br>
Mitigation: Install it only when agent-driven Apple TV control is intended, and require confirmation before disruptive device-control actions. <br>
Risk: The skill uses local Apple TV credentials stored in appletv.json. <br>
Mitigation: Protect the credential file and limit access to users and agents that are allowed to control the device. <br>
Risk: The skill depends on the pyatv command-line tooling installed in the user environment. <br>
Mitigation: Verify the pyatv install source and use a supported Python version before deployment. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local Apple TV control commands and status text using a configured pyatv setup.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
