## Description:

Controls Chromecast-compatible devices on a local network with catt for device discovery, media casting, playback control, seeking, volume, queue management, subtitles, and device aliases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Chromecast-style devices on a trusted local network for home entertainment, meeting-room casting, and multi-device media control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run local shell commands and discover or control Chromecast-compatible devices on the user's LAN.

Mitigation: Use it only for explicit Chromecast or catt tasks on trusted networks, and confirm the target device and command before execution.

Risk: Casting selected local files or URLs can expose media content on an external device.

Mitigation: Verify local file paths, URLs, subtitles, and destination devices before casting, and avoid public or untrusted networks.

Risk: Device alias and default-device operations can modify catt configuration under the user's home directory.

Mitigation: Review alias/default changes before applying them and inspect the catt configuration if device routing behaves unexpectedly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/chromecast-control)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include device names, local file paths, URLs, playback status, and catt configuration guidance.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
