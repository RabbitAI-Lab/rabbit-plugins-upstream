## Description:

Helps agents adapt one ecommerce product asset set into region-specific listing copy, size conversion tables, compliance-label reminders, and marketplace image variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace sellers, ecommerce operators, and developers use this skill to localize product assets for cross-border listings, including regional copy, image-generation prompts, size conversions, and platform checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts may be uploaded to configured generation providers.

Mitigation: Use dry-run mode to inspect requests first, avoid sensitive images, and choose only providers acceptable for the product data.

Risk: Compliance and marketplace-fit checks are review aids, not final legal or platform approval.

Mitigation: Confirm regional requirements against current official marketplace rules and professional compliance guidance before publishing.

Risk: Generated non-English listing text or image text can contain localization errors.

Mitigation: Have native speakers or qualified reviewers check customer-facing copy and prefer generating no-text base images before final layout.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/cross-border-localize)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI reference](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands; scripts can emit JSON status and generated image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload selected prompts and product images to configured generation providers and write generated assets to local output paths.]

## Skill Version(s):

1.0.8 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
