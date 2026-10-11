## Description:

Guides the creation of ecommerce outfit images by combining up to eight product photos on one model while aiming to preserve each item's appearance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and creative teams use this skill to prepare prompts and image-generation commands for coordinated product outfit photos, with optional pose and model references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product, prompt, and optional model or reference images are sent to the selected cloud provider.

Mitigation: Use only images authorized for cloud processing, check configured provider credentials, and avoid private or internal image URLs.

Risk: Generated outfits can omit items or change colors, patterns, or layering.

Mitigation: Review each result against every input image before publication; revise the prompt or regenerate when details differ.

Risk: Image-generation requests may incur provider charges.

Mitigation: Check the proposed request and estimated cost with --dry-run before generating images.

## Reference(s):

- [ClawHub image-fusion skill](https://clawhub.ai/dlazyai/skills/image-fusion)
- [Provider CLI and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with prompt and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands generate local ecommerce images through the selected cloud provider; results require visual review for product fidelity.]

## Skill Version(s):

1.0.19 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
