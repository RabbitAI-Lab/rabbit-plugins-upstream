## Description: <br>
Control WiiM audio devices (play, pause, stop, next, prev, volume, mute, play URLs, presets). Use when the user wants to control music playback, adjust volume, discover WiiM/LinkPlay speakers on the network, or play audio from a URL on a WiiM device. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[geodeterra](https://clawhub.ai/user/geodeterra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers can use this skill to ask an agent for WiiM CLI guidance and shell commands to discover and control WiiM or LinkPlay speakers on a local network. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs users to install and run the external wiim-cli package. <br>
Mitigation: Install it only from a package source you trust and review the package before using it in sensitive environments. <br>
Risk: Auto-discovery can target the wrong speaker when multiple WiiM or LinkPlay devices are present. <br>
Mitigation: Use the --host option to target a specific device IP address on multi-device networks. <br>
Risk: Playing an untrusted media URL can send a device to retrieve unwanted or unsafe content. <br>
Mitigation: Use play-url only with trusted direct audio URLs. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target local-network WiiM or LinkPlay devices and may include host addresses, volume values, preset numbers, and direct audio URLs.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
