## Description:

Turns garment flat-lay photos and pose references into on-model e-commerce image generation instructions while aiming to preserve garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and creators use this skill to prepare virtual try-on product photography from clothing images and pose or model references, with optional brand-consistent styling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, model references, prompts, and brand details are sent to the selected cloud image provider.

Mitigation: Review the images and brand data before upload; select the provider explicitly and use --dry-run to inspect the request first.

Risk: Generated images could misrepresent a product or use a person's likeness without permission.

Mitigation: Use authorized model references, customize example brand and model defaults, and review garment details before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/flat-lay)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands can save generated product images locally.]

## Skill Version(s):

1.0.23 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
