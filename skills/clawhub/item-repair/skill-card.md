## Description:

Helps turn casual product photos into catalog-ready images by removing incidental wrinkles, improving alignment and lighting, and cleaning up backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and catalog teams use this skill to retouch photos of a single product for listings, including garment flat lays, while preserving design details and visible defects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled runner has broader cloud-generation and remote-image fetching capabilities than product retouching requires; private photos and prompts may leave the user's environment.

Mitigation: Review before installing, use only an approved cloud provider with the necessary credentials, prefer local image files over arbitrary URLs, and preview requests with dry-run before submitting sensitive assets.

Risk: Retouching may alter product construction or conceal visible flaws, misleading shoppers.

Mitigation: Compare results with source photos; preserve structural folds, color, hardware, and visible damage, and reject edits that hide defects.

## Reference(s):

- [Item Repair release on ClawHub](https://clawhub.ai/dlazyai/skills/item-repair)
- [Image model options](references/model-flags.md)
- [Provider and output reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and command examples; generated JPEG, PNG, or WebP images when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts one to four views of the same product; supports a dry-run preview and comparison against original images.]

## Skill Version(s):

1.0.19 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
