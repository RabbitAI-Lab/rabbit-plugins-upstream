## Description:

OpenAI Audio Transcriptions API via curl; gpt-4o-transcribe, mini, diarize, or whisper-1.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to transcribe local audio files through OpenAI-compatible audio transcription endpoints, optionally selecting model, output format, language, prompt context, and diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected recordings and prompt text are uploaded to the configured transcription endpoint.

Mitigation: Use the skill only with recordings approved for that endpoint and avoid sensitive audio unless organizational policy permits upload.

Risk: A custom OPENAI_BASE_URL can send audio and the OpenAI API key to an arbitrary endpoint.

Mitigation: Use the default OpenAI endpoint or a trusted HTTPS gateway, and do not send a primary OpenAI API key to untrusted or HTTP endpoints.

## Reference(s):

- [OpenAI speech-to-text documentation](https://platform.openai.com/docs/guides/speech-to-text)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/openai-whisper-api)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration]

**Output Format:** [Plain text or JSON transcription files with shell command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, node, and OPENAI_API_KEY; selected audio and optional prompt text are uploaded to the configured transcription endpoint.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
