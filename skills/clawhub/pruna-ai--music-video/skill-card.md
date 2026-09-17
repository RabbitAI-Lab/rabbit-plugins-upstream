## Description:

Use when someone wants a full music video - original song or vocals, performance clips, B-roll, and lyric-synced edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to plan and run a gated music-video workflow from lyrics and song generation through alignment, stills, clips, and final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documentation includes unpinned, auto-confirmed npx install commands for remote skills, including a full-suite install.

Mitigation: Review install commands before use, prefer pinned and verified skill revisions, and avoid full-suite installs in environments with sensitive files or credentials.

Risk: Normal music-video generation uploads prompts, images, and audio slices to Pruna or Replicate services.

Mitigation: Do not use sensitive, private, or regulated media unless the destination service and account terms are approved for that data.

Risk: Skipping approval gates or alignment can waste paid generation calls and produce poor lip sync or mid-word cuts.

Mitigation: Follow the documented approve plan, approve stills, and approve clips gates, and use WhisperX timing review before video generation.

## Reference(s):

- [Music video quality checklist](artifact/references/music-video-quality-checklist.md)
- [Lyrics and cut-safe editing](artifact/lyrics-and-cuts.md)
- [Music video plan template](artifact/templates/music-video-plan.template.json)
- [Pruna music-to-video workflow](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/skills/workflows/music_to_video.html)
- [MiniMax Music 2.5](https://replicate.com/minimax/music-2.5)
- [ClawHub music-video skill page](https://clawhub.ai/pruna-ai/skills/music-video)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON plan templates and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces phase-gated workflow instructions and file templates for external media-generation and ffmpeg assembly tools.]

## Skill Version(s):

1.0.12 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
