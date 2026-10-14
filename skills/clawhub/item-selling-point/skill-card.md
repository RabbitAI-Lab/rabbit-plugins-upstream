## Description:

Creates Chinese-language ecommerce hero images with product selling points and promotional callouts from a product photo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and designers use this skill to turn a product photo and verified selling points into a marketplace hero image with readable Chinese copy and a promotional badge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected cloud image provider.

Mitigation: Use non-sensitive product assets and confirm the selected provider before generation.

Risk: Unverified product claims or promotional offers could appear in public marketplace images.

Mitigation: Confirm claims and promotions before publication, and review generated copy for accuracy.

Risk: Generation creates local output files at the specified path.

Mitigation: Choose the save location deliberately and check the result before sharing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/item-selling-point)
- [Provider and CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown instructions and saved ecommerce image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports square or portrait layouts and multiple image candidates; outputs are saved to a chosen local path.]

## Skill Version(s):

1.0.21 (source: SKILL.md frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
