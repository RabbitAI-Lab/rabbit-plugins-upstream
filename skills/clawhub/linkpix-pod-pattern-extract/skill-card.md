## Description:

Helps users extract a garment print from a product photo into a flat, high-resolution, white-background pattern image for POD and apparel design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

POD creators and apparel designers use this skill to turn prints visible on clothing or product photos into reusable, flat pattern images. The generated image should be checked against the original before reuse.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI or Node runtime and changing PATH or shell startup files affects the host.

Mitigation: Get explicit approval before installation, downloads, or PATH changes; prefer pinned package versions and remove temporary configuration when finished.

Risk: Using the service uploads source images and requires an API token that may be stored locally.

Mitigation: Confirm the user trusts the service and approves the upload and token setup; protect the token and remove it when no longer needed.

Risk: Generated patterns may differ from the source or reproduce protected branding and artwork.

Mitigation: Check key visual details and rights to reuse the source artwork before publishing the result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-extract)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix POD workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Markdown with CLI examples and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [White-background raster patterns, not vector or transparent files; generative redrawing may change details.]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
