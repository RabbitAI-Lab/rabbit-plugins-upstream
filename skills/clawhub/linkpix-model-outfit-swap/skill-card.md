## Description:

Generates LinkPix virtual try-on ecommerce images from garment photos and optional model references, with guidance for model choice, prompt setup, cost confirmation, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, creative operators, and agent users use this skill to turn flat-lay or hanger garment photos into realistic model try-on images. The skill supports choosing model demographics, body type, pose, scene, image count, and size while requiring user approval before paid generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can install Node/qhkit tooling and run qhkit shell commands.

Mitigation: Review install commands before execution, use a trusted environment, and surface permission or network failures to the user instead of bypassing them.

Risk: Generation uploads selected local reference images to the LinkPix/qhkit service and can spend credits.

Mitigation: Before any generate action, list the model, image count, size, reference files, and estimated credits, then wait for explicit user approval.

Risk: Generated try-on images can differ from the source garment in text, logos, structure, or fine product details.

Mitigation: Ask the user to inspect critical garment details before using generated images in commercial listings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-model-outfit-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with qhkit JSON command examples and user-facing generation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and actual credit usage after approved qhkit generation.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
