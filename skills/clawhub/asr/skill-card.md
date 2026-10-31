## Description:

Transcribes audio with Speech is Cheap, supporting 100 languages, speaker diarization, word timestamps, and configurable output formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ilyakam](https://clawhub.ai/user/ilyakam)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to submit audio files or audio URLs to Speech is Cheap for transcription, job-status lookup, and transcript formats such as JSON, SRT, VTT, and WebVTT.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected audio files, audio URLs, transcription options, and optional webhook URLs are sent to Speech is Cheap.

Mitigation: Use the skill only when the provider's privacy terms fit the content, and use --private for sensitive recordings.

Risk: Confidential internal URLs or recordings could be exposed to an external transcription provider.

Mitigation: Avoid submitting confidential internal URLs or audio unless the release owner has approved that provider for the data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ilyakam/skills/asr)
- [Speech is Cheap](https://speechischeap.com)
- [Speech is Cheap Documentation](https://docs.speechischeap.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell command examples; command output is JSON or subtitle text depending on selected options.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SIC_API_KEY and sends selected audio files, audio URLs, transcription options, and optional webhook URLs to Speech is Cheap.]

## Skill Version(s):

1.2.0 (source: server release metadata, artifact manifest, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
