## Description:

Generates high-quality images with Doubao Seedream 4.5 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images through the dLazy CLI, including text-to-image and image-to-image workflows. It is useful when an agent needs hosted image generation, result URLs, or saved image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced images are sent to dLazy hosted services for generation.

Mitigation: Do not submit sensitive prompts or media unless the user is comfortable sharing them with dLazy and its service terms.

Risk: The dLazy API key can be stored in a local CLI config file.

Mitigation: Prefer per-invocation DLAZY_API_KEY for sensitive environments, or verify local config permissions and rotate or revoke keys when needed.

Risk: Image generation may consume paid dLazy credits.

Mitigation: Confirm the user accepts credit usage before generation and surface insufficient-balance errors with recharge guidance.

Risk: --dry-run behavior is under-disclosed for network and upload safety with local media.

Mitigation: Do not rely on --dry-run as a no-network or no-upload control until the CLI behavior is clarified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON result with generated image URLs; optional saved image file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires dLazy API authentication; referenced local images may be uploaded to dLazy media storage; async mode can return a task ID for polling.]

## Skill Version(s):

1.3.11 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
