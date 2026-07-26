## Description: <br>
Convert text to speech using Microsoft Edge's TTS engine with customizable voices, direct playback, and automatic temporary file cleanup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaov1976](https://clawhub.ai/user/zhaov1976) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use this skill to add text-to-speech, voice listing, audio playback, and temporary audio cleanup workflows to an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Normal inputs can reach shell and system playback commands. <br>
Mitigation: Install only from a trusted publisher, review generated actions before use, and avoid untrusted text, options, playback paths, or output paths until command execution uses safe argument arrays and path constraints. <br>
Risk: Text sent for speech generation may be processed by an external TTS service. <br>
Mitigation: Do not pass secrets, credentials, private messages, or other sensitive text unless external processing and retention behavior are acceptable. <br>
Risk: Dependency installation and runtime behavior depend on the edge-tts package and local audio players. <br>
Mitigation: Pin and review dependencies before deployment, and verify that local playback tooling is available and acceptable in the target environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhaov1976/skills/voice) <br>


## Skill Output: <br>
**Output Type(s):** [text, files, shell commands] <br>
**Output Format:** [JSON result objects with status messages, media file paths, voice lists, and generated MP3 audio files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated audio is stored in temporary files; direct speaking schedules cleanup after playback, and cleanup can remove older audio files.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
