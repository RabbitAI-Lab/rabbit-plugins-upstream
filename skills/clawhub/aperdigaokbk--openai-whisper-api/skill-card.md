## Description:

Transcribe audio via OpenAI Audio Transcriptions API (Whisper).

This skill is ready for commercial/non-commercial use.

## Publisher:

[aperdigaokbk](https://clawhub.ai/user/aperdigaokbk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to transcribe local audio files through OpenAI's audio transcription API and save the result as text or JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected audio files are sent to OpenAI for transcription.

Mitigation: Use the skill only for recordings that your OpenAI account, project permissions, and data-handling requirements allow.

Risk: The skill requires an OpenAI API key.

Mitigation: Store or supply the key only through approved credential handling practices and avoid exposing it in shared files or command history.

## Reference(s):

- [OpenAI Speech to Text documentation](https://platform.openai.com/docs/guides/speech-to-text)
- [OpenAI Audio Transcriptions endpoint](https://api.openai.com/v1/audio/transcriptions)
- [ClawHub skill page](https://clawhub.ai/aperdigaokbk/skills/openai-whisper-api)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration]

**Output Format:** [Plain text transcript or JSON transcription file produced by a shell command]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and OPENAI_API_KEY; writes .txt output by default or .json when requested.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
