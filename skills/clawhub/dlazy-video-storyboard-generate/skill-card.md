## Description:

Turns storyboard scenes into a video-generation pipeline for a canvas and guides step-by-step media generation through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to map storyboard dialogue and scene prompts into a canvas-ready audio, image, and video pipeline, then generate media one step at a time with user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls for installing or running a CLI and keeping a dLazy API key; its short description does not make these requirements clear.

Mitigation: Review the CLI package before installing globally; prefer one-off npx usage and an environment variable for the API key when appropriate.

Risk: Prompts and referenced media may be sent to dLazy services, and the workflow can modify a canvas.

Mitigation: Confirm the intended media, data sharing, and canvas changes with the user before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-storyboard-generate)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON configuration, Shell commands, Guidance]

**Output Format:** [JSON pipeline and Markdown guidance with shell commands and media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Canvas pipeline shares source audio and scene image across storyboard scenes; generated audio and video are per scene.]

## Skill Version(s):

1.2.30 (source: ClawHub release metadata; artifact frontmatter says 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
