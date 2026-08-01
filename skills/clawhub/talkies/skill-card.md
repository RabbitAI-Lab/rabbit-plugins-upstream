## Description: <br>
talkies is a self-hosted, OpenAI-compatible speech service for transcription, live ASR, speech synthesis, stereo diarization, URL fetching, MCP access, and optional bearer-token authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agent builders use this skill to connect agents to a trusted talkies server for speech-to-text, subtitles, streaming transcription, and text-to-speech workflows. It can also support existing OpenAI-compatible audio clients that need a self-hosted backend. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio, text, transcripts, and voice samples may be sent to and stored by the configured talkies server. <br>
Mitigation: Use only a server you run or explicitly trust, prefer localhost or HTTPS, and enable TALKIES_AUTH_TOKEN for any shared deployment. <br>
Risk: Server-side staged files and URL downloads may persist and be visible to other callers with API access. <br>
Mitigation: Avoid sending private media to untrusted servers, clean up staged files and cached downloads after use, and treat shared file staging as admin-controlled. <br>
Risk: Voice cloning and voice design can enable unauthorized impersonation or deceptive synthetic speech. <br>
Mitigation: Use voice cloning only with explicit speaker consent and avoid cloning or synthesizing real voices for fraud, deception, or unauthorized replication. <br>
Risk: URL file_path downloads are performed by the server and can reach network locations from the server environment. <br>
Mitigation: For exposed or multi-user deployments, set TALKIES_BLOCK_PRIVATE_DOWNLOADS=true and restrict network exposure with authentication and TLS. <br>


## Reference(s): <br>
- [Setup and configuration](references/setup.md) <br>
- [talkies ClawHub listing](https://clawhub.ai/psyb0t/skills/talkies) <br>
- [talkies project homepage](https://github.com/psyb0t/docker-talkies) <br>
- [Streaming protocol documentation](https://github.com/psyb0t/docker-talkies/blob/main/docs/streaming.md) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, API Calls, Files] <br>
**Output Format:** [Markdown guidance with curl and shell examples; API outputs can include JSON, plain text, SRT, VTT, and generated audio files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses TALKIES_URL as the primary endpoint setting and optionally TALKIES_AUTH_TOKEN for bearer authentication.] <br>

## Skill Version(s): <br>
1.3.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
