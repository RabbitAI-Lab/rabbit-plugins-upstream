## Description:

Guides final video assembly by placing narration, ducking source audio, generating subtitles, and optionally normalizing loudness and exporting an editable JianYing draft.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and developers use this skill to assemble narration, source audio and subtitles into a finished recap video, with optional editable-draft export and quality-control records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media processing may overwrite existing output files.

Mitigation: Review work and output directories before running and preserve important existing files.

Risk: An exported JianYing draft may differ from the delivered rendered video.

Mitigation: Treat the draft as an editable sidecar and inspect the rendered MP4 before delivery.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/worldwonderer/skills/video-assemble)
- [Audio modes](references/audio-modes.md)
- [Narration adoption](references/narration-adoption.md)
- [Subtitle track contract](references/subtitle-track.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution produces a rendered video, subtitle tracks, an assembly manifest and quality-control records; an editable JianYing draft is optional.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
