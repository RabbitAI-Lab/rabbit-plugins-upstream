## Description:

Transforms plain or white-background product photos into photorealistic lifestyle scene images while preserving the product's shape, color, material, logo, perspective, shadows, and reflections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce sellers, marketplace operators, and creative teams use this skill to place product images into plausible commercial scenes for listing and marketing assets. It helps agents produce grounded prompts, commands, and configuration for background replacement while avoiding changes to the product itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts may be processed by cloud providers.

Mitigation: Use only providers approved for the product data, and avoid sending confidential product images unless cloud processing is acceptable.

Risk: A configured endpoint or binary override can route credentials and images to an untrusted service.

Mitigation: Use trusted provider settings, avoid untrusted ARK_BASE_URL or DLAZY_BIN values, and review the environment before execution.

Risk: API keys are required for some providers.

Mitigation: Use scoped, revocable credentials and rotate or revoke keys if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter list](references/model-flags.md)
- [dLazy](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and optional JSON from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or save generated image files through configured cloud image providers when the commands are executed.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
