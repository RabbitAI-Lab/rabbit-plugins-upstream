## Description:

LinkPix helps an agent replace the product subject in an ecommerce scene image with a new product image while preserving the original scene, composition, perspective, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, creative teams, and agents use this skill to reuse product-scene imagery for new products by calling qhkit image generation with two reference images. It is intended for product subject replacement workflows where the user wants the original scene, composition, perspective, and lighting retained.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload selected product and scene images to the qhkit service for remote image generation.

Mitigation: Use only images the user is authorized to process and disclose that selected images are sent to qhkit before generation.

Risk: The skill can consume account credits and may rely on local qhkit credentials.

Mitigation: Estimate credits before generation when cost matters and prefer explicitly provided per-user tokens or an isolated qhkit configuration.

Risk: The skill includes broad installation and upgrade instructions for qhkit and Node.js.

Mitigation: Prefer a preinstalled qhkit environment; when installation is needed, avoid root-level credential reuse and show permission or network failures to the user.

Risk: Generated product replacements may alter details such as text, logos, product structure, reflections, or perspective.

Mitigation: Review the output image for brand, product, scale, lighting, and perspective accuracy before using it in commerce.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-product-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline bash commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The qhkit CLI returns one-line JSON and generated image URLs; the skill instructs the agent to report actual credit usage when generation completes.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
