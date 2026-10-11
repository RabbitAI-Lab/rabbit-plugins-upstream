## Description:

Transcribes audio with ElevenLabs scribe_v1 for subtitles, transcripts, and meeting notes, with language selection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to transcribe audio for subtitles, meeting notes, and other transcripts, optionally separating speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audio submitted for transcription is uploaded to dLazy's hosted service.

Mitigation: Confirm the audio is appropriate to share with dLazy before submitting it.

Risk: Logging in or saving an API key stores a credential in the local CLI configuration.

Mitigation: Use a per-invocation DLAZY_API_KEY if you do not want a stored key.

Risk: Copied prompt-based examples may not be the correct speech-to-text invocation.

Mitigation: Check the command help and supply an audio URL or local audio path.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON transcription result or asynchronous task status, with transcript text for the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization and language selection.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
