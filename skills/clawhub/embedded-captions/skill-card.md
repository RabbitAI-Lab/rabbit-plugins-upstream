## Description:

Adds captions or subtitles to existing single-subject talking-head videos, including readable rail captions, scene-embedded cinematic captions, and VFX-style themed captions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative-video agents use this skill to add readable or cinematic captions to single-subject talking-head clips while preserving the original footage. It guides identity selection, transcript timing, subject matting, preview QA, and final video rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can run local video-processing shell tools and mutate Hyperframes/OpenClaw skill state.

Mitigation: Review commands before execution and run the workflow in a project directory on copies of source videos.

Risk: The normal flow asks to update installed agent skills globally from upstream sources.

Mitigation: Confirm any skill-update step explicitly and prefer pinned or trusted Hyperframes sources before proceeding.

Risk: Captioning quality depends on transcription, matting, and preview review for the selected clip.

Mitigation: Use the documented decision gates and preview QA before rendering, and refuse unsuitable clips rather than shipping misleading captions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [CATALOG.md](CATALOG.md)
- [themes/README.md](themes/README.md)
- [dna/README.md](dna/README.md)
- [references/rail.md](references/rail.md)
- [references/composition-craft.md](references/composition-craft.md)
- [references/aesthetic-principles.md](references/aesthetic-principles.md)
- [references/direction-catalog.md](references/direction-catalog.md)
- [references/failure-modes.md](references/failure-modes.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local project files, preview frames, and final captioned MP4 outputs.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
