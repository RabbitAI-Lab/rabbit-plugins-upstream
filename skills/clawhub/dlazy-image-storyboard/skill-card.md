## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict plan-first, render-later flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and production teams use the skill to turn creative briefs into film, advertising, short-video, and educational storyboards. It structures requirements, characters, scripts, and image-generation steps with approval gates before rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires dLazy CLI authentication, and the scanner notes that some references could not be resolved, leaving its security evidence incomplete.

Mitigation: Review the linked CLI and service references, verify the dLazy authentication flow through official channels, and decide whether to provide an API key before use.

Risk: Prompts and parameters are sent to dLazy hosted services, and local image, video, or audio files may be uploaded for processing.

Mitigation: Avoid submitting sensitive material; review dLazy's data-handling terms and obtain any required consent before sending prompts or media.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Storyboard scripts, Image-generation prompts, Generated image URLs]

**Output Format:** [Markdown with structured storyboard panels and image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific storyboard specs; workflow stages include user approval before image generation.]

## Skill Version(s):

1.3.42 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
