## Description:

A structured workflow skill dedicated to social-media carousel design. The core method is 'decide intent first, then execute,' using a 'single-confirmation + cover-first' two-phase flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to plan social-media carousel slides, confirm a design direction, and guide cover-first image generation followed by the remaining slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags CLI login and API-key setup as a limited concern relative to the carousel-design purpose.

Mitigation: Review the CLI authentication and configuration steps before use; use an API key that can be rotated or revoked.

Risk: Prompts and supplied local media may be sent to dLazy-hosted APIs or media storage during generation.

Mitigation: Avoid submitting sensitive prompts or media unless their transfer to the hosted service is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI information](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Image-generation prompts, Image URLs]

**Output Format:** [Markdown planning and image-generation requests, with generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cover-first, sequential workflow.]

## Skill Version(s):

1.3.44 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
