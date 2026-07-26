## Description: <br>
Control Apple TV, HomePod, and AirPlay devices via pyatv for scanning, streaming, playback, volume, and navigation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaronn](https://clawhub.ai/user/aaronn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to discover, pair with, and control local Apple TV, HomePod, and AirPlay devices. It helps agents propose or run atvremote commands for playback, volume, navigation, streaming, device information, and output device management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control local Apple media devices, including playback, volume, power, navigation, app launch, and output routing. <br>
Mitigation: Use with trusted prompts and review commands before execution; target only intended devices by name, IP address, or identifier. <br>
Risk: Streaming commands can play local files or remote URLs on media devices. <br>
Mitigation: Stream only intended local files or trusted URLs. <br>
Risk: Pairing credentials may be stored in ~/.pyatv.conf. <br>
Mitigation: Protect ~/.pyatv.conf and avoid exposing it in prompts, logs, or shared artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaronn/skills/apple-media) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands assume pyatv/atvremote is installed and that the target Apple media device is discoverable or paired when required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
