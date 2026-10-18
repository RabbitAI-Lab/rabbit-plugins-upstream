## Description:

Helps 1688 wholesale sellers and factories create product image sets, detail images, and promotional graphics using the Qinghu AI image service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Wholesale sellers, factories, and B2B commerce operators use this skill to prepare 1688 product listings with image sets, product details, and campaign graphics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sharing an API key in chat can expose account credentials.

Mitigation: Configure the token yourself through an environment variable or local CLI command; do not paste it into chat.

Risk: Unpinned package installs can introduce unexpected code changes.

Mitigation: Install only if you trust qhkit/iqinghu; prefer a pinned package version or an isolated environment.

Risk: Product images are uploaded to an external image service.

Mitigation: Confirm you are comfortable sharing the selected images with the service before uploading.

Risk: Image generation spends service credits.

Mitigation: Review estimated costs and generation parameters and obtain explicit approval before submitting a request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-1688-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown with shell commands and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation can consume service credits and requires user confirmation.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
