## Description: <br>
Transcribe audio to text using ElevenLabs Scribe. Supports batch transcription, realtime streaming from URLs, microphone input, and local files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paulasjes](https://clawhub.ai/user/paulasjes) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to transcribe local audio files, live stream URLs, or microphone input through ElevenLabs Scribe, with optional speaker diarization, language hints, event tagging, partial transcripts, and JSON output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected audio, microphone input, or stream URLs are sent to ElevenLabs for transcription under the user's API key. <br>
Mitigation: Use only audio you are authorized to process, avoid confidential or non-consented recordings, and use microphone mode only intentionally. <br>
Risk: The ElevenLabs API key is required for operation and could expose account access if mishandled. <br>
Mitigation: Store ELEVENLABS_API_KEY in a protected environment or secret store, avoid committing it to files, and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paulasjes/skills/elevenlabs-transcribe) <br>
- [ElevenLabs Speech to Text](https://elevenlabs.io/speech-to-text) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration] <br>
**Output Format:** [Plain text transcripts by default, JSON when requested, and stderr status or error messages for setup and runtime failures.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ELEVENLABS_API_KEY, python3, and ffmpeg; microphone mode and URL streaming send selected audio sources to ElevenLabs under the user's API key.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
