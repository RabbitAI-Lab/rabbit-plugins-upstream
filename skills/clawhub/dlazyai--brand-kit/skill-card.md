## Description:

Helps ecommerce teams define a reusable brand specification so product images stay visually consistent across SKUs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce teams and designers use a shared brand configuration to keep model appearance, lighting, composition, layout, and visual tone consistent across product images and batches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to an external image-generation provider.

Mitigation: Check which provider is selected and only use images for which you have rights and consent.

Risk: Image generation may incur provider costs or use an unintended provider.

Mitigation: Run --dry-run to review the selected provider, request, and estimated cost before generating.

Risk: A missing model reference image can reduce consistency across generated product images.

Mitigation: Confirm the reference file exists and review warnings before running a full batch.

## Reference(s):

- [Brand Kit release](https://clawhub.ai/dlazyai/skills/brand-kit)
- [Brand configuration fields](artifact/references/brand-schema.md)
- [Provider and generation guidance](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Configuration guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance, YAML configuration, and optional generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can preview brand prompt additions and generation costs before creating images.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
