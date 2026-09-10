## Description:

Generates realistic ecommerce product scene images from product images and scene prompts using LinkPix through the qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and agent users use this skill to generate lifestyle, ambience, and product-in-context marketing images for product detail pages and ads. The agent prepares qhkit commands, estimates credits when needed, runs image generation, and returns generated image URLs with usage cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup and upgrade instructions can install or upgrade unpinned qhkit and Node tooling in the user's environment.

Mitigation: Prefer a pinned, platform-managed qhkit installation; avoid automatic @latest upgrades and npx fallback execution unless the user approves the toolchain change.

Risk: Using the LinkPix service requires a QHKIT token and uploads selected product images to the service.

Mitigation: Provide the token only when the user intends to use LinkPix, and confirm that the selected product images are appropriate to upload.

Risk: Generated scene images may alter product details such as text, logos, or structure.

Mitigation: Review generated outputs for brand, logo, text, and product-structure accuracy before using them in commerce or advertising.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-scene-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline qhkit shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit-generated image URLs, one-line JSON command results, and credit usage summaries.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
