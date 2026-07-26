## Description: <br>
Local Voice Input/Output for Agents using the AI Voice Agent API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ricardotrevisan](https://clawhub.ai/user/ricardotrevisan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to transcribe user-provided audio through a local Voice Agent API and synthesize spoken responses to audio files. It is intended for workflows where a separately managed local backend is already running at http://localhost:8000. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a separately managed backend at http://localhost:8000. <br>
Mitigation: Install and use it only with a local backend you trust and can operate deliberately. <br>
Risk: Text submitted for speech synthesis may be handled by AWS Polly through the backend. <br>
Mitigation: Avoid sending secrets, regulated data, or highly private text unless that backend and AWS handling are acceptable for the use case. <br>
Risk: Audio input files and synthesized output paths are provided by the user or agent. <br>
Mitigation: Use deliberate audio inputs and safe output paths when running transcription or synthesis commands. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ricardotrevisan/skills/voice-agent) <br>
- [Publisher Profile](https://clawhub.ai/user/ricardotrevisan) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Files, Shell commands, Guidance] <br>
**Output Format:** [Plain text transcripts, generated audio files, and shell command invocations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local Whisper through the configured backend for speech-to-text and AWS Polly through the backend for text-to-speech.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata, frontmatter, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
