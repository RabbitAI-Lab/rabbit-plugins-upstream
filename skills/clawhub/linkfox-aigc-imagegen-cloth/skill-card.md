## Description:

Generates apparel-focused ecommerce imagery, including ghost mannequin white-background images, model images, lifestyle scene images, selling-point images, A+ images, and size-chart images, either as single outputs or planned image sets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and agents use this skill to turn apparel reference images into product visuals for listings, merchandising, and marketing workflows. It supports both direct single-image generation and multi-image set planning for common apparel commerce formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill needs review because it mixes external skill installation with under-scoped likeness, upload, and script-execution behavior.

Mitigation: Review the skill before installing or running it, and do not allow onboarding ZIP installation unless that package and source have been separately trusted.

Risk: Product, model, or reference images may be sent to Linkfox services.

Mitigation: Use only images the operator is allowed to upload to Linkfox services, and avoid reference photos unless the operator has the necessary likeness rights.

Risk: Generated size-chart data may be inaccurate or unsuitable for a final listing.

Mitigation: Manually verify generated size data before publishing or using it in customer-facing commerce materials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-imagegen-cloth)
- [Linkfox guide](https://skill.linkfox.com/linkfoxskills/guide.htm)
- [Runtime collection index](references/runtime/00-index.md)
- [Image delivery protocol](references/runtime/03-deliver.md)
- [White-background apparel image reference](references/types/white-bg.md)
- [Model apparel image reference](references/types/model-image.md)
- [Lifestyle scene apparel image reference](references/types/scene.md)
- [Selling-point apparel image reference](references/types/selling-point.md)
- [A+ apparel image reference](references/types/aplus.md)
- [Size-chart apparel image reference](references/types/size.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, JSON, Image files, Guidance]

**Output Format:** [Markdown with inline image references, JSON status or manifest files, and generated image file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Linkfox text and image generation services, require uploaded or public apparel image URLs, and produce intermediate planning files for multi-image sets.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
