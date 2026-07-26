## Description: <br>
Generates spoken audio from text using a local or remote Kokoro TTS endpoint when a user asks for text-to-speech, a voice message, or something to be said. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edkief](https://clawhub.ai/user/edkief) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to convert user-provided text into MP3 speech audio through a configured Kokoro TTS endpoint, with optional voice and speed parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User text is sent to the configured Kokoro endpoint. <br>
Mitigation: Use the localhost default or another trusted endpoint, and avoid sending secrets or sensitive private text to untrusted remote servers. <br>
Risk: Generated audio files accumulate in the local media directory. <br>
Mitigation: Review and clean up generated MP3 files according to local retention needs. <br>


## Reference(s): <br>
- [Available Kokoro Voices](artifact/references/voices.md) <br>
- [Kokoro TTS on ClawHub](https://clawhub.ai/edkief/skills/kokoro-tts) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Files, Configuration, Guidance] <br>
**Output Format:** [Plain text command guidance and a MEDIA-prefixed MP3 file path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Saves generated MP3 files under the local media directory and supports configurable voice, speed, and Kokoro API endpoint.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
