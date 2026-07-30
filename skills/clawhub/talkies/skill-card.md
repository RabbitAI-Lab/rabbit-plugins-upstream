## Description: <br>
Self-hosted OpenAI-compatible speech service for ASR, live PCM transcription, TTS, stereo diarization, URL fetching, MCP access, and optional bearer-token authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect agents to a self-hosted talkies speech server for transcription, subtitle generation, live ASR, speech synthesis, voice discovery, file staging, and maintenance workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requests send text, audio, and voice-cloning samples to the configured TALKIES_URL. <br>
Mitigation: Use only a server you control or explicitly trust, prefer HTTPS outside localhost or LAN, and avoid sending confidential data to shared servers. <br>
Risk: A server without TALKIES_AUTH_TOKEN can expose speech, file staging, and management endpoints to anyone who can reach it. <br>
Mitigation: Set TALKIES_AUTH_TOKEN for non-local deployments and pair it with TLS, a trusted tunnel, or a reverse proxy with rate limiting. <br>
Risk: Staged uploads and URL downloads persist server-side and can be listed or removed through the API. <br>
Mitigation: Stage only needed files, delete staged or cached files when the task is complete, and treat file management as admin-only on shared instances. <br>
Risk: Voice cloning can enable unauthorized impersonation or deceptive synthesized speech. <br>
Mitigation: Clone or synthesize real voices only with explicit authorization and informed consent from the speaker. <br>
Risk: Debug logging can capture TTS input text, cloned-voice transcripts, and ASR transcripts. <br>
Mitigation: Keep production logging at info or higher, and use debug logging only for local troubleshooting with synthetic or disposable data. <br>
Risk: Server-side URL fetching can retrieve private or sensitive media and cache it on the server. <br>
Mitigation: Do not pass private media URLs unless the server is trusted and access-controlled; enable private-address blocking when exposed to untrusted clients. <br>


## Reference(s): <br>
- [talkies setup](references/setup.md) <br>
- [docker-talkies repository](https://github.com/psyb0t/docker-talkies) <br>
- [talkies streaming documentation](https://github.com/psyb0t/docker-talkies/blob/main/docs/streaming.md) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline JSON, shell commands, configuration snippets, and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce transcripts, subtitles, synthesized audio requests, MCP configuration, and server maintenance commands depending on the user task.] <br>

## Skill Version(s): <br>
1.3.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
