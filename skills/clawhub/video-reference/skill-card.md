## Description:

Analyzes a finished video for reusable editing and audio patterns, separating source-specific facts from an exported production reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Video editors and production agents use this optional Chinese-language workflow to measure shot pacing and loudness, review cuts, and turn an existing video into reusable production guidance without exporting its source-specific facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local video analysis runs Python and ffmpeg/ffprobe on selected media.

Mitigation: Review the workflow before running it and analyze only videos you intend to process.

Risk: Local breakdown JSON and frame images can contain identifiable details from the source video.

Mitigation: Keep the working directory local and avoid sharing the breakdown or extracted frames.

Risk: Literal leak checks may miss paraphrased plot details in the exported reference.

Mitigation: Manually review production_reference.json before reuse or sharing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/worldwonderer/skills/video-reference)
- [Reference schema](artifact/references/reference-schema.md)

## Skill Output:

**Output Type(s):** [Guidance, Files]

**Output Format:** [JSON (production_reference.json)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Contains measured editing and audio profiles plus reusable methods; source-specific facts and extracted frames remain in the local work directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
