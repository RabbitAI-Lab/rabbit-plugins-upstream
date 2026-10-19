## Description:

Retouches product photos for catalog use by reducing incidental wrinkles, improving layout and lighting, and cleaning backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and content teams use this skill to prepare product photos for listings, including flat-lay clothing retouching and wrinkle removal without intentionally changing product attributes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected cloud provider.

Mitigation: Confirm the provider and its data terms before sending images; avoid confidential photos unless authorized.

Risk: Retouching can unintentionally change product features or conceal defects.

Mitigation: Compare edited images with originals and reject any changes to structure, color, labels, damage, or intentional folds.

Risk: Ambiguous requests or paid image generation may produce unwanted edits or charges.

Mitigation: Confirm editing intent for vague requests and use dry-run or doctor mode to check configuration before running.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider CLI guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Images]

**Output Format:** [Markdown instructions and commands; edited image files when run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports one to four views of the same product and saves edited images locally.]

## Skill Version(s):

1.0.23 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
