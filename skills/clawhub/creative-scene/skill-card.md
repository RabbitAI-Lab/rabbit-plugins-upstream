## Description:

Generates creative ecommerce-style images from a text prompt, optionally using a reference image to change a model, pose, or outfit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and developers use this skill to draft prompts and commands for text-to-image scene generation and targeted edits to a model, pose, or outfit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to external generation providers.

Mitigation: Use approved providers and scoped API keys, and avoid submitting confidential prompts, private product images, or sensitive personal images.

Risk: Reference images and generated assets may be fetched from unvalidated URLs.

Mitigation: Use trusted local image paths or known public URLs, and run the skill away from networks with sensitive internal HTTP services.

Risk: A custom ARK_BASE_URL can direct credential-bearing requests to a non-default endpoint.

Mitigation: Leave ARK_BASE_URL unset unless the endpoint is fully trusted, and isolate the environment to only the credentials required for the selected provider.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [banana-pro parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with command examples; generation commands can save JPEG image files or return JSON envelopes when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports text-only generation, optional reference images, selectable aspect ratio and image size, and batch generation.]

## Skill Version(s):

1.0.8 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
