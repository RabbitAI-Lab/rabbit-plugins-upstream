## Description:

Checks product listing images against platform specifications, reports rejection risks, and optionally saves corrected images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and content teams check product images before listing them on Amazon, TikTok Shop, Temu, Shopee, Shopify, or Taobao, and can save corrected images for measurable specification failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional image generation can send prompts and images to external AI providers.

Mitigation: Use the local Python compliance checker for checks; run provider-backed generation only when intended and approved for the images and prompts involved.

## Reference(s):

- [Platform image specifications](references/platform-specs.md)
- [Provider and data-flow reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Image files]

**Output Format:** [Plain-text or JSON compliance reports; optional corrected JPEG images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports measured values and rejection risks; corrections are saved separately. Text, watermarks, and image quality need separate review.]

## Skill Version(s):

1.0.23 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
