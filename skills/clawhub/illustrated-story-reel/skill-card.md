## Description: <br>
Use when someone wants a slideshow story with narration or music -- picture-book illustrated frames with Ken Burns or gentle p-video motion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative operators use this skill to plan and generate illustrated story reels with per-beat stills, narration or music, optional gentle video motion, and final local MP4 assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses paid media APIs and requires API credentials. <br>
Mitigation: Use dedicated credentials and follow the staged approval gates before TTS, music, video, and assembly. <br>
Risk: Local ffmpeg assembly can overwrite the target MP4 path. <br>
Mitigation: Use a dedicated output folder and confirm the final MP4 path before assembly. <br>
Risk: Plan files and generated media may contain private prompts, narration, or project details. <br>
Mitigation: Treat plan.json and generated media as confidential when prompts or narration include private information. <br>
Risk: Generated stills, audio, or motion clips can be unsuitable before final assembly. <br>
Mitigation: Review outputs at the stills, audio, and clips gates before proceeding to later phases. <br>


## Reference(s): <br>
- [Illustrated story reel -- API reference](artifact/references/illustrated-story-reel-api.md) <br>
- [Illustrated story reel -- staged gates](artifact/references/illustrated-story-reel-gates.md) <br>
- [Illustrated story reel -- p-video motion](artifact/references/illustrated-story-reel-p-video-motion.md) <br>
- [Illustrated story reel -- positive still prompts](artifact/references/illustrated-story-reel-prompts.md) <br>
- [Illustrated story reel -- quality gates](artifact/references/illustrated-story-reel-quality.md) <br>
- [Vertical story plan template](artifact/templates/story-plan.template.json) <br>
- [Landscape story plan template](artifact/templates/story-plan.landscape.template.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands, API Calls, Files] <br>
**Output Format:** [Markdown guidance with JSON plan templates, API request patterns, shell commands, and generated media file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a staged plan and media workflow that can create plan.json, stills, audio, optional clips, and a final story_reel.mp4 under a user-selected output directory.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
