## Description:

Transcribes audio with ElevenLabs scribe_v1 for subtitles, meeting notes, and other transcripts, with language selection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, teams, and developers use this skill to turn audio into text for subtitles, transcription, and meeting notes, with optional speaker diarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI executable is installed from npm.

Mitigation: Review the @dlazy/cli package and source before installing.

Risk: Audio submitted for transcription is sent to dLazy/ElevenLabs services.

Mitigation: Submit only audio you are comfortable sharing with those services.

Risk: API keys can be stored locally and saved output can write to a chosen path.

Mitigation: Use a per-run DLAZY_API_KEY to avoid a stored key, and use --save only with trusted output paths.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text transcript in a JSON result; agent responses may be plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization; asynchronous requests can return a task ID before the transcript is ready.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
