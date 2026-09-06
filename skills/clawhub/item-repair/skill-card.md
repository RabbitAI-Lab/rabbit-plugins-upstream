## Description:

商品精修、去褶皱。随手拍的商品图 → 可直接上架的精修图。当用户说「精修」「去褶皱」「修图」「拍得不好看」「整理一下」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and ecommerce teams use this skill to turn casual product photos into listing-ready images by reducing wrinkles, aligning layout, evening lighting, and preparing clean backgrounds while preserving product style, color, hardware, and structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts may be sent to dLazy or another configured external provider.

Mitigation: Use the skill only with images and URLs suitable for external processing, keep provider API keys scoped, and review provider data handling before production use.

Risk: The bundled shared generator can run tasks beyond the advertised item-repair workflow.

Mitigation: Prefer the item-repair task path, use --dry-run first, and audit or constrain the generator if only item-repair behavior is intended.

Risk: Retouching may hide product defects or alter product appearance in ways that misrepresent a listing.

Mitigation: Compare outputs against the source images and require prompts that preserve structure, color, hardware, intentional folds, and real defects.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated image files locally through the configured image provider.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
