## Description:

LinkPix helps an agent recreate the composition and visual style of ecommerce reference images using the user's own product images through qhkit image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and agent operators use this skill to create product main-image variants that follow a reference image's layout, color, and style while substituting their own product imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product or reference images can be uploaded to the qhkit service during generation.

Mitigation: Use images the user has rights to use and avoid uploading sensitive or restricted product imagery.

Risk: Generation can spend qhkit credits after approval.

Mitigation: Run an estimate when supported, summarize selected inputs and expected credits, and submit generation only after explicit user approval.

Risk: The skill stores or uses a qhkit API token.

Mitigation: Prefer environment variables or the documented qhkit config flow, keep tokens out of shared files and logs, and rotate exposed tokens.

Risk: Generated images may differ from the intended product details, text, logo, or structure.

Mitigation: Review outputs before publication and verify key product details, text, logos, and claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-clone)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [LinkPix API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and qhkit credit usage after user-approved generation.]

## Skill Version(s):

0.1.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
