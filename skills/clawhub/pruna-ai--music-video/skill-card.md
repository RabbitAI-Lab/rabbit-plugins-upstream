## Description:

Use when someone wants a full music video: original song or vocals, performance clips, B-roll, and lyric-synced edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill to plan and run lyric-synced music-video production from approved lyrics and song generation through cut alignment, stills, video clips, and ffmpeg assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic installation of multiple remote skills can pull mutable or unnecessary dependencies.

Mitigation: Review install commands, avoid automatic -y installs, and pin or verify the specific skills and installer before use.

Risk: Generated media workflows require API keys and may transfer uploads to external providers.

Mitigation: Use dedicated API keys with spending limits, keep tokens out of shared shells and logs, and verify data-transfer expectations before uploading media.

Risk: The workflow contains an always-on reply instruction that can shape agent behavior beyond the core production task.

Mitigation: Constrain use to the music-video workflow, and review agent replies and plans at each phase gate before paid generation.

## Reference(s):

- [Music video quality checklist](references/music-video-quality-checklist.md)
- [Lyrics and cut-safe editing](lyrics-and-cuts.md)
- [Pruna music-to-video workflow](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/skills/workflows/music_to_video.html)
- [MiniMax Music 2.5](https://replicate.com/minimax/music-2.5)
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/music-video)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON plan templates and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce JSON planning artifacts, cut manifests, ffmpeg command lines, and final media assembly guidance; generated media is produced by dependent tools.]

## Skill Version(s):

1.0.12 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
