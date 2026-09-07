## Description:

Alibaba Bailian Fun-ASR recording transcription supports Chinese, English, and other languages, with automatic language detection and speaker diarization for subtitles, transcription, and meeting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy Fun-ASR transcription for audio recordings, including multilingual transcripts, subtitles, speaker diarization, and meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs a third-party npm CLI.

Mitigation: Review the dLazy CLI source or npm package before use, prefer the pinned npx invocation when a persistent global binary is not needed, and avoid administrator or root installation.

Risk: Selected audio inputs and related parameters are sent to dLazy-hosted services.

Mitigation: Use only audio approved for third-party cloud processing, especially when recordings or transcripts may contain sensitive information.

Risk: The artifact example uses --prompt even though the audio command documents --audio_url for audio input.

Mitigation: Use --audio_url for audio transcription and confirm the current CLI help before running production tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-fun-asr)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON transcription result with optional Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when invoked with no-wait mode.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
