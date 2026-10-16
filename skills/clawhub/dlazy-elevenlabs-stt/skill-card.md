## Description:

Transcribes audio with ElevenLabs Scribe v1, with language selection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to transcribe audio for subtitles, transcripts, and meeting notes, optionally separating speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio and API requests are sent to dLazy-hosted services, and the CLI may store an API key locally.

Mitigation: Confirm the dLazy service and CLI are trusted before submitting sensitive audio; protect and rotate the API key as needed.

Risk: Copied examples describe prompt and image/video inputs that do not match this transcription command.

Mitigation: Use the documented audio_url, language_code, and diarize options instead of the prompt example.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI homepage (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Transcribed text in a JSON result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization; asynchronous requests return a task ID instead of an immediate result.]

## Skill Version(s):

1.3.30 (source: server-resolved release; skill frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
