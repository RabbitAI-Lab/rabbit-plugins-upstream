## Description: <br>
Self-hosted OpenAI-compatible speech service for ASR and TTS with transcription, live PCM streaming, speech synthesis, stereo diarization, URL fetching, MCP access, and optional bearer authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to run a trusted Talkies server for speech-to-text, subtitles, live ASR, and text-to-speech workflows through OpenAI-compatible HTTP APIs and documented shell examples. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio, text, and voice samples are sent to the configured Talkies server. <br>
Mitigation: Use only a server you run or explicitly trust; prefer localhost or HTTPS and avoid sending sensitive content to untrusted hosts. <br>
Risk: Shared or exposed Talkies servers can receive unauthenticated requests when bearer authentication is not configured. <br>
Mitigation: Enable TALKIES_AUTH_TOKEN for shared or exposed deployments and limit network exposure to trusted clients. <br>
Risk: Staged uploads and URL-download artifacts can persist server-side. <br>
Mitigation: Clean up staged files after each workflow and treat file management as administrative on shared instances. <br>
Risk: Voice cloning or generated speech can be misused for impersonation. <br>
Mitigation: Clone or synthesize a person's voice only with explicit authorization and consent. <br>


## Reference(s): <br>
- [Talkies setup reference](references/setup.md) <br>
- [Talkies ClawHub listing](https://clawhub.ai/psyb0t/skills/talkies) <br>
- [Talkies project homepage](https://github.com/psyb0t/docker-talkies) <br>
- [Talkies streaming protocol documentation](https://github.com/psyb0t/docker-talkies/blob/main/docs/streaming.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and API request examples; transcription outputs may be text, JSON, SRT, VTT, or generated audio files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a trusted TALKIES_URL endpoint; optional TALKIES_AUTH_TOKEN is used when the server is configured for bearer authentication.] <br>

## Skill Version(s): <br>
1.3.11 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
