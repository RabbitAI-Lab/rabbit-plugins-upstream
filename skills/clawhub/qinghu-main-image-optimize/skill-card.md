## Description:

Uses Qinghu AI to redraw e-commerce product images with improved composition, lighting, texture, and detail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and creative teams use the skill to refresh product listing images or generate a coordinated set of new images with Qinghu AI.

### Deployment Geography for Use:

China (Qinghu domestic service)

## Known Risks and Mitigations:

Risk: Broad image-editing triggers could start an unwanted external workflow.

Mitigation: Confirm that the user wants Qinghu image generation before proceeding.

Risk: The workflow uploads local product images to the Qinghu service and may spend credits.

Mitigation: Confirm the images to upload and estimated credit cost before generating.

Risk: Installing or updating qhkit changes the local toolchain; persistent configuration may retain access tokens.

Mitigation: Prefer a pinned, reviewed qhkit version, avoid unrequested persistent PATH changes, and keep tokens scoped and removable.

Risk: Generative redraws can misrepresent product text, logos, or construction.

Mitigation: Review generated images against the source product before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-main-image-optimize)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image links]

**Output Format:** [Markdown with generated image links and credit usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generative redraws may alter product text, logos, or structural details.]

## Skill Version(s):

0.1.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
