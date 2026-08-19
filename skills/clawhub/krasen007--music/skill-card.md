## Description: <br>
Control AIMP music player via native command-line switches for play, pause, stop, next, and previous track actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[krasen007](https://clawhub.ai/user/krasen007) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to let an agent provide Windows command-line controls for AIMP playback. It is useful when the user wants direct media playback actions such as play, pause, stop, next track, or previous track. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Playback commands can immediately change the user's active AIMP playback state. <br>
Mitigation: Use the skill only in contexts where direct media control is expected and acceptable to the user. <br>
Risk: Commands fail or have no effect if AIMP is not installed or not running on Windows. <br>
Mitigation: Check that AIMP is installed and running before issuing playback commands. <br>


## Reference(s): <br>
- [AIMP homepage](https://aimp.ru) <br>
- [AIMP-player ClawHub listing](https://clawhub.ai/krasen007/skills/music) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are intended for Windows systems with AIMP installed and running.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
