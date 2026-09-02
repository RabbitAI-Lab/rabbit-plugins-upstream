## Description:

Helps ecommerce operators, ad designers, and sellers use qhkit image generation to create and edit product listing images, ad creatives, and ecommerce covers with the Nano Banana 2 / LinkPix workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, advertisers, and sellers use this skill to prepare prompts, choose qhkit image model options, estimate cost, and generate product images, listing creatives, PPC ads, and storefront covers. The workflow supports text-to-image, image-to-image, background replacement, text replacement, and multi-angle composition tasks using user-supplied product references when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install and run the external qhkit CLI and related dependencies locally.

Mitigation: Install only when the qhkit package and local dependency changes are acceptable for the environment.

Risk: The workflow requires API credentials and the security guidance warns against pasting API keys into chat.

Mitigation: Configure credentials directly in a terminal or managed secret store, and avoid exposing API keys in conversation history.

Risk: Generation tasks can consume paid credits.

Mitigation: Confirm model, image count, size, quality, reference images, and estimated credits with the user before submitting any generation command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-nano-banana-2)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Text]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and credit usage returned by qhkit after a user-approved generation task.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
