## Description:

Generates vector graphics from text prompts, producing SVG results suitable for logos, icons, and scalable design assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External designers and developers can generate logos, icons, and other scalable visual assets from text prompts. They can choose an aspect ratio and save generated assets locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files explicitly submitted for generation are processed by dLazy.

Mitigation: Submit only prompts and files you are authorized to share with the service.

Risk: Login saves an API key locally, and generation can consume paid credits.

Mitigation: Use the documented environment-variable option if you prefer not to save the key, protect any local configuration containing credentials, and check the cost estimate before generation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4-vector)
- [CLI project information](https://github.com/dlazy-ai/cli)
- [CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image files, Vector graphics]

**Output Format:** [Generated vector graphic (described as SVG and returned as an image result)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-driven; supports an optional aspect ratio and local file saving.]

## Skill Version(s):

1.3.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
