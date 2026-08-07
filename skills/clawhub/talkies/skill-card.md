## Description:

Self-hosted OpenAI-compatible speech service for transcription, live PCM ASR streaming, text-to-speech, stereo diarization, URL fetching, server-side file staging, and MCP ASR/file-staging tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run and call a self-hosted speech API for audio transcription, subtitle generation, live ASR, text-to-speech, voice cloning with authorized samples, and staged file workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio, text prompts, transcripts, and voice-cloning reference samples are sent to the configured Talkies server.

Mitigation: Use a server you operate or explicitly trust, prefer localhost or HTTPS, and avoid confidential text, audio, or unauthorized voice samples.

Risk: Server-side staged files and downloaded URLs may persist and be visible to other callers on a shared instance.

Mitigation: Enable authentication, limit network exposure, avoid staging sensitive data on shared servers, and clean up files after each workflow.

Risk: URL fetching is performed by the server and can expose private network resources if unrestricted.

Mitigation: Enable private-download blocking on exposed deployments and only submit URLs appropriate for the server operator to fetch.

Risk: Debug logging can record request and response bodies that include transcripts, TTS input text, and voice reference details.

Mitigation: Do not run debug logging with real or sensitive data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/psyb0t/skills/talkies)
- [Setup Guide](references/setup.md)
- [Source Homepage](https://github.com/psyb0t/docker-talkies)
- [Streaming Documentation](https://github.com/psyb0t/docker-talkies/blob/main/docs/streaming.md)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and bash command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe generated transcript, subtitle, audio, or staged-file outputs produced by the configured Talkies server.]

## Skill Version(s):

1.3.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
