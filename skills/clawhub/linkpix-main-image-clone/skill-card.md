## Description:

Generates ecommerce main-image variants by analyzing a popular reference image and applying its composition and visual style to the user's product image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and ecommerce designers use this skill to create product main images that echo a reference image's style while substituting their own product and copy. It guides an agent through qhkit setup, option checks, cost estimation, user confirmation, image generation, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit or Node and make persistent changes to the host environment.

Mitigation: Install only in an environment where those package changes are acceptable, and review install or upgrade commands before execution.

Risk: The skill can reuse local qhkit service credentials and submit paid image-generation jobs.

Mitigation: Confirm the token or account in use and preserve the required estimate and explicit approval step before any paid generation.

Risk: Generated ecommerce images may copy protected brand elements or introduce inaccurate product details.

Mitigation: Keep prompts limited to style and layout transfer, avoid reproducing reference products, brands, logos, or watermarks, and review generated images for text, logo, and product-structure accuracy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-main-image-clone)
- [@iqinghu/qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit image-generation commands, setup guidance, confirmation steps, and generated image URLs when generation succeeds.]

## Skill Version(s):

0.1.1 (source: server release metadata, released 2026-08-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
