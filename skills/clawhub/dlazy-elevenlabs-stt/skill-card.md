## Description:

Transcribes audio with ElevenLabs scribe_v1 through dLazy, with language selection and optional speaker diarization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to transcribe audio for subtitles, meeting notes, and other text records, optionally separating speakers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio or referenced local media is sent to dLazy's cloud service.

Mitigation: Confirm that the audio can be shared with the service before submitting it.

Risk: Logging in stores a dLazy API key locally.

Mitigation: Protect the local credential and rotate or revoke it if exposed.

Risk: Installing the external CLI executes third-party software.

Mitigation: Review the CLI package and use the documented pinned npx invocation if a persistent global install is unnecessary.

Risk: The documentation's --prompt example does not match the audio input option.

Mitigation: Supply audio using --audio_url instead.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-stt)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON transcription response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional speaker diarization and asynchronous task status.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
