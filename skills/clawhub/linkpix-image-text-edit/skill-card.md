## Description:

Helps agents modify text in ecommerce product images by preparing targeted LinkPix/qhkit image-editing prompts, setup steps, cost checks, and delivery guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and agents use this skill to replace prices, titles, selling points, and promotional text in product images while preserving the rest of the image as much as possible. The skill also guides setup, model selection, estimate checks, user confirmation, and result delivery for qhkit image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or invoke qhkit and supporting Node/npm or Python packages.

Mitigation: Confirm trust in the qhkit package and any requested runtime installs before installation or execution.

Risk: The skill requires a qhkit API key for service access.

Mitigation: Treat the API key like a password, prefer scoped or revocable credentials when available, and avoid exposing it in chat or logs.

Risk: Image editing requires uploading user-provided images to the qhkit service.

Mitigation: Use only images the user is authorized to process and avoid sending sensitive or restricted content unless explicitly approved.

Risk: Generation jobs can consume credits and may not be cancellable after submission.

Mitigation: Run an estimate when supported, summarize the model, image count, dimensions, source images, and estimated credits, then wait for explicit user approval before generation.

Risk: Generated edits can introduce wrong text, prices, logos, or product details.

Mitigation: Inspect the output before delivery and ask for a more precise retry when critical text, numbers, or product structure are incorrect.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-text-edit)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command output summaries, generated image URLs, and credit usage when a generation job completes.]

## Skill Version(s):

0.1.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
