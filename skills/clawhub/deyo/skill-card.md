## Description:

Deyo guides agents to use the installed deyo CLI to transcribe explicit user-provided URLs or exact local audio/video file paths, with strict authorization, output, and troubleshooting boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[casatwy](https://clawhub.ai/user/casatwy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to run Deyo transcription through the CLI for explicitly provided links or exact local media files. It supports cleaned transcripts, raw or timed transcript formats, and sequential multi-input transcript summaries while preserving authorization and output-safety boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use Deyo API-key access, upload explicit local media, and consume the user's transcription minutes.

Mitigation: Require an explicit user request for each input and action, mask credential status, avoid automatic recharge, and surface minute or trial-confirmation decisions before paid work proceeds.

Risk: Transcripts and local output files may contain sensitive user content.

Mitigation: Accept only explicit URLs or exact ordinary file paths, reject directories and globs, keep raw working files private, and publish final files with no-clobber local helpers.

Risk: Cleaned transcripts and summaries can accidentally change or overstate source content.

Mitigation: Limit cleanup to punctuation, confident ASR corrections, and filler removal; preserve raw or structured output when requested; require source-cited batch conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/casatwy/skills/deyo)
- [Batch workflow reference](references/batch.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, plus transcript text, structured transcript formats, and local markdown summaries when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local transcript files, per-item summaries, batch indexes, and overview files using no-clobber delivery.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
