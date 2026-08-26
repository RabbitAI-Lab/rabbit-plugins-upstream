## Description:

LinkPix helps agents translate text in ecommerce product images into a target language while preserving the original layout and design style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and cross-border sellers use this skill to localize product listing images in batches. It guides an agent through estimating cost, confirming paid generation parameters, invoking qhkit/LinkPix, and handing back translated image results for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends user images to a paid external LinkPix/qhkit service.

Mitigation: Submit only approved images after showing the user the exact files, target language, and estimate, and require explicit confirmation before generation.

Risk: The skill may ask users to provide an API key to the agent.

Mitigation: Prefer QHKIT_TOKEN or a user-run qhkit config command, and avoid pasting long-lived API keys into chat.

Risk: Generated image translation can alter or mistranslate text, product details, prices, logos, or layout.

Mitigation: Require visual review of each output image and prompt for preserving critical numbers, brand terms, and specifications when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-translate)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix account and API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [LinkPix API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command output summaries and translated image URLs after user-confirmed paid generation.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
