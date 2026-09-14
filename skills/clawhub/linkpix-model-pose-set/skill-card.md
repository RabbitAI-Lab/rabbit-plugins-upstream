## Description:

Generates multi-pose and multi-angle clothing model image sets from a single model photo for ecommerce product pages and social media marketing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and agent users use this skill to create consistent pose and angle variations for apparel listings from one model image. It supports workflows such as front, side, back, walking, seated, upper-body, and fabric-detail display images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update an unpinned global npm CLI.

Mitigation: Install only after trusting the @iqinghu/qhkit package and LinkPix service, and prefer a pinned or local install instead of npx or automatic @latest upgrades.

Risk: The workflow requires an API token for the qhkit service.

Mitigation: Provide the token through a secret manager or protected environment variable and avoid pasting it directly into command history.

Risk: Generated clothing images may not preserve every product detail exactly.

Mitigation: Review generated images before publication, especially logos, text, garment structure, and other product-critical details.

## Reference(s):

- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-pose-set)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, image URLs]

**Output Format:** [Markdown with bash command examples and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The qhkit CLI returns one-line JSON and generated image URLs when image generation succeeds.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
