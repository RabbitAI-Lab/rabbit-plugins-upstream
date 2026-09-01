## Description:

Use when someone wants a full music video -- original song or vocals, performance clips, B-roll, and lyric-synced edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to plan and run a gated music-video workflow that creates lyrics, an AI song, aligned cut manifests, generated stills and clips, and an assembled MP4.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can spend credits on paid music, image, and video generation services.

Mitigation: Use the documented phase gates and require explicit approval before song generation, still generation, and video clip generation.

Risk: The workflow uploads audio, image, and video assets to Pruna/Replicate-style generation providers.

Mitigation: Install and run the skill only when the user is comfortable sending the required media assets to those providers.

Risk: Lyric-synced cuts can drift or cut through words if timings are guessed.

Mitigation: Run WhisperX alignment after song generation and review the cut manifest before producing video clips.

Risk: Character identity may drift across performance shots when continuity is expected.

Mitigation: Approve a hero still, derive performance stills from that reference, and reuse the approved plate for avatar clips.

## Reference(s):

- [ClawHub music-video release](https://clawhub.ai/pruna-ai/skills/music-video)
- [Pruna music-to-video workflow](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/skills/workflows/music_to_video.html)
- [MiniMax Music 2.5](https://replicate.com/minimax/music-2.5)
- [Lyrics and cut-safe editing](lyrics-and-cuts.md)
- [Music video quality checklist](references/music-video-quality-checklist.md)
- [Music video plan template](templates/music-video-plan.template.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON plan templates and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces gated workflow guidance and file plans for media generation; final artifacts may include cut manifests, audio slices, stills, clips, and a music_video.mp4 assembled with ffmpeg.]

## Skill Version(s):

1.0.10 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
