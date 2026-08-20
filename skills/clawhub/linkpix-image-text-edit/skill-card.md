## Description:

Uses the qhkit CLI to edit specified text in ecommerce product images, such as prices, titles, selling points, and promotions, while preserving the rest of the image as much as the generative model allows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and agent users can use this skill to update text in product images without redesigning the image from scratch. Typical tasks include changing prices, titles, selling points, promotion copy, or batches of similar product assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic npm or Node installation and package upgrades can change the execution environment.

Mitigation: Preinstall qhkit through a trusted administrative path and review package updates before use.

Risk: The skill may reuse existing qhkit credentials on the host.

Mitigation: Confirm the intended account and token scope before running generation commands.

Risk: Local product images may be uploaded to the qhkit service for editing.

Mitigation: Confirm that the user is authorized to upload the images and avoid sensitive assets unless approved.

Risk: Generative redrawing may alter product details or produce incorrect text.

Mitigation: Visually inspect generated images, verify prices and spelling, and rerun with a more precise prompt when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-text-edit)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with qhkit CLI commands, configuration guidance, and generated image URLs when generation succeeds.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON stdout details, generated image URLs, and credit usage.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
