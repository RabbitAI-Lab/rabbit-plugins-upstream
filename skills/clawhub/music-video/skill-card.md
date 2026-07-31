## Description: <br>
Use when someone wants a full music video - original song or vocals, performance clips, B-roll, and lyric-synced edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creators use this skill to plan and run a phased AI music-video workflow: lyrics, song generation, lyric alignment, stills, video clips, and final ffmpeg assembly. It is intended for media generation workflows that require approval gates before paid generation steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses paid PrunaAI and Replicate-backed media generation APIs and may upload prompts, audio, and images to those providers. <br>
Mitigation: Install and run it only when those providers, API keys, uploads, and paid generation steps are acceptable for the project. <br>
Risk: Optional full-suite installation may add more capabilities than needed for the music-video workflow. <br>
Mitigation: Review the full-suite install path before use, or install only the specific skills required for the workflow. <br>
Risk: Generating clips before lyric approval, song approval, and WhisperX alignment can cause lip-sync drift or cuts in the middle of words. <br>
Mitigation: Follow the documented approval gates and alignment step before stills, video clips, and final assembly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/music-video) <br>
- [Lyrics and cut-safe editing](lyrics-and-cuts.md) <br>
- [Music video quality checklist](references/music-video-quality-checklist.md) <br>
- [Music video plan template](templates/music-video-plan.template.json) <br>
- [Pruna music-to-video workflow](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/skills/workflows/music_to_video.html) <br>
- [MiniMax Music 2.5](https://replicate.com/minimax/music-2.5) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON plan templates and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation of JSON plan and cut manifest files, audio slices, media assets, and a final music_video.mp4.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
