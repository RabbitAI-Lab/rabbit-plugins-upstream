## Description:

Helps Lazada and LazMall sellers generate localized product, carousel, detail-page, white-background, scene, and campaign images through Qinghu AI and qhkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Lazada sellers and Southeast Asia ecommerce operators use this skill to prepare localized marketplace visuals, including main-image sets, detail images, and campaign posters. Agents use qhkit to inspect valid image-generation options, estimate credits, submit approved jobs, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the user to provide a Qinghu API token during setup.

Mitigation: Configure the token through QHKIT_TOKEN or another protected local secret mechanism instead of pasting secrets into chat.

Risk: The skill installs or upgrades qhkit and, if needed, Node tooling from network package sources.

Mitigation: Review package installation and upgrade commands before execution and prefer pinned or organization-approved package sources where required.

Risk: Product images are uploaded to an external Qinghu AI service and paid credits may be consumed.

Mitigation: Confirm uploaded images, selected model or template, output count, quality, language, and estimated credits with the user before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-lazada-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated image URLs and credit usage after user confirmation; qhkit stdout is single-line JSON.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
