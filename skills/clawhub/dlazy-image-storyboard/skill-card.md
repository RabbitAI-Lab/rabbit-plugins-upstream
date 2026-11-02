## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Film, advertising, short-video, and education creators use the skill to turn a creative brief into a storyboard through staged requirements, character, script, and image reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's cloud service, and image generation may incur charges.

Mitigation: Explain the cloud processing and possible charges, and get user approval before each generation using content the user approves for transfer.

Risk: Logging in stores an API key in the local dLazy CLI configuration.

Mitigation: Use a trusted device, protect the local configuration, and rotate or revoke the key if it may have been exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI project link (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Image generation requests]

**Output Format:** [Markdown storyboard plans and panel prompts, with generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stepwise workflow with explicit approval gates; image generation is performed one command at a time.]

## Skill Version(s):

1.3.38 (source: server-resolved release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
