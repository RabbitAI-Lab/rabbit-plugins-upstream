## Description:

Generates and edits images from text prompts or reference images with Nano Banana 2.0.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can create or edit images with text prompts and optional reference images, then save generated image assets locally or use returned image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to dLazy cloud services, and generation may incur credit charges.

Mitigation: Submit only prompts and images you are comfortable sharing with dLazy, and review costs before generation.

Risk: CLI login stores an API key in local configuration, and the skill depends on an external CLI.

Mitigation: Review the CLI before installing; use the documented environment-variable option for temporary authentication when preferred.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image files, JSON, Shell commands]

**Output Format:** [Generated image assets (PNG) and structured JSON results or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text prompts, up to 14 reference images, aspect-ratio and image-size options, and optional local saving.]

## Skill Version(s):

1.3.32 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
