## Description:

Use when someone wants a slideshow story with narration or music: picture-book illustrated frames with Ken Burns or gentle p-video motion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to plan and produce illustrated story reels with generated stills, narration or music, optional gentle motion, staged review gates, and local assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generated images, narration, and optional audio may be sent to Pruna or Replicate APIs using the user's API keys.

Mitigation: Review the skill source before installation, use trusted installer paths, and avoid sending confidential material unless external API processing is acceptable.

Risk: Local ffmpeg assembly uses overwrite behavior for the target MP4.

Mitigation: Use a fresh output directory and confirm the output path before assembly.

Risk: Generated plan files and media can contain prompts, narration, and project details.

Mitigation: Treat the output directory as confidential project data and delete local state when it is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pruna-ai/skills/illustrated-story-reel)
- [Illustrated story reel API reference](references/illustrated-story-reel-api.md)
- [Illustrated story reel staged gates](references/illustrated-story-reel-gates.md)
- [Illustrated story reel p-video motion](references/illustrated-story-reel-p-video-motion.md)
- [Illustrated story reel positive still prompts](references/illustrated-story-reel-prompts.md)
- [Illustrated story reel quality gates](references/illustrated-story-reel-quality.md)
- [Pruna P-API predictions endpoint](https://api.pruna.ai/v1/predictions)
- [Pruna P-API file upload endpoint](https://api.pruna.ai/v1/files)
- [Replicate model predictions endpoint](https://api.replicate.com/v1/models/{owner}/{name}/predictions)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with JSON plan templates and inline shell/API command patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a plan and generated media workflow ending in an MP4 story reel under the selected output directory.]

## Skill Version(s):

1.0.13 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
