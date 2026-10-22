## Description:

Generates high-quality videos with Kling v3 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to request Kling v3 text-to-video or image-to-video generation through dLazy. They can specify a prompt, reference images, aspect ratio, duration, mode, and sound, then receive a generated video result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy, and local media may be uploaded for generation.

Mitigation: Upload only media intended to be shared with the service.

Risk: Generation uses service credits, and the CLI stores the organization API key locally.

Mitigation: Protect the saved API key and check generation costs before submitting requests.

Risk: Installing a pinned CLI introduces third-party software into the environment.

Mitigation: Review the pinned CLI before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy service](https://dlazy.com)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video asset URL with a JSON result envelope; optionally saved as a local video file.]

**Output Parameters:** [Prompt, up to two reference images, aspect ratio, duration, generation mode, and sound setting.]

**Other Properties Related to Output:** [Supports synchronous or asynchronous generation and an optional local save path.]

## Skill Version(s):

1.3.33 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
