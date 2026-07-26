## Description: <br>
Chromecast Control helps an agent use catt to discover and control local-network casting devices, cast media, manage playback, adjust volume, handle queues, load subtitles, and manage device aliases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to operate Chromecast-compatible devices on a local network for home entertainment, meeting-room casting, and multi-device media management. It is intended for workflows that need device discovery, media casting, playback control, volume changes, queue management, subtitles, and local device alias configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local-network discovery and casting can expose device names, IP addresses, media URLs, or local file paths in shared homes or offices. <br>
Mitigation: Confirm the network, target device, and media source before scanning or casting, especially in shared environments. <br>
Risk: The skill can execute catt commands that affect real playback, volume, queues, and local catt configuration. <br>
Mitigation: Review proposed commands before execution and verify the target device before changing playback state or aliases. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/chromecast-control) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and execution summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include device names, IP addresses, media URLs, local file paths, playback status, volume settings, and catt command output.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
