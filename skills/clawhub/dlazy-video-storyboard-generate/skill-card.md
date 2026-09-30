## Description:

Turns storyboard scenes into a video-generation pipeline with shared source media and per-scene audio and video nodes for a canvas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to organize storyboard dialogue and scene prompts into a canvas-ready video pipeline, with optional dLazy media generation after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files can be sent to dLazy cloud services.

Mitigation: Review prompts and files for sensitive information before approving uploads.

Risk: The skill can draw pipeline nodes on the canvas and run a media-generation command.

Mitigation: Inspect proposed canvas changes and approve each generation command individually.

Risk: A dLazy API key may be stored in local configuration.

Mitigation: Prefer a revocable key or a per-run environment variable when persistent credentials are undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (linked in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Guidance]

**Output Format:** [Canvas-ready JSON pipeline and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shared source audio and scene image, with per-storyboard cloned audio and video nodes; media URLs may be returned after generation.]

## Skill Version(s):

1.2.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
