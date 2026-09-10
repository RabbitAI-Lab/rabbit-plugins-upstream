## Description:

This skill helps agents replace the product subject in an e-commerce image while preserving the original scene, composition, perspective, and lighting with LinkPix/qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce content teams and developers use this skill to reuse scene images by swapping in a new product reference while preserving composition and lighting. Agents can produce qhkit commands, prompt guidance, and review checks for scale, perspective, reflections, text, logos, and product structure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade an unpinned third-party npm CLI globally.

Mitigation: Prefer a pinned local install in a restricted environment and review the package before use.

Risk: The workflow uploads selected images to the LinkPix/qhkit service using the user's token.

Mitigation: Confirm token use, expected costs, and whether the selected images may be sent to that service before running generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-product-swap)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local image paths or public image URLs; qhkit returns JSON containing generated image URLs and credit usage.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
