## Description: <br>
Self-hosted OpenAI-compatible speech service for audio transcription, live PCM transcription, text-to-speech, stereo diarization, server-side file staging, URL-based audio fetching, MCP access, and optional bearer authentication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect agents to a self-hosted speech service for transcription, subtitle generation, live speech recognition, and speech synthesis. It is suited to deployments where the operator controls or explicitly trusts the Talkies server and Docker image. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio, text prompts, transcripts, and voice-cloning samples are sent to the operator-configured TALKIES_URL server. <br>
Mitigation: Use only a server and Docker image you control or explicitly trust, prefer HTTPS behind a proxy, and avoid sending sensitive data to untrusted deployments. <br>
Risk: The service can be reachable without authentication if TALKIES_AUTH_TOKEN is not configured. <br>
Mitigation: For anything beyond a private local test, set TALKIES_AUTH_TOKEN and bind the container to localhost or another protected network boundary. <br>
Risk: Staged uploads and cached URL downloads persist server-side and may be visible to other callers on the same instance. <br>
Mitigation: Clean up files staged by the current workflow, keep shared file management admin-only, and add deployment-level isolation or retention controls for shared instances. <br>
Risk: Server-side URL fetching can retrieve remote media from locations chosen by callers. <br>
Mitigation: Pass only URLs appropriate for the server to fetch and enable private-address download blocking when the service is exposed to untrusted clients. <br>
Risk: Voice cloning and synthetic speech can be misused for impersonation or deception. <br>
Mitigation: Use voice-cloning samples only with explicit authorization and speaker consent, and review generated speech before external distribution. <br>
Risk: Debug logging can expose request and response contents, including transcripts and TTS input text. <br>
Mitigation: Keep debug logging disabled for real data and route logs through the deployment's normal sensitive-data controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/talkies) <br>
- [Publisher profile](https://clawhub.ai/user/psyb0t) <br>
- [Setup guide](references/setup.md) <br>
- [Streaming protocol documentation](https://github.com/psyb0t/docker-talkies/blob/main/docs/streaming.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, curl examples, JSON request bodies, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to produce local command lines, API calls, transcript or subtitle files, and cleanup guidance for staged server files.] <br>

## Skill Version(s): <br>
1.3.9 (source: server release evidence; target metadata version 1.3.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
