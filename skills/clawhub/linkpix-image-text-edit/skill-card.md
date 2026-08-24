## Description:

This skill helps agents update text in e-commerce product images by using LinkPix/qhkit image generation to replace titles, prices, selling points, and promotional copy while preserving the rest of the image as much as possible.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce operators use this skill through an agent to revise visible text in product images, such as prices, titles, selling points, and promotional copy, without redesigning the image from scratch.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload product images to the qhkit service.

Mitigation: Use it only with images that are approved for upload to that service, and avoid confidential or restricted assets unless policy allows that transfer.

Risk: Image generation can spend service credits.

Mitigation: Require an explicit confirmation step after showing the model, reference images, output count, dimensions, and estimated credits before submitting a generation request.

Risk: The skill can ask the agent to install or update Node/npm/Python packages.

Mitigation: Run installation steps in a controlled environment and review package installation commands before execution.

Risk: API key handling in chat can expose credentials.

Mitigation: Prefer a secure secret store or preconfigured qhkit credentials; if a key must be provided interactively, treat the conversation as sensitive.

Risk: Generated edits may change product details or render prices and text incorrectly.

Mitigation: Manually inspect the resulting image for text, numbers, logos, and product structure before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-text-edit)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent may return qhkit-generated image URLs and must prompt for review of edited text, prices, logos, and product details.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
