## Description: <br>
Use when someone wants a full music video: original song or vocals, performance clips, B-roll, and lyric-synced edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to plan and orchestrate lyric-synced AI music videos with gated lyrics, song, still, clip, and assembly phases. It coordinates Pruna and Replicate media skills, WhisperX alignment, and ffmpeg assembly while keeping user approval gates before paid generation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can spend credits on external media APIs. <br>
Mitigation: Keep the lyrics, song, stills, and clips approval gates enabled before running paid generation steps. <br>
Risk: Song slices, stills, and prompts may be uploaded to Replicate or Pruna services. <br>
Mitigation: Review planned inputs before upload and avoid including sensitive or unapproved media in prompts, audio slices, or still images. <br>
Risk: Lyric-synced cuts can drift or cut words if alignment is skipped. <br>
Mitigation: Run WhisperX alignment and review cut timing before video generation and final assembly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/music-video) <br>
- [lyrics-and-cuts.md](lyrics-and-cuts.md) <br>
- [Music video quality checklist](references/music-video-quality-checklist.md) <br>
- [music-video-plan.template.json](templates/music-video-plan.template.json) <br>
- [Pruna music-to-video workflow documentation](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/skills/workflows/music_to_video.html) <br>
- [MiniMax Music 2.5 on Replicate](https://replicate.com/minimax/music-2.5) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON plan templates and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces phased generation plans, approval checkpoints, cut manifests, media API routing guidance, and ffmpeg assembly commands.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
