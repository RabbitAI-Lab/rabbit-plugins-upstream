## Description: <br>
Use when someone wants a slideshow story with narration or music, using picture-book illustrated frames with Ken Burns or gentle p-video motion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to plan and generate illustrated story reels with staged approval gates for stills, audio, optional p-video motion, and final MP4 assembly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls can incur cost during still, audio, and optional p-video phases. <br>
Mitigation: Use the documented approval gates before TTS, music, video, and assembly steps. <br>
Risk: API credentials may be exposed if broadly shared with subagents or logs. <br>
Mitigation: Keep PRUNA_API_KEY and REPLICATE_API_TOKEN scoped to the parent agent or approved per-lane work only. <br>
Risk: Local ffmpeg assembly may overwrite an existing MP4 at the target path. <br>
Mitigation: Use a dedicated output directory and confirm the final MP4 path before assembly. <br>
Risk: Plan files and generated media may contain confidential prompts, narration, or project details. <br>
Mitigation: Treat plan.json and media under the output directory as confidential local files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/illustrated-story-reel) <br>
- [Illustrated story reel API reference](references/illustrated-story-reel-api.md) <br>
- [Illustrated story reel staged gates](references/illustrated-story-reel-gates.md) <br>
- [Illustrated story reel p-video motion](references/illustrated-story-reel-p-video-motion.md) <br>
- [Illustrated story reel positive still prompts](references/illustrated-story-reel-prompts.md) <br>
- [Illustrated story reel quality gates](references/illustrated-story-reel-quality.md) <br>
- [Pruna P-API predictions endpoint](https://api.pruna.ai/v1/predictions) <br>
- [Pruna P-API file upload endpoint](https://api.pruna.ai/v1/files) <br>
- [Replicate predictions endpoint](https://api.replicate.com/v1/models/{owner}/{name}/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with JSON story plans, API payloads, shell commands, and generated media paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces plan.json and staged media under the output directory; final assembly is usually story_reel.mp4.] <br>

## Skill Version(s): <br>
1.0.7 (source: server evidence, release metadata, and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
