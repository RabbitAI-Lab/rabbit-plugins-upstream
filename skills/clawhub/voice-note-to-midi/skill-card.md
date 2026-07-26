## Description: <br>
Convert voice notes, humming, and melodic audio recordings to quantized MIDI files using ML-based pitch detection and intelligent post-processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[danbennettuk](https://clawhub.ai/user/danbennettuk) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, musicians, and producers use this skill to convert clear monophonic voice notes, humming, singing, or existing MIDI into quantized MIDI files for editing in a DAW. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow installs Python dependencies and may fetch or rely on a Basic Pitch hum2midi script. <br>
Mitigation: Review the hum2midi script before downloading it manually and pin or review Python dependencies on sensitive machines. <br>
Risk: The setup flow can add ~/melody-pipeline to PATH, which changes future command lookup behavior. <br>
Mitigation: Accept the PATH change only when that behavior is intended; remove the added export line from the shell profile to undo it. <br>


## Reference(s): <br>
- [Basic Pitch](https://github.com/spotify/basic-pitch) <br>
- [librosa HPSS](https://librosa.org/doc/latest/generated/librosa.decompose.hpss.html) <br>
- [Krumhansl-Kessler Key Profiles](https://rnhart.net/articles/key-finding/) <br>
- [Voice Note To Midi on ClawHub](https://clawhub.ai/danbennettuk/skills/voice-note-to-midi) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and command-line options] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides local setup and use of an audio-to-MIDI pipeline that produces standard MIDI files.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
