## Description:

Self-hosted OpenAI-compatible speech service for transcription, live ASR streaming, text-to-speech, stereo diarization, URL-based file input, server-side file staging, MCP ASR tools, and optional bearer authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use talkies to run a self-hosted speech API for transcribing audio, generating subtitles, streaming live ASR, and synthesizing speech from text or authorized reference voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text, audio, reference voice samples, and URLs are sent to the configured Talkies server.

Mitigation: Use only a server you run or explicitly trust; prefer localhost or HTTPS and avoid sending confidential media to untrusted deployments.

Risk: Server-side staged files and URL downloads can persist and may be visible to other callers on the same instance.

Mitigation: Clean up files after use, avoid private URLs on shared servers, and treat file-management operations as administrative in shared deployments.

Risk: An unprotected or broadly exposed deployment can accept requests from anyone who can reach the port.

Mitigation: Enable TALKIES_AUTH_TOKEN for shared or exposed deployments and restrict network exposure with localhost binding, HTTPS, and proxy controls.

Risk: Voice cloning and synthesized speech can be misused for impersonation or deception.

Mitigation: Use only reference voices with the speaker's informed consent and authorization.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/talkies)
- [Setup reference](references/setup.md)
- [Talkies streaming documentation](https://github.com/psyb0t/docker-talkies/blob/main/docs/streaming.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and API examples; service responses may include JSON, text, SRT, VTT, or audio files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the configured Talkies server, selected speech model, response_format, authentication, and file-staging settings.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
