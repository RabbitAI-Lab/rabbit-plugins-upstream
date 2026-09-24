## Description:

Discord语音助手 helps agents join Discord voice channels for real-time two-way voice interaction with VAD, speech-to-text, agent response handling, text-to-speech playback, barge-in handling, streaming transcription, and reconnect workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure and operate a Discord voice assistant for community voice Q&A, live captioning, accessibility support, and voice status monitoring. It is intended for Discord channels where voice capture, transcription, agent processing, and TTS playback are appropriate and disclosed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles live third-party speech and external callbacks without enough consent and data-handling controls.

Mitigation: Use it only in Discord channels where participants are clearly told that speech may be recorded, transcribed, processed by an agent, and sent to selected STT/TTS providers.

Risk: Transcripts, audio, Discord tokens, provider API keys, or callback payloads could expose sensitive data.

Mitigation: Prefer local providers where possible, restrict allowedUsers and channel scope, disable auto-join unless needed, use only trusted HTTPS callback endpoints with minimal transcript exposure, and store tokens in environment variables or a secret store.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/discord-voice)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with command examples and JSON configuration/output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Discord voice workflow commands, provider configuration guidance, status output, transcripts, synthesized speech instructions, and troubleshooting steps.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter lists 0.1.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
