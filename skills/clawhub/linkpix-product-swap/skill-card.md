## Description:

Helps ecommerce teams replace a product in a scene image with a new product while aiming to preserve the scene, composition, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce marketers and content teams use this skill to reuse an existing product scene for a new item, guided by a scene photo and a new product photo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and token configuration are sent to iqinghu/LinkPix through qhkit.

Mitigation: Upload only material approved for the service, protect the API token, and confirm the intended account and site before use.

Risk: Installing or upgrading an external CLI may introduce unreviewed dependencies or change local shell settings.

Mitigation: Prefer a preinstalled or version-pinned qhkit package; avoid persistent PATH changes unless necessary.

Risk: Generative replacement can alter product details or yield implausible perspective, and reused third-party scenes may raise rights concerns.

Mitigation: Inspect the final image for product details, scale, lighting, and reflections; use scene images you have rights to reuse.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-product-swap)
- [qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key setup](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown text with shell commands and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation may consume credits; review the resulting image for product fidelity and natural placement.]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
