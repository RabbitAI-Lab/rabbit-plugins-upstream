## Description: <br>
Control whole-house music scenes combining Spotify playback with Airfoil speaker routing. Quick presets for morning, party, chill modes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Home users and automation authors on macOS use this skill to start, stop, and inspect predefined Spotify and Airfoil music scenes across local speakers. It supports both terminal use and Python automation for focus, chill, morning, party, and off scenes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger phrases and local command execution could cause unintended Spotify or speaker-routing actions. <br>
Mitigation: Review before installing and invoke the skill explicitly, such as by naming the skill or requesting a specific scene. <br>
Risk: HOME_MUSIC_SCRIPT or PATH could redirect the Python wrapper to an unexpected executable. <br>
Mitigation: Check HOME_MUSIC_SCRIPT and PATH before use and keep the intended home-music script in a trusted location. <br>
Risk: Automations can leave music playing after a workflow fails or exits early. <br>
Mitigation: Use the provided stop_music or off command in a finally block for automation workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/home-music) <br>
- [Spotify](https://spotify.com) <br>
- [Airfoil](https://rogueamoeba.com/airfoil/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown documentation with inline shell commands and Python snippets; runtime output is terminal text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires macOS with Spotify Desktop, Airfoil, and the referenced spotify-applescript helper available.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata and artifact documentation) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
