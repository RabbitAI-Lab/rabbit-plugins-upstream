## Description:

Self-hosted OpenAI-compatible speech service for transcription, live ASR, text-to-speech, stereo diarization, URL fetching, file staging, and bearer-authenticated speech workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate a self-hosted speech service, transcribe audio, generate subtitles, stream ASR, synthesize speech, and connect OpenAI-compatible audio clients to local or trusted Talkies deployments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Speech text, uploaded audio, and voice-cloning reference samples are sent to the configured Talkies server.

Mitigation: Use only a server you operate or explicitly trust, prefer HTTPS or loopback binding, and avoid sending confidential material to untrusted endpoints.

Risk: Shared or non-local Talkies deployments can expose speech endpoints when bearer authentication is not configured.

Mitigation: Set TALKIES_AUTH_TOKEN, restrict network exposure, and place public deployments behind appropriate TLS, rate limiting, and access controls.

Risk: URL-based file_path requests are fetched by the Talkies server and can reach private or internal network locations if allowed.

Mitigation: Enable private-download blocking when untrusted users can submit URLs and pass only URLs that are intended for the server to fetch.

Risk: Server-side staged files persist and share one namespace, so other callers with access may enumerate, read, or remove them.

Mitigation: Treat file staging as an admin or trusted-user feature, clean up staged files after use, and add deployment-level retention and isolation controls where needed.

Risk: Voice cloning or synthetic speech can enable impersonation or deceptive use.

Mitigation: Clone or synthesize voices only with explicit speaker authorization and keep consent requirements visible in user workflows.

Risk: Setup and workflow examples can run local shell commands such as docker, curl, and ffmpeg.

Mitigation: Review commands, container images, target hosts, and file paths before execution, especially when working with unfamiliar deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/talkies)
- [Setup guide](references/setup.md)
- [Talkies project homepage](https://github.com/psyb0t/docker-talkies)
- [Streaming ASR documentation](https://github.com/psyb0t/docker-talkies/blob/main/docs/streaming.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, API request examples, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing operational guidance for ASR, TTS, file staging, streaming, deployment, and cleanup workflows.]

## Skill Version(s):

1.3.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
