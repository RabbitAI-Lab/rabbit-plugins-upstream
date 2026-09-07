## Description:

ElevenLabs scribe_v1 speech-to-text with auto language detection and optional speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to transcribe audio files or URLs with ElevenLabs scribe_v1, including subtitles, transcription, and meeting notes with optional speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes an external npm CLI and dLazy service.

Mitigation: Install only if you trust dLazy; use npx @dlazy/cli@1.2.3 when you do not want a persistent global binary.

Risk: Selected audio files or URLs are uploaded to dLazy for transcription.

Mitigation: Pass only audio content intended for upload and avoid sensitive recordings unless the user's policy permits that processing.

Risk: Authentication uses a dLazy API key.

Mitigation: Use a revocable API key and rotate or revoke it from the dLazy dashboard when access is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying command can return synchronous JSON outputs or an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
