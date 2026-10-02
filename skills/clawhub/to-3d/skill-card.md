## Description:

Turns flat-lay garment photos into dimensional ghost-mannequin product images while aiming to preserve garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and product-image creators use this skill to turn single-garment flat-lay photos into dimensional, model-free product shots for listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment photos and prompts are sent to the selected cloud image provider.

Mitigation: Avoid private or sensitive images unless the selected provider's data handling is acceptable; confirm provider selection when multiple keys are configured.

Risk: Generation requests may incur costs or produce inaccurate garment details.

Mitigation: Use dry-run to review the request and estimated cost, then inspect the generated image for shape, texture, color and unwanted mannequin elements.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/to-3d)
- [Model flags](references/model-flags.md)
- [Provider CLI and data flow](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and image-generation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Running the commands can save JPEG product images; size, quality, batch size and output path are configurable.]

## Skill Version(s):

1.0.16 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
