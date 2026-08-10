## Description: <br>
Use when someone wants a full music video, including original song or vocals, performance clips, B-roll, and lyric-synced edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, creators, and developers use this skill to plan and run an AI music-video workflow from lyrics and song generation through alignment, stills, video clips, and ffmpeg assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can spend credits or call external generation services before the user is ready. <br>
Mitigation: Keep the documented phase gates in place: approve plan, approve stills, and approve clips before moving into paid or high-cost generation steps. <br>
Risk: The workflow uploads generated songs, stills, audio slices, and video assets to Pruna or Replicate-style services. <br>
Mitigation: Use the skill only when the user is comfortable sending those media assets to the external services named in the workflow and evidence security guidance. <br>
Risk: Lyric-synced videos can drift or cut mid-word if timing is guessed. <br>
Mitigation: Use WhisperX alignment and review timing stats before video generation, then trim clips on line boundaries during assembly. <br>
Risk: Character continuity can break across performance clips when each still is generated independently. <br>
Mitigation: Approve one hero still, store its URL in the plan, and derive later performance stills from that reference when the user wants one singer throughout. <br>
Risk: The optional full-suite install adds more capabilities than this single workflow needs. <br>
Mitigation: Review the optional full-suite install before use and install only the specific prerequisite skills needed for the requested workflow. <br>


## Reference(s): <br>
- [Music Video Skill Page](https://clawhub.ai/pruna-ai/skills/music-video) <br>
- [Lyrics and Cut-Safe Editing](lyrics-and-cuts.md) <br>
- [Music Video Quality Checklist](references/music-video-quality-checklist.md) <br>
- [Music Video Examples](examples.md) <br>
- [Music Video Plan Template](templates/music-video-plan.template.json) <br>
- [Pruna Music-to-Video Workflow](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/skills/workflows/music_to_video.html) <br>
- [MiniMax Music 2.5](https://replicate.com/minimax/music-2.5) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON plan templates, shell commands, and generated media file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a gated workflow that can create lyrics, song audio, cut manifests, still-image prompts, video-clip jobs, and a final music_video.mp4 assembly.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
