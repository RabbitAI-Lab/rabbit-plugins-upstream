## Description: <br>
macOS CLI tool for recording audio (microphone), screen (video/screenshot), and camera (video/photo) from the terminal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[atacan](https://clawhub.ai/user/atacan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, engineers, and terminal-based agents use this skill to list macOS capture devices and run consented microphone, screen, camera, screenshot, or photo capture commands with controlled duration and output paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Recording microphone, camera, or screen content can capture sensitive personal, workplace, or credential information. <br>
Mitigation: Ask for explicit user consent before recording, confirm what will be captured and for how long, and prefer short durations with narrow targets such as a selected window, display, or region. <br>
Risk: Captured media may be saved to an unintended location or retained longer than needed. <br>
Mitigation: Choose output paths deliberately, use temporary locations when appropriate, and remove recordings that are no longer needed. <br>
Risk: The tool requires trust in a third-party Homebrew tap and macOS capture permissions. <br>
Mitigation: Install only when the publisher and tap are trusted, and revoke microphone, camera, or screen permissions when they are no longer required. <br>


## Reference(s): <br>
- [Audio command reference](references/audio.md) <br>
- [Screen command reference](references/screen.md) <br>
- [Camera command reference](references/camera.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline bash commands and option guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The underlying CLI can emit plain paths or JSON and can create audio, video, screenshot, or photo files.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
