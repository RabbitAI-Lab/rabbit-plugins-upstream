## Description:

Alibaba Bailian Fun-ASR recording transcription supports Chinese, English, and other languages with automatic language detection and speaker diarization for subtitles, transcripts, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send audio URLs or local audio files to dLazy's hosted Fun-ASR transcription service and receive transcription results. It is suited to subtitles, meeting notes, and multilingual speech transcription workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio files, audio URLs, prompts, and related parameters may be sent to dLazy's hosted transcription service.

Mitigation: Use the skill only for audio that may be processed by dLazy, and review dLazy's service terms before submitting sensitive content.

Risk: The dLazy CLI can save an API key in the local user configuration.

Mitigation: Use a per-command DLAZY_API_KEY environment variable when avoiding a persistent local API key is preferred, and rotate or revoke keys from the dLazy dashboard as needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous generateId instead of immediate outputs when --no-wait is used.]

## Skill Version(s):

1.3.6 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
