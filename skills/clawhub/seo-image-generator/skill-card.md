## Description:

Generate visual asset prompts for SEO landing pages — banner (16:9, image-to-image with logo), product introduction (1:1), why choose (1:1), and pain points (1:1). Then optionally execute batch generation via image generation service. This skill should be used after page-seo-generator produces the 11-column SEO content, to create matching visual materials for the page.

This skill is ready for commercial/non-commercial use.

## Publisher:

[notegpt-official](https://clawhub.ai/user/notegpt-official)

### License/Terms of Use:

MIT-0

## Use Case:

External users creating SEO landing pages use this skill to write prompts for branded banners and unbranded product, comparison, and problem-solution images, then optionally generate image batches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Banner generation uploads the user's logo to an image-generation service.

Mitigation: Use only a logo you are authorized to share, and review the service's data-handling terms before uploading it.

Risk: Generated images may contain inaccurate text or product details if published without review.

Mitigation: Check the text, brand details, and product claims in each image against the source page before publishing.

## Reference(s):

- [Source repository (server-resolved provenance)](https://github.com/notegpt-official/notegpt-skills/tree/main/skills/seo/seo-image-generator)
- [ClawHub skill release](https://clawhub.ai/notegpt-official/skills/seo-image-generator)
- [SEO Page Image Prompt Templates](artifact/references/prompt-templates.md)

## Skill Output:

**Output Type(s):** [Text, Image prompts, Image files]

**Output Format:** [English-language image prompts and optionally generated image files, grouped by image type]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers one 16:9 banner and three 1:1 image types; banner generation requires a logo reference. Image generation is optional.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
