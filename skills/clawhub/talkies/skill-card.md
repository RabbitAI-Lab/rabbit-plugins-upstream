## Description:

talkies helps agents use a self-hosted OpenAI-compatible speech service for transcription, live ASR, text-to-speech, diarization, URL-based audio processing, file staging, and bearer-authenticated workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run speech-to-text, subtitle generation, live PCM transcription, text-to-speech, and voice-cloning workflows against a Talkies server they operate or trust.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio, text, and voice samples are sent to the configured Talkies server.

Mitigation: Use only a Talkies server you operate or explicitly trust; prefer localhost or HTTPS and enable bearer-token authentication.

Risk: Server-side staged files and URL downloads may persist and be visible to callers who can reach the API.

Mitigation: Clean up staged files after use, avoid staging sensitive media on shared deployments, and restrict network exposure.

Risk: Voice cloning can enable impersonation or deceptive speech generation.

Mitigation: Only clone or synthesize voices with explicit speaker authorization and informed consent.

Risk: Setup and workflow examples execute local shell commands such as docker, curl, and ffmpeg.

Mitigation: Review commands before execution, especially when pointed at unfamiliar hosts or images.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/talkies)
- [talkies setup](references/setup.md)
- [Streaming protocol documentation](https://github.com/psyb0t/docker-talkies/blob/main/docs/streaming.md)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown, Code]

**Output Format:** [Markdown with inline shell commands, HTTP examples, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or manage transcripts, subtitle files, staged audio files, and synthesized audio through the configured Talkies server.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
