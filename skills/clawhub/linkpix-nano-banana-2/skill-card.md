## Description:

Guides e-commerce teams in creating and editing product and advertising images with Nano Banana 2 through the qhkit image service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers, marketers, and designers use this skill to plan and generate product images, ad creatives, and image edits from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install Node/npm tools and store a qhkit API token.

Mitigation: Review installations and configure the token only for the intended qhkit account; keep the token private.

Risk: Reference images are uploaded to the image-generation service.

Mitigation: Confirm that the images may be shared with the service before uploading them.

Risk: Image-generation requests consume paid credits.

Mitigation: Check the model, image count, and credit estimate, and obtain explicit approval before generating.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-nano-banana-2)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [qhkit API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports estimated credits before approval and actual credits after generation.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
