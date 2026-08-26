## Description:

This skill helps agents use LinkPix/qhkit to generate ecommerce main images that follow the composition and visual style of reference product images while using the user's own product images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, marketers, and ecommerce operators use this skill to create product-listing main images inspired by high-performing reference images. Agents use it to install or configure qhkit, estimate paid generation, request user approval, submit image-generation jobs, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and runs the qhkit npm CLI.

Mitigation: Review the package choice, install source, and local environment before installation.

Risk: The workflow uses a Qinghu/LinkPix API key and uploads product and reference images to that service.

Mitigation: Use an approved API key handling path and confirm the images are appropriate to send to the service before generation.

Risk: Paid generation can consume credits.

Mitigation: Run the estimate action first and submit generation only after the user approves the key parameters and expected credit cost.

Risk: Reference images can include protected assets, logos, watermarks, or branding.

Mitigation: Use references for style and layout only, avoid directly copying protected elements, and review generated outputs before publication.

Risk: Generated images may differ from the intended product details, text, logos, or structure.

Mitigation: Inspect key visual and commercial details before using the generated image in a listing or campaign.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu account and API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline JSON and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit CLI calls, estimate results, approval prompts, and generated image URLs after successful tasks.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
