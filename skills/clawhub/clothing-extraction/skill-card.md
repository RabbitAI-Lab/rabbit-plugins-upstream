## Description:

Turns photos of worn clothing into clean, white-background flat-lay product images, one item at a time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Retailers and product-image creators use the skill to isolate clothing from model, street-style, or customer photos and make flat-lay images for listings or subsequent image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and prompts are sent to the selected external image provider.

Mitigation: Avoid sensitive, private, or non-consensual photos; use scoped, revocable API keys.

Risk: Customer or competitor photos may carry usage or branding rights restrictions.

Mitigation: Confirm rights to use source imagery and do not remove another party's branding to misrepresent a product.

Risk: Hidden garment details are inferred rather than recovered from the photo.

Mitigation: Review generated colors, patterns, and occluded details against the original before publishing.

## Reference(s):

- [Clothing Extraction release](https://clawhub.ai/dlazyai/skills/clothing-extraction)
- [Provider and authentication guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and JPEG or PNG flat-lay images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One image per item; verify inferred details in occluded areas.]

## Skill Version(s):

1.0.17 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
