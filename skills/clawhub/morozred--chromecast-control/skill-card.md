## Description: <br>
Control Chromecast devices on your local network - discover, cast media, control playback, manage queues, and save/restore states <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[morozred](https://clawhub.ai/user/morozred) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to have an agent discover and control Chromecast or Google Cast devices on a local network, including casting media, controlling playback and volume, managing YouTube queues, and saving or restoring playback state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cast media or change playback on Chromecast and Google Cast devices on the local network, including shared devices. <br>
Mitigation: Target devices explicitly and confirm the intended device before casting, stopping playback, or changing volume. <br>
Risk: Saved playback state may reveal or replay prior media, position, or volume settings. <br>
Mitigation: Use save and restore only when prior playback state is appropriate to preserve and replay. <br>


## Reference(s): <br>
- [catt project homepage](https://github.com/skorokithakis/catt) <br>
- [Control Chromecast on ClawHub](https://clawhub.ai/morozred/skills/chromecast-control) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target local-network Chromecast or Google Cast devices through the catt CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
