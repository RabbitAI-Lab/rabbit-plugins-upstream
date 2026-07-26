## Description: <br>
talkies helps agents use a self-hosted OpenAI-compatible speech service for audio transcription, subtitle generation, text-to-speech, voice cloning workflows, stereo diarization, and server-side file handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use talkies to point an agent at a trusted self-hosted speech server for transcribing audio, generating subtitles, and producing speech from text. It is suited for OpenAI-compatible audio workflows where the operator controls the endpoint, authentication, model choice, and handling of media files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio, text, and voice reference samples are sent to the configured talkies server, so private data can leave the local host. <br>
Mitigation: Use only a server you run or explicitly trust, prefer localhost or HTTPS, and avoid sending secrets or private media to untrusted endpoints. <br>
Risk: Shared or remote deployments can expose the API and staged files when bearer authentication is not configured. <br>
Mitigation: Set TALKIES_AUTH_TOKEN for shared or remote use, restrict network exposure, and treat staged file management as an administrative operation. <br>
Risk: Voice cloning or synthesized speech can impersonate a real person without authorization. <br>
Mitigation: Clone or synthesize a voice only with explicit authorization or consent from the speaker. <br>
Risk: Server-side staged files and cached URL downloads can persist after a workflow finishes. <br>
Mitigation: Clean up staged files and cached downloads created for the task once they are no longer needed. <br>


## Reference(s): <br>
- [talkies ClawHub listing](https://clawhub.ai/psyb0t/skills/talkies) <br>
- [Setup reference](references/setup.md) <br>
- [Project homepage](https://github.com/psyb0t/docker-talkies) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and API request examples; generated service outputs include JSON, plain text, SRT/VTT subtitle files, and audio files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured TALKIES_URL; setup workflows use Docker and curl, with an optional TALKIES_AUTH_TOKEN for authenticated deployments.] <br>

## Skill Version(s): <br>
1.3.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
