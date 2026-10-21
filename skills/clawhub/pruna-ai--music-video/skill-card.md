## Description:

Helps create a complete music video with an original song or vocals, performance clips, B-roll, and lyric-synced edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to plan lyrics and cuts, generate a song and visuals, review each stage, and assemble a lyric-synced music video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation commands may fetch an unintended skill version or source.

Mitigation: Verify the source and version before installing, especially in sensitive environments.

Risk: Audio and images are uploaded to external generation services.

Mitigation: Avoid confidential media unless upload is intended, and use dedicated, limited-scope API keys.

Risk: Generating songs and video clips consumes paid API credits.

Mitigation: Keep the documented approval gates before paid generation and review outputs before continuing.

## Reference(s):

- [Music Video on ClawHub](https://clawhub.ai/pruna-ai/skills/music-video)
- [Lyrics and Cut-Safe Editing](lyrics-and-cuts.md)
- [Music Video Quality Checklist](references/music-video-quality-checklist.md)
- [Music Video Plan Template](templates/music-video-plan.template.json)
- [Pruna Music-to-Video Workflow](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/skills/workflows/music_to_video.html)
- [MiniMax Music 2.5](https://replicate.com/minimax/music-2.5)

## Skill Output:

**Output Type(s):** [Markdown guidance, JSON plans, Shell commands, Audio and video files]

**Output Format:** [Markdown instructions and JSON cut plans; generated MP3 and MP4 files after execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lyrics, song, stills, and clips have approval gates before final assembly.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
