## Description:

Enhances blurred garment material in ecommerce images by using a high-resolution product reference to reconstruct realistic texture while preserving composition, subject, background, color, and silhouette.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce creators and developers use this skill to post-process garment photos whose fabric detail is blurred, supplying the original image and a high-resolution same-product reference so an image model can restore material texture without changing the scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and local images to the selected cloud provider for image generation or editing.

Mitigation: Use only images that the user is authorized to upload, and confirm the selected provider before execution.

Risk: The bundle includes broader generation tasks and provider paths beyond the stated material-enhancement purpose.

Mitigation: Prefer explicit `--task material-enhancement` and avoid unrelated tasks such as watermark removal or text/video generation unless separately reviewed.

Risk: Material reconstruction can alter identity, background, garment color, or silhouette if the prompt is underspecified.

Mitigation: Use the skill's constraints to lock non-garment regions, preserve color and silhouette, and compare source, reference, and output before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI Reference](references/provider-cli.md)
- [gpt-image-2 Model Flags](references/model-flags.md)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [Material Enhancement Source Image Example](https://raw.githubusercontent.com/dlazyai/ecommerce-skills/main/docs/material-enhancement/source-image.jpg)
- [Material Enhancement Reference Image Example](https://raw.githubusercontent.com/dlazyai/ecommerce-skills/main/docs/material-enhancement/hires-product.jpg)
- [Material Enhancement Output Example](https://raw.githubusercontent.com/dlazyai/ecommerce-skills/main/docs/material-enhancement/example-output.jpg)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with CLI commands and saved image outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or saves enhanced image files through a selected cloud image provider; dry-run and JSON output modes are available through the bundled generator.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
