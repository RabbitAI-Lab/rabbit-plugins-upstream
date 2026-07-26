## Description: <br>
Local STT with selectable backends - Parakeet (best accuracy) or Whisper (fastest, multilingual). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[araa47](https://clawhub.ai/user/araa47) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users can use this skill to transcribe local audio files with selectable Parakeet or Whisper speech-to-text models. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using --room-id sends recognized speech text to Matrix with MATRIX_HOMESERVER and MATRIX_ACCESS_TOKEN. <br>
Mitigation: Use --room-id only with appropriate consent, room access, and token handling; omit the option for sensitive audio. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/araa47/skills/local-stt) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Plain text transcript with Markdown usage examples and JSON configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ffmpeg and uv-managed Python dependencies; can optionally post recognized speech text to a Matrix room when --room-id and Matrix credentials are supplied.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
