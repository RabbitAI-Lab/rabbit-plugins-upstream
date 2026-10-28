## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a plan-first, render-later workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators use the skill to turn briefs for film, advertising, short video, and educational narratives into structured storyboards. It guides requirements and character review, script approval, sequential image generation, and final storyboard export.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's hosted service, and selected local media is uploaded for model processing.

Mitigation: Proceed only when comfortable sharing the prompts and media with dLazy; review each image-generation request before approving it.

Risk: The CLI uses an API key, and the skill documentation contains a stale CLI version reference.

Mitigation: Protect the locally saved API key or use the documented DLAZY_API_KEY environment variable, and verify that the CLI install uses version 1.2.3.

## Reference(s):

- [dLazy CLI repository (linked by the skill)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Image generation prompts, Generated images and image URLs, Storyboard guidance]

**Output Format:** [Structured storyboard plans, panel scripts, prompts, and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sequential workflow with user approval gates before image generation and between images]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
