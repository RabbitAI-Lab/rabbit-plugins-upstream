## Description: <br>
Local Voice helps agents set up and use a local FluidAudio TTS/STT daemon on Apple Silicon Macs for offline speech synthesis and transcription. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[trondw](https://clawhub.ai/user/trondw) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and voice assistant integrators use this skill to configure local text-to-speech and speech-to-text on Apple Silicon Macs, replacing cloud TTS/STT calls with localhost endpoints where appropriate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup installs a user-level macOS background service that starts at login and listens on localhost. <br>
Mitigation: Review the LaunchAgent before loading it, keep access limited to localhost, and document how to unload the service and remove installed files. <br>
Risk: Speech models or dependencies may be downloaded during setup or first startup before later offline use. <br>
Mitigation: Run installation in an approved network environment, verify downloaded dependencies, and cache required models before relying on offline operation. <br>
Risk: Transcription output snippets may be written to local logs. <br>
Mitigation: Avoid sensitive speech until transcript-content logging is removed or disabled, and rotate or delete existing local logs. <br>


## Reference(s): <br>
- [Kokoro Voice Reference](artifact/references/VOICES.md) <br>
- [FluidAudio dependency](https://github.com/FluidInference/FluidAudio.git) <br>
- [Hummingbird dependency](https://github.com/hummingbird-project/hummingbird.git) <br>
- [ClawHub skill page](https://clawhub.ai/trondw/skills/local-voice) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with inline bash, curl, JavaScript, and Swift code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides setup of a localhost HTTP service that returns WAV audio for TTS and JSON transcripts for STT when deployed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
