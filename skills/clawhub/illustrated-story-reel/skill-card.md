## Description:

Use when someone wants a slideshow story with narration or music, using picture-book illustrated frames with Ken Burns or gentle p-video motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to plan and generate illustrated slideshow stories with narration or music. It supports staged review gates, optional p-video motion, and local ffmpeg assembly into a final story reel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses paid Pruna and Replicate APIs and prerequisite skills.

Mitigation: Confirm the prerequisite skill source is trusted and require the documented approval gates before paid generation phases.

Risk: Generated plans, prompts, narration, and media can contain confidential project details.

Mitigation: Treat plan files and generated media under the output directory as confidential when user inputs include private information.

Risk: Local ffmpeg assembly can overwrite the final MP4 output path.

Mitigation: Verify the output directory and final filename before assembly because ffmpeg is documented to use overwrite behavior.

## Reference(s):

- [Illustrated story reel API reference](artifact/references/illustrated-story-reel-api.md)
- [Illustrated story reel staged gates](artifact/references/illustrated-story-reel-gates.md)
- [Illustrated story reel p-video motion guidance](artifact/references/illustrated-story-reel-p-video-motion.md)
- [Illustrated story reel prompt guidance](artifact/references/illustrated-story-reel-prompts.md)
- [Illustrated story reel quality gates](artifact/references/illustrated-story-reel-quality.md)
- [Vertical story plan template](artifact/templates/story-plan.template.json)
- [Landscape story plan template](artifact/templates/story-plan.landscape.template.json)
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/illustrated-story-reel)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with JSON plan templates, shell commands, API payload patterns, and media file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces plan.json, stills, narration or music audio, optional clips, and story_reel.mp4 under the selected output directory.]

## Skill Version(s):

1.0.11 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
