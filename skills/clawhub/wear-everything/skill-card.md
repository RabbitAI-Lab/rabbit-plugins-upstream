## Description:

Generates on-model product images by placing shoes, bags, and accessories from product photos onto a reference model while aiming to preserve product details and the surrounding scene.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and product photographers use this skill to create on-model accessory imagery from product and model-reference photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and model-reference photos and prompts are sent to the configured image provider.

Mitigation: Use only approved providers and images for which you have permission; avoid sensitive personal photos without consent.

Risk: Image generation may incur charges and alter model likeness or product details.

Mitigation: Run a dry-run to check requests and costs, then review generated images for accuracy before use.

Risk: Untrusted provider settings or executable overrides could redirect image data or execution.

Mitigation: Set provider environment variables and DLAZY_BIN only to trusted values.

## Reference(s):

- [Provider CLI and data flow reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/wear-everything)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with command examples and image-generation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can save generated product images locally; review results before publication.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
