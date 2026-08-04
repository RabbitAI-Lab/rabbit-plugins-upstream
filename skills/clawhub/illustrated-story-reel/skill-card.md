## Description: <br>
Use when someone wants a slideshow story with narration or music - picture-book illustrated frames with Ken Burns or gentle p-video motion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, marketers, educators, and developers use this skill to plan and generate illustrated slideshow-style story reels with narration or music. It guides staged review gates for stills, audio, optional p-video motion, and final reel assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API use and media uploads to Pruna and Replicate may incur cost and expose project media to external services. <br>
Mitigation: Confirm budget and upload acceptability before installation or generation, and use the documented approval gates before paid audio, video, or assembly phases. <br>
Risk: Generated plan and media files may contain confidential prompts or story details. <br>
Mitigation: Use an appropriate output directory, treat generated plan and media files as confidential, and remove local artifacts when they are no longer needed. <br>
Risk: ffmpeg assembly can overwrite the selected output MP4 path. <br>
Mitigation: Confirm the output directory and filename before assembly, especially when reusing an existing project folder. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/illustrated-story-reel) <br>
- [Illustrated story reel API reference](references/illustrated-story-reel-api.md) <br>
- [Illustrated story reel staged gates](references/illustrated-story-reel-gates.md) <br>
- [Illustrated story reel p-video motion](references/illustrated-story-reel-p-video-motion.md) <br>
- [Illustrated story reel positive still prompts](references/illustrated-story-reel-prompts.md) <br>
- [Illustrated story reel quality gates](references/illustrated-story-reel-quality.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Configuration, Shell commands] <br>
**Output Format:** [Markdown guidance with JSON story-plan templates and inline shell/API command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create plan.json, still images, audio files, optional motion clips, and story_reel.mp4 under the selected output directory.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata, SKILL.md frontmatter, skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
