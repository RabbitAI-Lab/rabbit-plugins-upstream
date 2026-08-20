## Description:

Uses the qhkit CLI package @iqinghu/qhkit to help POD sellers generate design assets for print extraction, mockup placement, design variation, and product images across apparel, home goods, accessories, and related print-on-demand categories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External POD sellers and operators use this skill to guide qhkit-based image generation workflows for extracting print designs, creating variants, applying designs to products, estimating credits, and returning generated image URLs. Developers and agents can also use it to install or configure the qhkit CLI before running those workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade global Node packages and relies on the qhkit CLI.

Mitigation: Prefer preinstalling and reviewing @iqinghu/qhkit yourself, then let the agent use the existing CLI rather than performing global installation during a task.

Risk: Selected local images may be uploaded to the LinkPix/qhkit service and account credits may be consumed.

Mitigation: Confirm the exact image inputs, token/account, estimate results, and credit cost before generation.

Risk: The skill may reuse an existing OpenClaw qinghu credential file.

Mitigation: Confirm which credential source is active and use an explicit token or environment variable when account separation matters.

Risk: Generated print designs may differ from source artwork and use of third-party or branded artwork can create rights issues.

Mitigation: Review generated outputs for key visual details and confirm rights for any source designs, brands, or IP before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix / iQingHu workspace](https://www.iqinghu.com)
- [iQingHu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit image generation and may return generated image URLs and credit usage after command execution.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
