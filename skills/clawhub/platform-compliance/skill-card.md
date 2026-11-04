## Description:

Checks product images against configurable marketplace listing rules and can repair measurable background, framing, resolution, and file-size issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and listing teams use this skill to check product images against Amazon, TikTok Shop, Temu, Shopee, Shopify, and Taobao requirements before upload, review rejection risks, and optionally save adjusted copies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace image rules can change, and the bundled checks cover only measurable portions of each platform's requirements.

Mitigation: Check the platform's current official guidance and provide updated thresholds with --rules when needed.

Risk: Pixel checks cannot determine whether an image contains text, a watermark, a collage, or a damaged product; geometric and color repairs do not correct those content issues.

Mitigation: Review those issues with a visual inspection or a suitable visual review skill, then recheck any repaired copy.

Risk: Optional cloud-generation helpers may upload supplied images and prompts to a provider and may incur charges.

Mitigation: Choose the provider explicitly and preview requests with --dry-run before cloud generation.

## Reference(s):

- [Platform image specifications](references/platform-specs.md)
- [Provider CLI reference](references/provider-cli.md)
- [Related visual review skill: detect-task](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/detect-task/skill.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Image files]

**Output Format:** [Pass or rejection-risk reports in text or JSON, plus optional repaired image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports individual or batch image checks; repaired copies are saved to a chosen output directory.]

## Skill Version(s):

1.0.28 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
