## Description:

Turns storyboard details into a video-generation pipeline for a canvas, with optional dLazy image-generation steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn storyboard scenes, dialogue, and video prompts into a canvas pipeline with shared scene media and per-scene audio and video steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill combines storyboard canvas setup with broader CLI installation, authentication, and cloud generation instructions.

Mitigation: Review the CLI package before installation and run only the dLazy commands explicitly approved for the task.

Risk: Prompts, parameters, and referenced local media may be sent to dLazy services; login stores an API key locally.

Mitigation: Avoid sending sensitive media or prompts without consent, and protect or rotate the locally stored API key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI project (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Configuration, Guidance, Shell commands]

**Output Format:** [JSON canvas pipeline with Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes shared scene assets and per-storyboard audio and video steps; optional image-generation results may include URLs.]

## Skill Version(s):

1.2.25 (source: ClawHub release metadata; artifact frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
