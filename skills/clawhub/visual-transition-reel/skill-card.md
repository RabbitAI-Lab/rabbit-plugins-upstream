## Description:

Guides an agent through planning, generating, reviewing, and assembling a montage with transitions between composed video clips where narration is optional.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to plan scene anchor pairs, generate start and end stills, render transition clips, and assemble a reviewed multi-scene reel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install examples use unpinned external npx skills add commands.

Mitigation: Install only from a trusted PrunaAI source and prefer pinned versions or reviewed commits when available.

Risk: The workflow can upload image assets to external media-generation services and consume generation credits.

Mitigation: Review prompts, input assets, and phase gates before generation, especially before paid video steps.

Risk: Local media assembly uses ffmpeg on generated or supplied media files.

Mitigation: Run ffmpeg only on trusted local files in a controlled workspace and review generated commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/visual-transition-reel)
- [Example prompt](artifact/example-prompt.md)
- [Transition plan template](artifact/templates/transition-plan.template.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON plan templates and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce scene plans, media-generation prompts, file paths, ffmpeg commands, and review-gated workflow instructions.]

## Skill Version(s):

1.0.13 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
