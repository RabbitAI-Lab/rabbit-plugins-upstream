## Description:

Turns storyboard scenes, dialogue, and video prompts into a canvas-ready video-generation pipeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn storyboard details into a canvas pipeline with shared scene assets and per-scene audio and video generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image-generation instructions go beyond the stated storyboard-to-canvas purpose.

Mitigation: Review the full workflow before installing and approve only the generation steps you intend to run.

Risk: Using the external CLI can send prompts and referenced media to dLazy services and store an API key locally.

Mitigation: Use only with content you are authorized to share, review CLI actions before execution, and protect or revoke the API key when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Configuration instructions, Guidance, Shell commands]

**Output Format:** [JSON canvas pipeline and Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defines shared audio and image inputs and per-storyboard voice-clone and video nodes; separate image-generation instructions request user confirmation before each command.]

## Skill Version(s):

1.2.28 (source: ClawHub release metadata; embedded skill frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
