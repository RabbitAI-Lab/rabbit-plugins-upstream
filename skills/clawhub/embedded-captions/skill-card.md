## Description:

Adds synchronized captions to single-subject talking-head videos, with options for plain subtitles, typography behind the subject, and visual effects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to add timed subtitles or stylized captions to existing single-subject talking-head clips, including captions that appear behind the subject.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup installs project dependencies and may download transcription and subject-matting models.

Mitigation: Review dependency and download requirements before running, and use the project's locked versions when present.

Risk: Video processing generates numerous intermediate files and may run local tools for an extended period.

Mitigation: Allow sufficient disk space and review project outputs before delivery.

Risk: An optional skill-update command can change installed skills.

Mitigation: Confirm updates with the user before running them, especially in shared or restricted environments.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [Caption style catalog](artifact/CATALOG.md)
- [Composition craft](artifact/references/composition-craft.md)
- [Caption rail guidance](artifact/references/rail.md)

## Skill Output:

**Output Type(s):** [Video, Captions, Configuration, Guidance]

**Output Format:** [MP4 video with synchronized captions; JSON transcript and style configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate preview frames and intermediate media files.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
