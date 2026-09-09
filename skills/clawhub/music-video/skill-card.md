## Description:

Use when someone wants a full music video including original song or vocals, performance clips, B-roll, and lyric-synced edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan and run staged AI music-video production from lyrics and song generation through cut alignment, stills, video clips, and final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can spend credits on external AI media services.

Mitigation: Use the documented approval gates for plan, stills, and clips before running paid generation steps.

Risk: Prompts, stills, and audio slices may be uploaded to Pruna or Replicate during generation.

Mitigation: Avoid private or sensitive media unless the user is comfortable sending it to those services.

Risk: Installer references and required tools can introduce supply-chain exposure.

Mitigation: Use trusted package sources, consider pinning installer references, and verify ffmpeg and ffprobe availability before execution.

## Reference(s):

- [Lyrics and Cut-Safe Editing](artifact/lyrics-and-cuts.md)
- [Music Video Quality Checklist](artifact/references/music-video-quality-checklist.md)
- [Music Video Plan Template](artifact/templates/music-video-plan.template.json)
- [Pruna Music-to-Video Workflow Documentation](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/skills/workflows/music_to_video.html)
- [MiniMax Music 2.5](https://replicate.com/minimax/music-2.5)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON plan templates and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coordinates Pruna and Replicate media generation plus ffmpeg assembly with explicit approval gates before costly steps.]

## Skill Version(s):

1.0.11 (source: release evidence and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
