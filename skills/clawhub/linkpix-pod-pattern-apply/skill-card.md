## Description:

LinkPix helps agents generate POD product mockups by applying a supplied print pattern to clothing, hats, mugs, or similar products with perspective, wrinkle, and lighting-aware image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, designers, and ecommerce operators use this skill to prepare POD mockup generation with an agent, applying a pattern image to product imagery or to a described product. The workflow is intended for commercial ClawHub use and includes user confirmation before paid image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install qhkit, configure an API token, upload product or pattern images to the provider, and spend credits on mockup generation.

Mitigation: Confirm provider use, token configuration, image upload, and estimated credit cost with the user before generation.

Risk: Generated mockups may slightly alter pattern details or visual placement.

Mitigation: Review generated images for pattern fidelity, color accuracy, and placement before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-apply)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQingHu workspace](https://www.iqinghu.com)
- [iQingHu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and qhkit credit usage after user confirmation.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
