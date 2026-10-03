## Description:

Guides agents through obtaining word-level timestamps from audio for lyric alignment, cut-safe edits, and caption timing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media creators use this skill to align audio with word-level timestamps for lyric edits, cut boundaries, and captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audio is provided to Replicate for transcription.

Mitigation: Confirm permission to upload recordings and avoid sending sensitive audio without approval.

Risk: A Replicate API token is required for transcription.

Mitigation: Keep the token in secure environment storage and out of shared commands and outputs.

Risk: Related-skill installation commands fetch external packages.

Mitigation: Review installation commands and use pinned or trusted versions before running them.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides audio input and alignment settings; downstream transcription can produce JSON and SRT files.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
