## Description:

Helps agents create and edit images for e-commerce and marketing, including product shots, posters, background removal, retouching, and upscaling through AdsTurbo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adsturbo](https://clawhub.ai/user/adsturbo)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to generate product images and campaign visuals, edit existing images, and prepare image assets for online storefronts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Removing watermarks, logos, credits, or other provenance marks could misrepresent ownership.

Mitigation: Use removal tools only for content the user owns or is explicitly authorized to alter.

Risk: Uploading local files may make sensitive assets externally accessible.

Mitigation: Confirm the user accepts external accessibility before uploading, and avoid sensitive files.

Risk: Prompts and image URLs are sent to AdsTurbo for processing.

Mitigation: Share only prompts and URLs the user is comfortable sending to AdsTurbo.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/adsturbo/skills/adsturbo-image)
- [Image operations and model capabilities](references/image.md)
- [Asset upload guidance](references/upload.md)
- [Async work status guidance](references/work.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are shared as result URLs; requests require an AdsTurbo API key and may use paid credits.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
