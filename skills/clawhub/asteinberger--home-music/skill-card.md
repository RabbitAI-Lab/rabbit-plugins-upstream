## Description: <br>
Control whole-house music scenes combining Spotify playback with Airfoil speaker routing. Quick presets for morning, party, chill modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asteinberger](https://clawhub.ai/user/asteinberger) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to trigger predefined home music scenes that control Spotify playback, Airfoil speaker routing, and speaker volume from concise commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Music scenes can change local playback, speaker routing, and volume if invoked accidentally or without reviewing the preset values. <br>
Mitigation: Review speaker names, playlist URIs, and volume levels before use, and invoke explicit commands such as home-music party or home-music off. <br>
Risk: The install instructions use a sudo symlink into /usr/local/bin, which broadens command availability on the host. <br>
Mitigation: Use a user-local bin directory instead when global command access is not required. <br>
Risk: The script depends on a hardcoded spotify-applescript path and local macOS applications being present. <br>
Mitigation: Confirm the spotify-applescript path and verify Spotify and Airfoil are running before executing scenes. <br>


## Reference(s): <br>
- [Spotify](https://spotify.com) <br>
- [Airfoil](https://rogueamoeba.com/airfoil/) <br>
- [Home Music on ClawHub](https://clawhub.ai/asteinberger/skills/home-music) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local macOS command guidance for Spotify and Airfoil scenes; no structured API response is emitted.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and artifact documentation) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
