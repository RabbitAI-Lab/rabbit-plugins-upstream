## Description:

Talkies helps agents operate a self-hosted OpenAI-compatible speech service for transcription, live ASR, text-to-speech, voice cloning, diarization, URL-based audio fetching, and staged file workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use talkies to transcribe audio, generate subtitles, stream live ASR, synthesize speech, and integrate self-hosted speech endpoints into OpenAI-compatible client workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Speech, text, and voice reference samples are sent to the configured Talkies server.

Mitigation: Use localhost or a server you operate or explicitly trust, and use HTTPS or a trusted tunnel when traffic leaves the local host.

Risk: Shared or exposed deployments can accept requests without application-layer authentication if no token is configured.

Mitigation: Enable TALKIES_AUTH_TOKEN for shared or exposed deployments and limit network exposure to trusted clients.

Risk: Staged uploads and cached URL downloads can persist after a workflow completes.

Mitigation: Avoid sending secrets or regulated data, and clean up staged files and cached URL downloads when finished.

Risk: Voice cloning can reproduce a real speaker's voice.

Mitigation: Only clone or synthesize a voice with explicit speaker consent and authorization.

## Reference(s):

- [talkies ClawHub listing](https://clawhub.ai/psyb0t/skills/talkies)
- [talkies repository](https://github.com/psyb0t/docker-talkies)
- [talkies setup](references/setup.md)
- [Streaming ASR documentation](https://github.com/psyb0t/docker-talkies/blob/main/docs/streaming.md)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, curl, JSON, and configuration snippets; service workflows produce text, JSON, SRT, VTT, and audio files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes examples for direct API calls, Docker setup, MCP usage, and a bulk transcription shell workflow.]

## Skill Version(s):

1.3.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
