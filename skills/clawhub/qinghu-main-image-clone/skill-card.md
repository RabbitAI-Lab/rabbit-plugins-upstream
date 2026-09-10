## Description:

Generates ecommerce product main images by using a best-selling reference image and the user's product image to reproduce composition and visual style while avoiding copied brands, logos, and watermarks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and marketing teams use this skill to create product main-image variants that match the layout and visual style of a reference competitor or best-selling image. The workflow guides an agent through Qinghu qhkit image generation, option selection, cost estimation, and result delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to install or update an unpinned third-party global CLI.

Mitigation: Install only after trusting the Qinghu service and @iqinghu/qhkit package; prefer a local or pinned install where possible.

Risk: The workflow may handle API tokens for Qinghu image generation.

Mitigation: Use limited or revocable tokens and avoid pasting production tokens into commands or logs.

Risk: Product and reference images may be uploaded to an external service.

Mitigation: Review which images will be uploaded before running generation, especially for confidential product assets.

Risk: Reference-based main-image generation can copy protected brand elements if prompts are not constrained.

Mitigation: Keep the prompt constraint that generated images should not include the reference product, brand name, logo, or watermark.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-main-image-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, text]

**Output Format:** [Markdown guidance with bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and actual credit usage from the qhkit CLI.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
