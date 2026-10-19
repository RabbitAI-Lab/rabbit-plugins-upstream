## Description:

Helps replace a product in an e-commerce scene image with a new product while retaining the scene, composition, and lighting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and marketers use this skill to reuse a product scene for a new item, generating an updated image from a scene image and a new-product reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing a third-party CLI or changing shell PATH can affect the local environment.

Mitigation: Use a managed or pinned qhkit install where possible and avoid persistent PATH changes unless intended.

Risk: Source images are sent to the Qinghu service, and the CLI requires an API token.

Mitigation: Upload only images approved for that service and configure the token securely.

Risk: Generated images may alter product details or reuse scenes without permission.

Mitigation: Check logos, text, product structure, perspective, and usage rights before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-product-swap)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key setup](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown guidance and commands with links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image details and reported credit usage should be checked before use.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
