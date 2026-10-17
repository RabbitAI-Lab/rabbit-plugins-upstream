## Description:

Guides agents to remove unwanted people, text, watermarks, or clutter from product photos and fill the background using LinkPix image editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to clean up product photos by removing specified elements and generating a plausible replacement background.

### Deployment Geography for Use:

Global (requires access to the iqinghu.com China service)

## Known Risks and Mitigations:

Risk: Selected product images are uploaded to the qhkit/iqinghu service for editing, and use requires an access token.

Mitigation: Confirm the images are appropriate to share with the service and configure the token securely.

Risk: Installing or updating the CLI can introduce supply-chain exposure or persistent environment changes.

Mitigation: Prefer a reviewed or pinned qhkit version and avoid permanent PATH or shell-startup changes unless intended.

Risk: Generative retouching can change product details, text, or logos while replacing backgrounds.

Mitigation: Visually compare edited images against the originals and verify important product details before publication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-image-eraser)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with CLI examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Edited image URLs are returned by the service; review output before use.]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
