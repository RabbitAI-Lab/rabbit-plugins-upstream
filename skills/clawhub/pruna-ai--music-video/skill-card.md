## Description:

Use when someone wants a full music video: original song or vocals, performance clips, B-roll, and lyric-synced edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to plan and run a gated AI music-video workflow, from lyrics and song generation through aligned cuts, stills, video clips, and final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable npx install commands can install changed helper skills or a broader skill suite than needed.

Mitigation: Review install commands, prefer pinned or verified installers, and install only the specific helper skills required for the workflow.

Risk: API keys, prompts, stills, and audio slices may be sent to external generation services and may incur cost.

Mitigation: Keep API keys out of committed files and logs, confirm which services will receive media, and use the approval gates before paid generation.

Risk: Lyric timing or lip sync can drift if video clips are generated before alignment is checked.

Mitigation: Use WhisperX alignment before video generation, review timing statistics, listen once, and avoid cuts that split words.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/music-video)
- [Music video quality checklist](references/music-video-quality-checklist.md)
- [Lyrics and cut-safe editing](lyrics-and-cuts.md)
- [Examples](examples.md)
- [Music video plan template](templates/music-video-plan.template.json)
- [Pruna music-to-video workflow documentation](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/skills/workflows/music_to_video.html)
- [MiniMax Music 2.5 model page](https://replicate.com/minimax/music-2.5)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON plan templates, shell commands, and generated media file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces lyrics, music prompts, cut manifests, still and clip generation prompts, ffmpeg assembly commands, and approval-gated workflow guidance.]

## Skill Version(s):

1.0.13 (source: server release metadata, SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
