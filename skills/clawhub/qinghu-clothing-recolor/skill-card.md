## Description:

Helps sellers generate clothing color variants for SKU listings from a single garment photo using Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and creative teams use this skill to create alternate garment colors and SKU images without photographing every color. Review the generated images before publishing product listings.

### Deployment Geography for Use:

Global; requires access to the Qinghu China service and a compatible account.

## Known Risks and Mitigations:

Risk: Selected garment images are uploaded to the Qinghu service.

Mitigation: Confirm permission to upload the images and avoid sharing sensitive or confidential material.

Risk: Installing or updating qhkit and Node changes the user's environment.

Mitigation: Confirm installation with the user and prefer a vetted, pinned package version; avoid persistent PATH changes unless requested.

Risk: API tokens enable use of account credits and could be exposed if mishandled.

Mitigation: Keep tokens private, confirm estimated credits before generation, and report actual credits spent.

Risk: Generated recolors can change product details rather than only the fabric color.

Mitigation: Review logos, text, garment structure, and colors before using the images in listings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-clothing-recolor)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu account and API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, Image links]

**Output Format:** [Markdown guidance with commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits spent; generated recolors may differ in logos, text, garment details, or lighting.]

## Skill Version(s):

0.1.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
