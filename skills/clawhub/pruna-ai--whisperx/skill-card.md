## Description:

Guides agents in obtaining word-level audio timestamps for lyric alignment, cut-safe boundaries, and caption timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to align words in recorded audio for lyric-synced edits, subtitle preparation, and reliable video cut points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned skill installation commands may retrieve changed third-party content.

Mitigation: Verify the publisher and use a pinned or vetted installer when possible.

Risk: Audio sent to Replicate and mishandled API credentials may expose sensitive content.

Mitigation: Submit only audio suitable for third-party processing and keep the Replicate token in the environment, out of shared logs.

## Reference(s):

- [whisperx on ClawHub](https://clawhub.ai/pruna-ai/skills/whisperx)
- [WhisperX model on Replicate](https://replicate.com/victor-upmeet/whisperx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides generation of word-aligned transcripts and subtitles; downstream helpers may write JSON and SRT files.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
