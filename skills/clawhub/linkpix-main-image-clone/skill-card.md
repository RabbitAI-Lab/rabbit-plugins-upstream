## Description:

Guides agents to use the qhkit CLI to generate ecommerce main product images that adapt the composition, color, lighting, and visual style of a reference listing image to the user's own product image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agent users use this skill to create product main-image candidates inspired by high-performing competitor or reference images while replacing the subject with their own product. It also guides agents through qhkit setup, option lookup, cost estimation, generation, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends the user's product image and reference image to the qhkit service.

Mitigation: Confirm the user is comfortable sharing those images with qhkit before generation.

Risk: Reference-inspired ecommerce images can accidentally reproduce brand names, logos, watermarks, text, or protected product details.

Mitigation: Keep the prompt constraint to borrow only style and layout, ask for replacement text when needed, and review outputs for brand, logo, watermark, text, and product-detail accuracy before publishing.

Risk: The skill may install or upgrade the third-party npm package @iqinghu/qhkit when the CLI is missing or outdated.

Mitigation: Review and approve npm/global dependency setup or use the documented npx fallback when global install permissions are unsuitable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-clone)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with qhkit shell commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and actual credit usage returned by qhkit.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
