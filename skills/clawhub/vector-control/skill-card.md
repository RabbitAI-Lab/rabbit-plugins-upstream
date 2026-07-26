## Description: <br>
Control a Vector robot via Wirepod’s local HTTP API on the same network. Use when you need to move Vector, tilt head/lift, speak text, capture camera frames, or run patrol/explore routines from the Pi/Wirepod host. Includes a CLI helper script and endpoint reference. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dbeadle1](https://clawhub.ai/user/dbeadle1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and robot operators use this skill to control a local Vector robot through Wirepod for movement, speech, audio playback, camera snapshots, patrols, and exploration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move a physical Vector robot through patrol, explore, wheel, head, and lift commands. <br>
Mitigation: Supervise movement, use short timed moves, keep the robot in a clear area, and release behavior control when finished or if manual intervention is needed. <br>
Risk: Camera snapshots can capture local surroundings and save image data to user-selected paths. <br>
Mitigation: Capture only in appropriate locations, choose snapshot paths deliberately, and handle saved images as potentially sensitive data. <br>
Risk: Audio playback and speech can output arbitrary text or selected media through the robot speaker. <br>
Mitigation: Review text and media before playback, avoid untrusted media files, and keep use appropriate for nearby people. <br>
Risk: Wirepod HTTP control endpoints can affect the robot if exposed beyond localhost or a trusted private network. <br>
Mitigation: Keep Wirepod bound to localhost or trusted private networks and avoid exposing the API to untrusted hosts. <br>


## Reference(s): <br>
- [Wirepod HTTP API endpoint reference](artifact/references/wirepod-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/dbeadle1/skills/vector-control) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and Python CLI usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local MJPG camera snapshot files and converted audio during CLI use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
