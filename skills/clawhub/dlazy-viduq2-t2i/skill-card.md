## Description:

Generate high-quality images with Vidu Q2 from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can generate or edit images with Vidu Q2 through dLazy's hosted service. They provide a text prompt and optionally reference images, then receive generated image URLs or save the images locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to dLazy's hosted service, and generation uses service credits.

Mitigation: Submit only content approved for external processing; review the cost estimate before running generation.

Risk: The external CLI package and its claimed API-key file permissions were not independently verified.

Mitigation: Review the dependency before installation and protect the stored organization key, or use the documented environment-variable option.

## Reference(s):

- [dLazy service](https://dlazy.com)
- [CLI project page](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Image files, JSON, Shell commands]

**Output Format:** [Generated image URLs or saved image files with JSON task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, up to 10 reference images, and configurable aspect ratio and resolution.]

## Skill Version(s):

1.3.37 (source: ClawHub release metadata in evidence.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
