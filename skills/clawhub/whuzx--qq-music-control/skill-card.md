## Description: <br>
Controls playback, track navigation, shuffle behavior, volume, launch, and status checks for the macOS QQ Music client. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whuzx](https://clawhub.ai/user/whuzx) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Mac users and agent operators use this skill to control the local QQ Music desktop app through natural-language playback, volume, launch, and status requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can start QQ Music, bring it to the foreground, skip tracks, toggle playback, and change media volume on the user's Mac. <br>
Mitigation: Install it only where local QQ Music control is intended, and require confirmation or narrow triggers for disruptive playback and volume commands. <br>
Risk: The implementation depends on macOS MediaRemote private framework behavior and a locally installed QQ Music app. <br>
Mitigation: Use it on macOS machines with QQ Music and Python 3 installed, and verify behavior after macOS or QQ Music updates. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, text, guidance] <br>
**Output Format:** [Markdown guidance with Python command examples and terminal text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands run locally on macOS and may change QQ Music playback or media volume.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
