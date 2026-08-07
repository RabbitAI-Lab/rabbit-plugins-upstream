## Description: <br>
Chromecast Control helps an agent guide local `catt` commands for discovering Chromecast-compatible devices, casting media, controlling playback, adjusting volume, managing queues, loading subtitles, and configuring device aliases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and end users can use this skill to control local-network casting devices through `catt` for home entertainment, meeting room display, and multi-device media management workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides an agent to run `catt` commands that can control casting devices on the local network. <br>
Mitigation: Confirm the target device before casting or changing playback, especially on shared networks. <br>
Risk: Casting private media or browser content on shared or untrusted networks can expose sensitive content to unintended viewers. <br>
Mitigation: Use trusted networks and avoid private media unless the display device and audience are known. <br>
Risk: Device aliases and default-device changes persist in `~/.config/catt/catt.cfg`. <br>
Mitigation: Review alias and default-device settings after use, and remove or reset them with the documented delete/default-reset commands when no longer needed. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command examples, troubleshooting guidance, and local device configuration notes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
