## Description:

Creates slideshow stories with narration or music using illustrated frames, Ken Burns movement, and optional gentle p-video motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan and produce illustrated story reels with staged approval gates for story beats, stills, audio, optional motion clips, and final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence flags unpinned auto-install commands that use npx and the skills CLI with automatic confirmation.

Mitigation: Review and preferably pin or manually verify the skills CLI and each referenced Pruna skill before installation; avoid -y when a confirmation step is needed.

Risk: Prompts, narration, and media may be sent to Pruna and Replicate services during generation.

Mitigation: Use non-sensitive prompts and media unless external service processing is acceptable for the project.

Risk: API keys are required for Pruna and Replicate-backed generation.

Mitigation: Keep credentials scoped, avoid exposing them to broad subagent trees, and pass them only to approved still or TTS lanes when needed.

Risk: Local ffmpeg assembly can overwrite the output MP4.

Mitigation: Confirm the output directory and file name before assembly because the documented ffmpeg command uses -y.

Risk: The workflow can trigger paid API usage for stills, audio, and optional video.

Mitigation: Use the documented approval gates before TTS, music, video, and assembly phases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/illustrated-story-reel)
- [Illustrated story reel API reference](artifact/references/illustrated-story-reel-api.md)
- [Illustrated story reel staged gates](artifact/references/illustrated-story-reel-gates.md)
- [Illustrated story reel p-video motion](artifact/references/illustrated-story-reel-p-video-motion.md)
- [Illustrated story reel positive still prompts](artifact/references/illustrated-story-reel-prompts.md)
- [Illustrated story reel quality gates](artifact/references/illustrated-story-reel-quality.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON plan templates, shell command examples, and generated media file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides staged creation of plan.json, stills, audio, optional clips, and story_reel.mp4 with approval gates between paid or irreversible phases.]

## Skill Version(s):

1.0.12 (source: server release and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
