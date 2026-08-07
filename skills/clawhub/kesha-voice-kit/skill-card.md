## Description:

Local multilingual voice toolkit for speech-to-text, text-to-speech, speaker diarization, and language detection over a CLI or MCP server, running offline on Apple Silicon, Linux, and Windows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drakulavich](https://clawhub.ai/user/drakulavich)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to transcribe local audio, synthesize voice replies, detect language, and expose those capabilities through CLI, OpenClaw, or MCP workflows. It is intended for offline voice workflows where audio should remain on the user's machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global Bun installation and local model downloads add software and model artifacts to the user's machine.

Mitigation: Review the install commands first, use `kesha install --plan` to preview downloads where available, and install only in environments that need local voice processing.

Risk: OpenClaw transcript echoing and automatic TTS replies can expose private audio content in chat workflows.

Mitigation: Review and adjust the OpenClaw configuration before applying it, especially `echoTranscript`, `echoFormat`, and automatic TTS reply settings.

Risk: Routing unrelated files or private audio into the CLI could process content the user did not intend to transcribe or synthesize.

Mitigation: Limit tool routing to explicit audio paths and avoid broad file or media routing rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drakulavich/skills/kesha-voice-kit)
- [npm package](https://www.npmjs.com/package/@drakulavich/kesha-voice-kit)
- [Project source link from artifact README](https://github.com/drakulavich/kesha-voice-kit)
- [Release notes link from artifact README](https://github.com/drakulavich/kesha-voice-kit/releases)
- [Speaker diarization platform limitation](https://github.com/drakulavich/kesha-voice-kit/issues/199)
- [macOS AVSpeech SSML limitation](https://github.com/drakulavich/kesha-voice-kit/issues/236)
- [Kokoro script support limitation](https://github.com/drakulavich/kesha-voice-kit/issues/492)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell, JSON, and JSON5 examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to produce transcripts, timestamped JSON, OGG/Opus voice-note files, WAV/FLAC audio files, MCP configuration, and OpenClaw configuration.]

## Skill Version(s):

1.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
