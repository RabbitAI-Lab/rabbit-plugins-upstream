## Description:

Helps agents generate ecommerce product hero images that match the composition and visual style of a reference bestseller or competitor image using LinkPix/qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, designers, and agent users use this skill to create product hero image variants based on the layout, color, lighting, and style of a reference listing or competitor image. The skill is intended to replace the subject with the user's own product and avoid copying brands, logos, watermarks, or source-image products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may globally install or update an unpinned third-party npm CLI.

Mitigation: Use a pinned or locally isolated qhkit installation when possible, and review the package source and install behavior before deployment.

Risk: The workflow depends on an external image-generation service and API token configuration.

Mitigation: Avoid putting tokens directly in command text, prefer environment-based secret handling, and confirm the service is approved for the intended data and commercial use.

Risk: Generated ecommerce images may reproduce brand elements, logos, watermarks, text, or product details inaccurately.

Mitigation: Keep the prompt constraint against copying reference products, brands, logos, and watermarks, and manually review generated images before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent to produce or relay generated image URLs and actual credit usage from qhkit responses.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
