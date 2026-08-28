## Description:

Use when someone wants a slideshow story with narration or music: picture-book illustrated frames with Ken Burns or gentle p-video motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to plan and generate illustrated story reels with per-beat stills, narration or music, optional gentle p-video motion, and local ffmpeg assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses Pruna and Replicate credentials and may upload prompts or generated media to those services.

Mitigation: Confirm service use before installing, keep API keys in controlled environment variables, and avoid exposing credentials in prompts or broad subagent contexts.

Risk: Local ffmpeg assembly can overwrite the chosen output MP4 path.

Mitigation: Confirm the output directory and filename before assembly and keep backups of files that should not be replaced.

Risk: Plan files and generated media can contain confidential prompts, narration, or project details.

Mitigation: Store outputs in an appropriate directory, limit sharing, and remove plan or media artifacts when they are no longer needed.

Risk: Paid media generation phases can incur cost before the final reel is assembled.

Mitigation: Use the documented approval gates before stills, audio, optional p-video clips, and final assembly.

## Reference(s):

- [Illustrated story reel - API reference](artifact/references/illustrated-story-reel-api.md)
- [Illustrated story reel - staged gates](artifact/references/illustrated-story-reel-gates.md)
- [Illustrated story reel - p-video motion](artifact/references/illustrated-story-reel-p-video-motion.md)
- [Illustrated story reel - positive still prompts](artifact/references/illustrated-story-reel-prompts.md)
- [Illustrated story reel - quality gates](artifact/references/illustrated-story-reel-quality.md)
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/illustrated-story-reel)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON planning templates, shell command examples, API call patterns, and generated media file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce plan JSON and paths for stills, audio, optional clips, and the assembled story_reel.mp4 after user approval gates.]

## Skill Version(s):

1.0.10 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
